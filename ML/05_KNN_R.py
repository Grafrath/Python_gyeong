import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 이제까진 길이와 무게로 종류 분류
# 이제부턴 길이로 무게 예측

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42
)

print('\n================ 인풋 데이터 셰잎 ================\n')
print(train_input.shape)
print(test_input.shape)
print()

print('\n================ 넘피 reshape ================\n')
test_arr = np.array([1, 2, 3, 4])
print(test_arr.shape)
print()

test_arr = test_arr.reshape(2, 2)
print(test_arr)
print(test_arr.shape)
print()

print('\n================ 모양 바꾸기 전 ================\n')
print(train_input)
print()

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

print('\n================ 모양 바꾼후 ================\n')
print(train_input)
print()

print(train_input.shape)
print(test_input.shape)
print()

kn.fit(train_input, train_target)
print('\n================ 모델 훈련 완료 ================\n')

# 테스트셋 예측
y_pred = kn.predict(test_input)

print('\n 예측값 ', y_pred)
print('\n 실제값 ', test_target)

print('\n================ kn 테스트 스코어 ================\n')
print('테스트 스코어 ', kn.score(test_input, test_target))

print('\n================ kn 트레인 스코어 ================\n')
print('트레인 스코어 ', kn.score(train_input, train_target))

kn = KNeighborsRegressor(n_neighbors=3)
kn.fit(train_input, train_target)
print('\n================ 모델 다시 훈련 ================\n')

print('\n================ kn 테스트 스코어 ================\n')
print('테스트 스코어 ', kn.score(test_input, test_target))

print('\n================ kn 트레인 스코어 ================\n')
print('트레인 스코어 ', kn.score(train_input, train_target))

x = np.arange(5, 50).reshape(-1, 1)
prediction = kn.predict(x)
plt.scatter(train_input, train_target)
# 5 ~ 45 길이에 대한 무게 그래프
plt.plot(x, prediction, color='red')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

knr = KNeighborsRegressor()

x = np.arange(5, 45).reshape(-1, 1)

# for i in [1, 5, 10]:
#     knr.n_neighbors = i
#     knr.fit(train_input, train_target)
#     # 5~45까지 넣어가며 예측시키기
#     prediction = knr.predict(x)

#     # 원래 데이터 산점도
#     plt.scatter(train_input, train_target)
#     # 5 ~ 45 길이에 대한 무게 그래프
#     plt.plot(x, prediction, color='red')
#     plt.title(f'knr.n_neighbors {i}')
#     plt.xlabel('length')
#     plt.ylabel('weight')
#     plt.show()