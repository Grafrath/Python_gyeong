'''
<그라디언트 부스팅>
오차를 순차적으로 줄이는 학습
약한 모델(주로 얕은 결정트리)를 여러 개 만들고, 이전 모델이 틀린 부분을 다음 모델이 보완하도록
순차적으로 학습, 앙상블 방식이기 때문에 단일 모델보다 일반적으로 높은 정확도를 보여줌.
다양한 옵션으로 모델 학습 과정을 세밀하게 제어할 수 있다.
'''

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier
from sklearn.model_selection import cross_validate
from sklearn.inspection import permutation_importance

wine = pd.read_csv('./data/wine_data.csv')

print(wine.head())
print()
wine.info()
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)

print('\n================ 기본 gb 훈련/검증 스코어 ================\n')

print('훈련점수: ',np.mean(scores['train_score']))
print('검증점수: ', np.mean(scores['test_score']))
print()

gb = GradientBoostingClassifier(n_estimators=500, max_depth=3, # 얖은 트리 깊이 및 트리 최대 깊이, 디폴트 각 100, 3
                                learning_rate=0.1, random_state=42) # 학습률, 디폴트 0.1
scores = cross_validate(gb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

print('\n================ gbm gb 훈련/검증 스코어 ================\n')

print('훈련점수: ',np.mean(scores['train_score']))
print('검증점수: ', np.mean(scores['test_score']))
print()

gb.fit(train_input, train_target)
print('특성 중요도: ', gb.feature_importances_)
print()

# 히스토그램 기반 GB모델
# 데이터를 255개의 구간에 균등 개수로 할당(기본 max_bin=255)
# 각 구간의 오른쪽 값을 기반으로 분할을 계산

print('\n================ 모델 훈련 ================n')

hgb = HistGradientBoostingClassifier(max_bins=128,  # 구간 개수
                                     max_iter=300,  # 얕은 트리 갯수
                                     max_depth=3,   # 최대 깊이
                                     learning_rate=0.1,
                                     random_state=42)
scores = cross_validate(hgb, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

print('\n================ gbm hgb 훈련/검증 스코어 ================\n')

print('훈련점수: ',np.mean(scores['train_score']))
print('검증점수: ', np.mean(scores['test_score']))
print()

print('\n================ 모델 학습 ================n')
hgb.fit(train_input, train_target)

result = permutation_importance(hgb, train_input, train_target, 
                                n_repeats=10, random_state=42, n_jobs=-1)

print('hgb 특성 중요도(훈련세트):', result.importances_mean)
print()

result_test = permutation_importance(hgb, test_input, test_target, 
                                     n_repeats=10, random_state=42, n_jobs=-1)

print('hgb 특성 중요도(테스트세트):', result_test.importances_mean)
print()

# 모델 학습

# 모델 평가