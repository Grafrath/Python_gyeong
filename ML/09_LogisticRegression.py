import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
ss = StandardScaler()
lr = LogisticRegression()

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
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42 )
print('분할 완료')
print()

print('\n================ 인풋 데이터 스케일링 ================\n')
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
print('스케일링 완료')
print()

print('\n================  모델 준비 ================\n')
# 최근접 이웃 회귀 모델 준비
kn = KNeighborsClassifier(n_neighbors=3)
print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
# 모델 훈련
kn.fit(train_scaled, train_target)
print('모델 훈련 완료')
print()

print('\n================ 모델 학습 완료 ================\n')
# 테스트셋 예측
y_pred = kn.predict(test_scaled)

print('\n 트레인 스코어 ', kn.score(train_scaled, train_target))
print('\n 테스트 스코어 ', kn.score(test_scaled, test_target))
print()

print('정확도: ', accuracy_score(test_target, y_pred))
print()

print(kn.classes_) 
print()

proba = kn.predict_proba(test_scaled[:5])

print(np.round(proba, decimals=4))
print()

print('\n================ 그래프 ================\n')
print('그래프 출력')
print()

distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target[indexes[0]])

z = np.arange(-5, 5, 0.1)
phi = 1/(1 + np.exp(-z))

plt.plot(z, phi)
plt.xlabel('x')
plt.ylabel('phi')
plt.show()

print('\n================ 모델 준비 ================\n')

char_arr = np.array(['A', 'B', 'C', 'D', 'E'])
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

test_bream_smelt_indexes = (test_target == 'Bream') | (test_target == 'Smelt')
test_bream_smelt = test_scaled[test_bream_smelt_indexes]
test_target_bream_smelt = test_target[test_bream_smelt_indexes]

print('모델 준비 완료')
print()

print('\n================ 모델 훈련 ================\n')
lr.fit(train_bream_smelt, target_bream_smelt) 
print('모델 훈련 완료')
print()

print('\n================ 모델 학습 완료 ================\n')
# 테스트셋 예측
y_pred = lr.predict(train_bream_smelt[:5])

print('\n 트레인 스코어 ', lr.score(train_bream_smelt, target_bream_smelt))
print('\n 테스트 스코어 ', lr.score(test_bream_smelt, test_target_bream_smelt))
print(lr.predict(train_bream_smelt[:5]))
print()

print('클래스 종류:', lr.classes_) 
print()

proba = lr.predict_proba(train_bream_smelt[:5])
print('예측 확률 ([:5]): ', np.round(proba, decimals=4))
print()

print('기울기(coef_):', lr.coef_)
print('절편(intercept_):', lr.intercept_)
print()

from scipy.special import expit
decisions = lr.decision_function(train_bream_smelt[:5])
print('결정 함수 값:', decisions)
print()

print('시그모이드 통과 확률:', expit(decisions))
print()

print('\n================ 그래프 ================\n')
print('그래프 출력')
print()
