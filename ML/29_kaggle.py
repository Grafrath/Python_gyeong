import pandas as pd
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 200)

# 데이터 로드
train_df = pd.read_csv('./data/titanic/train.csv')
test_df = pd.read_csv('./data/titanic/test.csv')
submission = pd.read_csv('./data/titanic/gender_submission.csv')

# 랜덤 시드 설정
np.random.seed(1234)
random.seed(1234)


# ========================= 데이터 개요 파악 =========================

print('\n훈련 세트:', train_df.shape)   # (891, 12)
print('테스트 세트:', test_df.shape)    # (418, 11)

print('\n[훈련 세트]\n', train_df.head())
print('\n[테스트 세트]\n', test_df.head()) # Survived 컬럼 없음

print('\n[훈련 세트 자료형]\n', train_df.dtypes)

print('\n[훈련 세트 산술정보]\n', train_df.describe())
print('\n[테스트 세트 산술정보]\n', test_df.describe())

print('\n[훈련 세트 요약정보]\n')
train_df.info()

print('\n[테스트 세트 요약정보]\n')
test_df.info()

print('\n[성별 집계]\n', train_df['Sex'].value_counts()) # 남성이 두배정도
print('\n[승선도시별 집계]\n', train_df['Embarked'].value_counts()) # southampton 승선이 많음
print('\n[방번호별 집계]\n', train_df['Cabin'].value_counts())

# 결측치 확인
print('\n[훈련 세트 결측치]\n', train_df.isnull().sum())
print('\n[테스트 세트 결측치]\n', test_df.isnull().sum())


# ========================= 집계 및 시각화 =========================
print()
embarked_df = train_df[['Embarked', 'Survived', 'PassengerId']]
print(embarked_df)
print()

# 결측치 제거 => 그룹바이 => 카운트
embarked_df = embarked_df.dropna().groupby(['Embarked', 'Survived']).count()
print(embarked_df)
print()

# 승선 도시별 집계
embarked_df = embarked_df.unstack()
print(embarked_df)
print()

# 승선 도시별 생존 막대그래프
embarked_df.plot(kind='bar', stacked=True)
plt.xticks(rotation=0)
plt.show()

# 승선 도시별 생존률 컬럼 추가
embarked_df['survived_rate'] = embarked_df.iloc[:,1] / (embarked_df.iloc[:,0] + embarked_df.iloc[:,1])
print(embarked_df)
print()


# 성별 생존률
sex_df = train_df[['Sex', 'Survived', 'PassengerId']].dropna().groupby(['Sex', 'Survived']).count().unstack()
sex_df.plot(kind='bar', stacked=True)
plt.xticks(rotation=0)
plt.show()

# 티켓별 생존률 (Pclass)
ticket_df = train_df[['Pclass', 'Survived', 'PassengerId']].dropna().groupby(['Pclass', 'Survived']).count().unstack()
ticket_df.plot(kind='bar', stacked=True)
plt.xticks(rotation=0)
plt.show()

# 연령별 생존률 히스토그램
plt.hist(x=[train_df['Age'][train_df['Survived']==0], train_df['Age'][train_df['Survived']==1]],
         bins=8,
         histtype='barstacked',
         label=['Death', 'Survived'])
plt.legend()
plt.show()