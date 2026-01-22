import pandas as pd

fish = pd.read_csv('./data/fish_data.csv')

print(fish.head())
print()
fish.info()

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()

'''
'Bream'   'Roach'   'Whitefish' 'Parkki' 'Perch'  'Pike'   'Smelt'
 참붕어   붉은줄납줄개    백어       파르키    농어    가시고기    빙어
'''

# 인풋 데이터
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]

print(fish_input.head())
print()

# 타겟 데이터
fish_target = fish['Species']

# 훈련/테스트 셋 분리
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

# 스케일링(표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# =====================================================================

# 확률적 경사하강법
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)

# 데이터 한개에 업데이트 한 번
# max_iter = 10 >>> 10 에포크 (전체 데이터 10번 순회)
print('\n======= SGD 학습 스코어 =======\n')
print('훈련 스코어:', sc.score(train_scaled, train_target))
print('테스트 스코어:', sc.score(test_scaled, test_target))

# 추가 학습 가능 (온라인 학습 가능 모델)
# 1 에포크 학습
sc.partial_fit(train_scaled, train_target)

print('\n======= SGD 추가 학습 1회차 =======\n')
print('훈련 스코어:', sc.score(train_scaled, train_target))
print('테스트 스코어:', sc.score(test_scaled, test_target))


# 한번더 추가학습
sc.partial_fit(train_scaled, train_target)

print('\n======= SGD 추가 학습 2회차 =======\n')
print('훈련 스코어:', sc.score(train_scaled, train_target))
print('테스트 스코어:', sc.score(test_scaled, test_target))

import pandas as pd
import numpy as np
import sklearn
import scipy

print("pandas version:", pd.__version__)
print("numpy version:", np.__version__)
print("scikit-learn version:", sklearn.__version__)
print("scipy version:", scipy.__version__)
