import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# 데이터 불러오기

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.head())
print()
X.info()
print()
print(y.head())

'''
MedInc	해당 지역의 중앙 소득 (단위: 만 달러)
HouseAge	주택의 평균 연식
AveRooms	가구당 평균 방 개수
AveBedrms	가구당 평균 침실 수
Population	지역 인구 수
AveOccup	가구당 평균 거주 인원
Latitude	위도
Longitude	경도

주택 가격 단위 - 10만 달러
'''

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의
rf_model = RandomForestRegressor(random_state=42)
et_model = ExtraTreesRegressor(random_state=42)

# 하이퍼파라미터 그리드 설정
param_grid = {
    'n_estimators': [50, 100],      # 나무 개수
    'max_depth': [None, 10, 20],    # 최대 깊이
    'min_samples_split': [2, 5]     # 최소 분할 샘플 수
}

# 그리드 서치 설정 (verbose=3 까지 설정 가능)
rf_grid = GridSearchCV(rf_model, param_grid, n_jobs=-1, verbose=2)
et_grid = GridSearchCV(et_model, param_grid, n_jobs=-1, verbose=3)


# 그리드 서치 실행 및 모델학습
print('\n======= 랜덤포레스트 그리드 서치 =======\n')
rf_grid.fit(X_train, y_train)

print('\n======= 엑스트라트리 그리드 서치 =======\n')
et_grid.fit(X_train, y_train)


# 최적의 옵션 조합 출력
print('\n랜덤포레스트 best:', rf_grid.best_params_)
print('\n엑스트라트리 best:', et_grid.best_params_)

# 최적 모델
rf_best = rf_grid.best_estimator_
et_best = et_grid.best_estimator_

# 성능평가
print('\n랜덤포레스트 스코어:', rf_best.score(X_test, y_test))
print('\n엑스트라트리 스코어:', et_best.score(X_test, y_test))

# 특성 중요도
print('\n랜덤포레스트 특성 중요도:', rf_best.feature_importances_)
print('\n엑스트라트리 특성 중요도:', et_best.feature_importances_)