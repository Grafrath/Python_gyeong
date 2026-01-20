import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
kn = KNeighborsClassifier()

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = [[l, w] for l, w in zip (fish_length, fish_weight)]
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

train_input, test_input, train_target, test_target = train_test_split(
    input_arr, target_arr, test_size=0.25, random_state=42)

print('\n================ 트레인 / 테스트 input 크기 ================\n')
print(train_input.shape, test_input.shape)
print()

print('\n================ 트레인 / 테스트 target 크기 ================\n')
print(train_target.shape, test_target.shape)
print()

print('\n================ 테스트 target ================\n')
print(test_target)
print()

kn.fit(train_input, train_target)
print(kn.score(test_input, test_target))
print()

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(kn.predict([[25, 150]]))
print()

distances, indexs = kn.kneighbors([[25, 150]])
print('\n================ 근처 인덱스 ================\n')
print(indexs)
print()

print('\n================ 근처 인덱스 확인 ================\n')
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexs, 0], train_input[indexs,1])
# plt.scatter(train_input[indexs, 0], train_input[[12, 29, 5, 19, 4],1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

print('평균: ', mean)
print()
print('표준편차: ', std)
print()

train_scatter = (train_input - mean) / std

# plt.scatter(train_scatter[:,0], train_scatter[:,1], label='train_scaled')
# plt.scatter(25, 150, marker='^')
# plt.title('After Scaling All1')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.legend()
# plt.show()

new = ([25, 150] - mean) / std

plt.scatter(train_scatter[:,0], train_scatter[:,1], label='train_scaled')
plt.scatter(new[0], new[1], marker='^')
plt.title('After Scaling All')
plt.xlabel('length')
plt.ylabel('weight')
plt.legend()
plt.show()

# 재훈련
kn.fit(train_scatter, train_target)
print('\n================ 재훈련 완료 ================\n')

test_scaled = (test_input - mean) / std

print('스코어 ', kn.score(test_scaled, test_target))
print('월척 어종', kn.predict([new]))

distances, indexs = kn.kneighbors([new])

plt.scatter(train_scatter[:,0], train_scatter[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_input[indexs, 0], train_input[indexs,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('\n================ 이웃들 거리 ================\n')
print(distances)