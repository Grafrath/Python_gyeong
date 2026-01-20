import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
kn = KNeighborsRegressor()


perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

print('\n================ 훈련/테스트 분할 ================\n')
# 훈련/테스트 분할
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42 )
print('분할 완료')
print()

print('\n================ 인풋 데이터 reshape ================\n')
# 인풋 데이터 reshape
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
print('reshape 완료')
print()

print('\n================ 최근접 이웃 회귀 모델 준비 ================\n')
# 최근접 이웃 회귀 모델 준비
kn = KNeighborsRegressor(n_neighbors=3)
print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
# 모델 훈련
kn.fit(train_input, train_target)
print('모델 훈련 완료')
print()

print('\n================ 길이 50 ================\n')
# 50cm 농어 무게 예측
print(kn.predict([[50]]))
print()

print('\n================ 그래프 ================\n')
# 그래프그리기(훈련세트, 50cm 농어 이웃과 50cm 농어)
distances, indexes = kn.kneighbors([[50]])

print('그래프 출력')
print()

plt.scatter(train_input, train_target)
plt.scatter(50, kn.predict([[50]]), marker='^')
plt.scatter(100, kn.predict([[100]]), marker='^')
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# KNN(최근접 이웃) 모델의 한계
# 훈련 세트 범위 밖의 데이터는 정확한 예측이 어려움
# KNN 모델은 훈련 데이터의 범위를 벗어나면 가장 가까운 데이터의 값만 반복해서 출력됨

#선형 회귀(Linear Regression) 모델

print('\n================ 선형 회귀 모델 준비 ================\n')
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
lr.fit(train_input, train_target)
print('모델 훈련 완료')
print()

print('\n================ 길이 50 ================\n')
print(lr.predict([[50]]))
print()

print('기울기', lr.coef_)
print('절편', lr.intercept_)

print('\n================ 그래프 ================\n')
# 그래프그리기(훈련세트, 50cm 농어 이웃과 50cm 농어)

print('그래프 출력')
print()

plt.scatter(train_input, train_target)
plt.plot([15, 50], [15 * lr.coef_ + lr.intercept_, 50 * lr.coef_ + lr.intercept_])
plt.scatter(50, lr.predict([[50]]), marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('\n================ 다항 회귀 ================\n')
# 제곱항 추가
train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))
lr = LinearRegression()
lr.fit(train_poly, train_target)

print(train_poly.shape)
print(test_poly.shape)
print('모델 준비 및 훈련 완료')
print()

print('\n================ 길이 50 ================\n')
pred_data = np.array([[50**2, 50]])
print(pred_data)
print() 

print('\n================ 파라매터 ================\n')
print('기울기', lr.coef_)
print('절편', lr.intercept_)
print()

print('\n================ 그래프 ================\n')
# 그래프그리기(훈련세트, 50cm 농어 이웃과 50cm 농어)

print('그래프 출력')
print()

point = np.arange(15, 51)
plt.scatter(train_input, train_target)
plt.plot(point, lr.coef_[0]*point**2 + lr.coef_[1]*point + lr.intercept_)
plt.scatter(50, lr.predict(pred_data), marker='^')
plt.title('Polynomial Regression (2nd degree)')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()