fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import numpy as np

print('\n======= 넘피 컬럼스택 =======\n')
print(np.column_stack(([1,2,3], [4,5,6])))


print('\n======= 도미/빙어 인풋 데이터 준비 =======\n')
fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data[:5])

print('\n======= 정답지 생성 =======\n')
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)


from sklearn.model_selection import train_test_split

# 알아서 섞어준다.
# 디폴트 비율 75:25 (트레인:테스트) 비율

train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, test_size=0.25, random_state=42)

print('\n======= 트레인 / 테스트 input 크기 =======\n')
print(train_input.shape, test_input.shape)

print('\n======= 트레인 / 테스트 target 크기 =======\n')
print(train_target.shape, test_target.shape)

print('\n======= 테스트 target =======\n')
print(test_target)

# 훈련(train)
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)

# 테스트(test) 스코어
print('\n======= 훈련 스코어 =======\n')
print(kn.score(test_input, test_target))


# ======================================================

# 25, 150 물고기 어획.

import matplotlib.pyplot as plt

# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


print('\n======= 월척의 어종은? =======\n') 
print(kn.predict([[25, 150]]))


# 월척 근처 이웃들 누군지 인덱스 뽑아보자
distances, indexes = kn.kneighbors([[25, 150]])
print('\n근처 이웃들 인덱스:', indexes)


# 그래프로 이웃들 확인해보기
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.scatter(train_input[indexes, 0], train_input[indexes, 1], marker='D')
# # train_input[[12, 29, 5, 19, 4],1] 한 것과 같음.
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


# x축 늘려서 산점도 압축시키기
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.scatter(train_input[indexes, 0], train_input[indexes, 1], marker='D')
# # train_input[[12, 29, 5, 19, 4],1] 한 것과 같음.
# plt.xlim((0, 1000))
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


# 스케일링 (표준화)
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

print('\n평균:', mean)
print('표준편차:', std)

train_scaled = (train_input - mean) / std

# 표준화 후 그래프
# plt.scatter(train_scaled[:,0], train_scaled[:,1])
# plt.scatter(25, 150, marker='^')
# plt.title('After Scaling Train_input')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


# 월척도 스케일링 해주자.
new = ([25, 150] - mean) / std

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.title('After Scaling All')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# 다시 훈련
kn.fit(train_scaled, train_target)
print('\n======= 재훈련 완료 =======\n')

test_scaled = (test_input - mean) / std

print('\n스코어:', kn.score(test_scaled, test_target))
print('\n월척 어종:', kn.predict([new]))


distances, indexes = kn.kneighbors([new])

# 이웃들 다시 확인해 보자.
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()