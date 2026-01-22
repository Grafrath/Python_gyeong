import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy.special import expit
from scipy.special import softmax

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_absolute_error

diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target


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

print('\n================ 데이터 준비 ================\n')
print('샘플수, 특성수: ', x.shape)
print('샘플수: ', y.shape)
print('특성 이름: ', diabetes.feature_names)
print()

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)

print('\n================ 훈련/테스트 분할 ================\n')
train_x, test_x, train_y, test_y = train_test_split(x, y, random_state=42)
print('분할 완료')
print()

print('\n================ 인풋 데이터 스케일링 ================\n')
ss = StandardScaler()
ss.fit(train_x)

train_scaled = ss.transform(train_x)
test_scaled = ss.transform(test_x)
print('스케일링 완료')
print()

print('\n================ 모델 훈련 ================\n')
sc = SGDRegressor(max_iter=1000, random_state=42, tol=1e-3)
sc.fit(train_scaled, train_y) 
print('모델 훈련 완료')
print()

print('\n================ sgdR 학습 스코어 점수 ================\n')
print('\n 트레인 스코어 ', sc.score(train_scaled, train_y))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_y))
print()

test_pred = sc.predict(test_scaled)

# 2. 평균 절대 오차 계산 (실제 당뇨 수치와 평균적으로 얼마 차이나는지)
mae = mean_absolute_error(test_y, test_pred)
print(f'평균 절대 오차(MAE): {mae:.2f}')

# 3. 시각화 (실제값 vs 예측값)
plt.scatter(test_y, test_pred, alpha=0.5)
plt.plot([min(test_y), max(test_y)], [min(test_y), max(test_y)], '--r') # 기준선
plt.xlabel('Actual')
plt.ylabel('Predict')
plt.title('Actual vs Predict')
plt.show()
