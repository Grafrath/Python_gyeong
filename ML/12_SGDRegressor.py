# age: 나이 (years)
# sex: 성별 (보통 성별에 따라 이진화되거나 정규화된 값)
# bmi: 체질량 지수 (Body Mass Index)
# bp: 평균 혈압 (Average Blood Pressure)
# s1: tc, 총 혈청 콜레스테롤 (Total serum cholesterol)
# s2: ldl, 저밀도 지단백질 (Low-density lipoproteins)
# s3: hdl, 고밀도 지단백질 (High-density lipoproteins)
# s4: tch, 총 콜레스테롤/HDL 비율 (Total cholesterol / HDL)
# s5: ltg, 혈청 트리글리세라이드 수치 로그값 (Possibly log of serum triglycerides level)
# s6: glu, 혈당 수치 (Blood sugar level)

import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=500, precision=3)
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target
print(X)
print(y)
print()

feature_names = diabetes.feature_names

print('X shape (샘플수, 특성수):', X.shape)
print('y shape (샘플수,):', y.shape)
print('컬럼 이름:', feature_names)


# 데이터 분리 (8:2)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
                                                    
# 모델 준비 / 학습
from sklearn.linear_model import SGDRegressor

sgd = SGDRegressor(max_iter=1000, tol=1e-4, n_iter_no_change=20,
                   random_state=42)
sgd.fit(X_train, y_train)

# 평가
print('\n훈련 스코어:', sgd.score(X_train, y_train))
print('\n테스트 스코어:', sgd.score(X_test, y_test))

print('\n파라미터', sgd.coef_, sgd.intercept_)
print('\n실행된 에포크', sgd.n_iter_)
