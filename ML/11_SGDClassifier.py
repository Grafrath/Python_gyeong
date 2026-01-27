import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier

fish = pd.read_csv('./data/fish_data.csv')

'''
['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
 참붕어 붉은줄납줄개  백어      파르키    농어   가시고기  빙어
'''

print(fish)
fish.info()
print()

print(pd.unique(fish['Species']))
print()

print('\n================ 훈련/테스트 분할 ================\n')
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]
fish_target = fish['Species']



train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42 )
print('분할 완료')
print()

print('\n================ 인풋 데이터 스케일링 ================\n')
ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
print('스케일링 완료')
print()

print('\n================ 모델 훈련 ================\n')
sc = SGDClassifier(loss='log_loss',
                   max_iter=10,
                   random_state=42,
                   tol=1e-4,
                   n_iter_no_change=20)
sc.fit(train_scaled, train_target) 
print('모델 훈련 완료')
print()

# 확률적 경사하강법
# 데이터 한개에 업데이트 한번,
# max_iter = 10 -> 10 에포크 (전체 데이터 10번 순회)


print('\n================ sgdc 학습 스코어 점수 ================\n')
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

# 추가 학습 가능 (온라인 모델)
print('\n================ 1회 추가학습 스코어 점수 ================\n')
sc.partial_fit(train_scaled, train_target)
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

print('\n================ 2회 추가학습 스코어 점수 ================\n')
sc.partial_fit(train_scaled, train_target)
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

print('\n================ 3회 추가학습 스코어 점수 ================\n')
sc.partial_fit(train_scaled, train_target)
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

print('\n================ 4회 추가학습 스코어 점수 ================\n')
sc.partial_fit(train_scaled, train_target)
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

print('\n================ 5회 추가학습 스코어 점수 ================\n')
sc.partial_fit(train_scaled, train_target)
print('\n 트레인 스코어 ', sc.score(train_scaled, train_target))
print('\n 테스트 스코어 ', sc.score(test_scaled, test_target))
print()

# 추가 학습 가능 (온라인 모델)
print('\n================ 추가학습 스코어 그래프 ================\n')
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(0, 300):
    sc.partial_fit(train_scaled, train_target, classes=classes)
    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))

plt.plot(train_score, label='train')
plt.plot(test_score, label='test')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.show()

train_score = np.array(train_score)
test_score = np.array(test_score)

# 1. 두 점수의 차이 계산
gap = np.abs(train_score - test_score)

# 2. 골든 지점 찾기 
# (조건: 테스트 점수가 상위 50% 이상인 것 중 차이가 가장 적은 곳)
threshold = np.median(test_score)
candidates = np.where(test_score >= threshold)[0]
golden_epoch = candidates[np.argmin(gap[candidates])]

print(f"최적의 에포크(골든 지점): {golden_epoch}")
print(f"당시 테스트스코어 정확도: {test_score[golden_epoch]:.3f}")
print(f"당시 트레인스코어 정확도: {train_score[golden_epoch]:.3f}")

# 3. 그래프 보완
plt.plot(train_score, label='train')
plt.plot(test_score, label='test')
plt.axvline(x=golden_epoch, color='r', linestyle='--', label='Golden Point') # 수직선 추가
plt.legend()
plt.show()
