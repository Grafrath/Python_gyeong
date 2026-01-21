import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(include_bias=False)

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

perch_full = pd.read_csv('./ML/perch_data.csv')

train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight, random_state=42 )

poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print('\n================ 인풋 데이터 2제곱 특성공학 ================\n')
print(train_poly)
print()
print(test_poly)
print()

print('\n================ 인풋 데이터 shape ================\n')
print(f'변환 전 특성 개수: {train_input.shape }')
print(f'변환 후 특성 개수: {train_poly.shape}')
print()

print('\n================ poly.get_feature_names_out ================\n')
print(f'생성된 특성 조합: {poly.get_feature_names_out()}')
print()

# ================ 스케일링 ================
# 평균을 0으로 표준편차를 1로 만듦 -> 데이터들이 대략 -3 ~ 3 근처로 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

# ================ 릿지회귀 ================
# 손실함수 = MSE + L2 정규항
# 영향이 없는 특성은 파라미터가 작아짐
# 닫힌해 바로 구함

print('\n================ 릿지 회귀 모델 준비 ================\n')
from sklearn.linear_model import Ridge
rd = Ridge()
start = time.time()
print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
rd.fit(train_scaled, train_target)
end = time.time()
print('모델 훈련 완료')
print('훈련시간: ', end - start  , '초')
print()

print('\n================ 스코어 ================\n')
print('훈련 스코어: ', rd.score(train_scaled, train_target))
print()
print('테스트 스코어: ', rd.score(test_scaled, test_target))
print()

print('\n================ 릿지모델 파라미터 ================\n')
print('기울기', rd.coef_)
print('절편', rd.intercept_)

# 최적의 규제값 찾기

train_score = []
test_score = []
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

for a in alpha_list:
    rd = Ridge(alpha=a)
    rd.fit(train_scaled, train_target)
    train_score.append(rd.score(train_scaled, train_target))
    test_score.append(rd.score(test_scaled, test_target))

# plt.plot(alpha_list, train_score, color='red', label='train')
# plt.plot(alpha_list, test_score, color='blue', label='test')
# plt.xscale('log')
# plt.xlabel('Alpha')
# plt.ylabel('R^2')
# plt.legend()
# plt.show()

rd = Ridge(alpha=0.1)
rd.fit(train_scaled, train_target)

print('\n================ 최종  스코어 ================\n')
print('훈련 스코어: ', rd.score(train_scaled, train_target))
print()
print('테스트 스코어: ', rd.score(test_scaled, test_target))
print()

print('\n================    파라미터 ================\n')
print('기울기', rd.coef_)
print('절편', rd.intercept_)
print()

print('\n================ 라쏘 회귀 모델 준비 ================\n')
from sklearn.linear_model import Lasso
ls = Lasso()
start = time.time()
print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
ls.fit(train_scaled, train_target)
end = time.time()
print('모델 훈련 완료')
print('훈련시간: ', end - start  , '초')
print()

print('\n================ 스코어 ================\n')
print('훈련 스코어: ', ls.score(train_scaled, train_target))
print()
print('테스트 스코어: ', ls.score(test_scaled, test_target))
print()

print('\n================ 라쏘모델 파라미터 ================\n')
print('기울기', ls.coef_)
print('절편', ls.intercept_)
print()

# 최적의 규제값 찾기

train_score = []
test_score = []
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

for a in alpha_list:
    ls = Lasso(alpha=a)
    ls.fit(train_scaled, train_target)
    train_score.append(ls.score(train_scaled, train_target))
    test_score.append(ls.score(test_scaled, test_target))

plt.plot(alpha_list, train_score, color='red', label='train')
plt.plot(alpha_list, test_score, color='blue', label='test')
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()

ls = Lasso(alpha=1, max_iter=100000)
ls.fit(train_scaled, train_target)

print('\n================ 최종  스코어 ================\n')
print('훈련 스코어: ', ls.score(train_scaled, train_target))
print()
print('테스트 스코어: ', ls.score(test_scaled, test_target))
print()

print('\n================    파라미터 ================\n')
print('기울기', ls.coef_)
print('절편', ls.intercept_)
print()