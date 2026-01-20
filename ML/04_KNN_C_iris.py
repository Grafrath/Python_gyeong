import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
kn = KNeighborsClassifier()

df = sns.load_dataset('iris')
print(df)
df.info()
print()

'''
sepal_length 꽃받침 길이
sepal_width " 너비
petal_length    꽃잎 길이
petal_width " 너비
'''

# length = df['sepal_length'] + df['petal_length']
# weight = df['sepal_width'] + df['petal_width']

# # zip 활용 (길이, 무게) 쌍 리스트 생성
# iris_data = [[l, w] for l, w in zip (length, weight)]
# iris_target = df['species'].values

# # 넘피 배열 변환
# input_arr = np.array(iris_data)
# target_arr = np.array(iris_target)

# # 데이터 분할
# train_input, test_input, train_target, test_target = train_test_split(
#     input_arr, target_arr, test_size=0.2, random_state=42, stratify=target_arr
# )

# print('\n================ 데이터 분할 완료 ================\n')
# print(train_input.shape)
# print(test_input.shape)

# kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))

sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.show()

x = df.drop('species', axis=1)
y = df['species']

train_input, test_input, train_target, test_target = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

kn.fit(train_input, train_target)
print(kn.score(test_input, test_target))

knn = KNeighborsClassifier(n_neighbors=3)
print('\n================ 모델 준비 완료 ================\n')

knn.fit(train_input, train_target)
print('\n================ 모델 학습 완료 ================\n')

# 테스트셋 예측
y_pred = knn.predict(test_input)

print('\n 예측값 ', y_pred)
print('\n 실제값 ', test_target)
print('\n 트레인 스코어 ', knn.score(train_input, train_target))
print('\n 테스트 스코어 ', knn.score(test_input, test_target))

print('정확도: ', accuracy_score(test_target, y_pred))

'''
score 메서드: 모델 객체가 직접 가지고 있는 기능으로,
데이터를 넣으면 내부적으로 예측과 평가를 한 번에 수행합니다.

accuracy_score 함수: Scikit-learn의 metrics 모듈에서 가져온 독립된 함수로,
'실제 정답'과 '모델의 예측값' 두 리스트를 비교하여 계산합니다.

주요 차이점 비교구분
구분    estimator.score()
소속	모델(Estimator) 객체의 메서드
필요 인자	(테스트 입력값, 실제 정답)
작동 방식	내부에서 predict()를 자동 실행 후 점수 계산
용도	간편하게 모델의 성능을 확인할 때

accuracy_score(y_true, y_pred)
sklearn.metrics 패키지의 함수
(실제 정답, 모델이 예측한 값)
이미 계산된 두 결과값의 일치율만 계산
상세한 분석이나 다양한 평가지표를 쓸 때

'''