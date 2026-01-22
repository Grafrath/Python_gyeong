import pandas as pd
import numpy as np

from scipy.special import softmax
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

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
ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
print('스케일링 완료')
print()

print('\n================ 모델 훈련 ================\n')
lr = LogisticRegression(C=20, max_iter=1000, solver='lbfgs')
lr.fit(train_scaled, train_target) 
print('모델 훈련 완료')
print()

print('\n================ 스코어 점수 ================\n')
print('\n 트레인 스코어 ', lr.score(train_scaled, train_target))
print('\n 테스트 스코어 ', lr.score(test_scaled, test_target))
print()

print('\n================ 상위 5개행값 ================\n')
y_pred = lr.predict(train_scaled[:5])
print(y_pred)
print()

print('클래스 종류:', lr.classes_) 
print()

print('\n================ 파라미터 개수 ================\n')
print('기울기(coef_):', lr.coef_)
print('절편(intercept_):', lr.intercept_)
print()

print('\n================ 상위 5개행 클래스별 z값 출력 ================\n')
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))
print()

print('\n================ 소프트맥스 함수에 z값 대입 ================\n')
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))
print()
