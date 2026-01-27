# 결정트리 - 의사 결정 나무

import pandas as pd

# wine = pd.read_csv('https://bit.ly/wine_csv_data')
# wine.to_csv('./data/wine_data.csv', index=False)

wine = pd.read_csv('./data/wine_data.csv')


print(wine.head())
print()
wine.info()
print()
print(wine['class'].unique()) # 0 레드와인 / 1 화이트와인
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']

# 데이터 분할
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

# 스케일링
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import LogisticRegression

# 학습
lr = LogisticRegression()
lr.fit(train_scaled, train_target)

# 훈련 / 테스트 스코어
print('\n===== 로지스틱 리그레션 훈련/테스트 스코어 =====\n')
print('훈련 스코어:', lr.score(train_scaled, train_target))
print('테스트 스코어:', lr.score(test_scaled, test_target))

# 파라미터  값 확인
print('\n======= 파라미터 확인 ======\n')
print(lr.coef_, lr.intercept_)
print()

# ===================================================

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)


# 훈련 / 테스트 스코어
print('\n===== 결정나무 훈련/테스트 스코어 =====\n')
print('훈련 스코어:', dt.score(train_scaled, train_target))
print('테스트 스코어:', dt.score(test_scaled, test_target))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# plt.figure(figsize=(10,7))
# plot_tree(dt)
# plt.show()

# plt.figure(figsize=(10,7))
# plot_tree(dt, max_depth=1, filled=True,
#           feature_names=['alcohol', 'sugar', 'pH'])
# plt.show()

# 트리 깊이를 3으로 제한 (디폴트 무제한)
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)

print('\n===== 깊이 3 나무 스코어 =====\n')
print('훈련 스코어:', dt.score(train_scaled, train_target))
print('테스트 스코어:', dt.score(test_scaled, test_target))

# plt.figure(figsize=(20, 15))
# plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
# plt.show()


# 트리 모델은 스케일링을 할 필요가 없다!!
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_input, train_target)

print('\n===== 노 스케일링 깊이(3) 스코어 =====\n')
print('훈련 스코어:', dt.score(train_input, train_target))
print('테스트 스코어:', dt.score(test_input, test_target))

# 특성별로 중요도를 뽑아보기 (합해서 1)
# 불순도 감소에 누가 가장 많이 기여했는가?
print('\n======= 특성별 중요도 =======\n')
print(dt.feature_importances_)

# 정보이득이 0.0005 보다 적으면 더이상 분할 하지 마라.
# 디폴트값 = 0
dt = DecisionTreeClassifier(min_impurity_decrease=0.0005, random_state=42)
dt.fit(train_input, train_target)

''' 디폴트 값은 사실상 제약이 없음. (과적합 머신)
DecisionTreeClassifier(
    max_depth=None,             # 무제한
    min_impurity_decrease=0.0,  # 아주 미세한 개선도 허용
    min_samples_spplit=2,       # 샘플 2개만 있어도 분할 시도
    min_samples_leaf=1)         # 리프에 1개 샘플 허용

'''

print('\n===== min_impurity_decrease=0.0005 스코어 =====\n')
print('훈련 스코어:', dt.score(train_input, train_target))
print('테스트 스코어:', dt.score(test_input, test_target))

# plt.figure(figsize=(20,15))
# plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
# plt.show()


# ======================= 다중 분류 =======================

fish = pd.read_csv('./data/fish_data.csv')
print(fish.head())
print()

# 물고기 종류 확인(7개)
print(pd.unique(fish['Species']))
print()

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

# 모델 훈련
dt = DecisionTreeClassifier(max_depth=50, random_state=42)
dt.fit(train_input, train_target)

# 모델평가 (score)
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

# 트리 그래프
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['Weight', 'Length', 'Diagonal', 'Height', 'Width'])
plt.show()