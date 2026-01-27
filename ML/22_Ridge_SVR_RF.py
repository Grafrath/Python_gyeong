import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

# 데이터 불러오기
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.head())
X.info()
print()
print(y.head())

# 훈련/테스트 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 공통설정
scoring = 'neg_root_mean_squared_error' # sklearn 규칙 - 모든 score는 '클수록 좋은값' 이어야한다.
cv = 5
n_jobs = -1
verbose = 1

# 5번의 교차검증을 해야되는데, 할 때마다 스케일링을 따로 해줘야한다. 
# 그래서 훈련데이터를 먼저 스케일리을 해놓으면 안된다. 
# 파이프라인에 스케일링을 넣어 놓으면 교차검증시마다 따로 스케일링 해준다. 

# 1) Ridge (스케일링 + Ridge)
ridge_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge(random_state=42))
])

# 모델__옵션 >>> 언더바 2개
ridge_param_grid = {
    "ridge__alpha":[0.01, 0.1, 1, 10, 100, 300, 1000]
    }

ridge_grid = GridSearchCV(
    ridge_pipe, ridge_param_grid, cv=cv, scoring=scoring, n_jobs=n_jobs, verbose=verbose
)

# 2) SVR (스케일링 + SVR)
svr_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svr", SVR())
])

svr_param_grid = {
    "svr__kernel":["rbf"],
    "svr__C": [1, 10, 100],
    "svr__gamma": ["scale", 0.01, 0.1],
    "svr__epsilon": [0.05, 0.1, 0.2]
}

svr_grid = GridSearchCV(
    svr_pipe, svr_param_grid, cv=cv, scoring=scoring, n_jobs=n_jobs, verbose=verbose
)

# 3) RandomForest (스케일링이 불필요)
rf_model = RandomForestRegressor(random_state=42)

rf_param_grid = {
    "n_estimators": [100, 300],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2, 5],
    "max_features": ["sqrt", 1.0]
}

rf_grid = GridSearchCV(
    rf_model, rf_param_grid, cv=cv, scoring=scoring, n_jobs=n_jobs, verbose=verbose
)

# 학습
print("Ridge 그리드 서치")
ridge_grid.fit(X_train, y_train)
print()

print("SVR 그리드 서치")
svr_grid.fit(X_train, y_train)
print()

print("RandomForest 그리드 서치")
rf_grid.fit(X_train, y_train)
print()

# 평가함수
def evaluate(name, grid):
    best = grid.best_estimator_
    pred = best.predict(X_test)

    mse = mean_squared_error(y_test, pred)
    test_rmse = np.sqrt(mse)
    test_r2 = r2_score(y_test, pred)  # 최대값: 1, 최소값: 음수무한대
    cv_rmse = -grid.best_score_

    print(f"[{name}]")
    print("best params:", grid.best_params_)
    print(f"CV RMSE:   {cv_rmse:.4f}")
    print(f"Test RMSE: {test_rmse:.4f}")
    print(f"Test R2:   {test_r2:.4f}")
    print()

evaluate("Ridge", ridge_grid)
evaluate("SVR", svr_grid)
evaluate("RandomForest", rf_grid)