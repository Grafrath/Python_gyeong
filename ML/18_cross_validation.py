import pandas as pd

wine = pd.read_csv('./data/wine_data.csv')

print(wine.head())
wine.info()
print()
print(wine.describe())


data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

print('\n======= 와인 클래스 종류 =======\n')
print(target.unique())



from sklearn.model_selection import train_test_split

# 훈련 - 테스트 나누기
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)


# 훈련셋 >>> 훈련 - 검증 나누기
sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)



print('\n======= 훈련-검증 세트 크기 =======\n')
print(sub_input.shape, val_input.shape)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)

print('\n======= 훈련/검증 스코어 =======\n')
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

# 진짜 테스트 스코어
print('\n======= 테스트 스코어 =======\n')
print(dt.score(test_input, test_target))


# ========================= 교차검증 =========================

from sklearn.model_selection import cross_validate

# 교차검증
# 디폴트 5분할
scores = cross_validate(dt, train_input, train_target)
print('\n======= 교차검증 스코어 =======\n')
print(scores)

import numpy as np

print('\n======= 교차검증 평균 스코어 =======\n')
print(np.mean(scores['test_score']))

from sklearn.model_selection import StratifiedKFold

# 분류 디폴트 cv=StratifiedKFold, 회귀 = KFold()
scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())
print(np.mean(scores['test_score']))

# ======================================================

# 교차검증 상세 옵션 설정
# shuffle 디폴트 False ==> train_test_split 에서 한번 섞어주긴 했지만, 한 번 더 섞는 것이 안전.
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)

print('\n======= 교차검증 평균 스코어 (상세옵션) =======\n')
print(np.mean(scores['test_score']))