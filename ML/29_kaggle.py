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
# embarked_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# 승선 도시별 생존률 컬럼 추가
# embarked_df['survived_rate'] = embarked_df.iloc[:,1] / (embarked_df.iloc[:,0] + embarked_df.iloc[:,1])
# print(embarked_df)
# print()


# 성별 생존률
# sex_df = train_df[['Sex', 'Survived', 'PassengerId']].dropna().groupby(['Sex', 'Survived']).count().unstack()
# sex_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# 티켓별 생존률 (Pclass)
# ticket_df = train_df[['Pclass', 'Survived', 'PassengerId']].dropna().groupby(['Pclass', 'Survived']).count().unstack()
# ticket_df.plot(kind='bar', stacked=True)
# plt.xticks(rotation=0)
# plt.show()

# 연령별 생존률 히스토그램
# plt.hist(x=[train_df['Age'][train_df['Survived']==0], train_df['Age'][train_df['Survived']==1]],
#          bins=8,
#          histtype='barstacked',
#          label=['Death', 'Survived'])
# plt.legend()
# plt.show()

print('\n======================== 더미 생성 ========================\n')
# 카테고리 변수(컬럼)을 더미 변수로
train_df_corr = pd.get_dummies(
    train_df,
    columns=['Sex', 'Embarked'],
    drop_first=True,
    dtype=int
)

# 상관관계 개선
train_corr = train_df_corr.corr(numeric_only=True)

print('\n======== 상관관계 ========\n')
print(train_corr)
print()

# 히트맵 시각화
# plt.figure(figsize=(10, 8))
# sns.heatmap(train_corr, vmax=1, vmin=-1, center=0, annot=True)
# plt.title('Correlation Heatmap')
# plt.show()

# ========================= 데이터 전처리 =========================

# 학습 데이터와 테스트 데이터 통합
# sort=false 열 이름 순서 그대로 유지
all_df =  pd.concat([train_df, test_df], sort=False).reset_index(drop=True)

print('\n======== 통합데이터 ========\n')
print(all_df)
print()

print('\n======== 통합데이터 결측치 ========\n')
print(all_df.isnull().sum())
print()

# Pclass별 Fare 평균으로 결측치 채우기
all_df['Fare'] = all_df['Fare'].fillna(
    all_df.groupby('Pclass')['Fare'].transform('mean')
)

print('\n======== 통합데이터 결측치 ========\n')
print(all_df.isnull().sum())
print()

# ================ 나이 결측치 채우기 ================
name_df = all_df['Name'].str.split('[,.]', n=2, expand=True).apply(lambda x: x.str.strip())
name_df.columns = ['family_name', 'honorific', 'name']
print(name_df)
print()
 
print(name_df['honorific'].value_counts())

# 원본에 병합
all_df = pd.concat([all_df, name_df], axis=1)
print(all_df)
print()

# 호칭별 나이 통계 그래프
# plt.figure(figsize=(18, 5))
# sns.boxenplot(x='honorific', y='Age', data=all_df)
# plt.show()

# 호칭별 연령 평균값 확인
print(all_df[['Age', 'honorific']].groupby('honorific').mean())
print()

# 트레인 / 테스트셋에 따로 이름 데이터 결합
train_df = pd.concat([train_df, name_df[0:len(train_df)].reset_index(drop=True)], axis=1)
test_df = pd.concat([test_df, name_df[len(train_df):].reset_index(drop=True)], axis=1)

# 호칭별로 생존률 집계
honorific_df = train_df[['honorific', 'Survived', 'PassengerId']]\
.dropna().groupby(['honorific', 'Survived']).count().unstack()

# honorific_df.plot(kind='bar', stacked=True)
# plt.show()

# 연령 결측치를 호칭별 쳥균 연령으로 보완하기.
all_df['Age'] = all_df['Age'].fillna(
    all_df.groupby('honorific')['Age'].transform('mean')
)

print('\n======== 통합데이터 결측치 ========\n')
print(all_df.isnull().sum())
print()

# 가족 인원수 컬럼 추가
all_df['family_num'] = all_df['Parch'] + all_df['SibSp']
print(all_df['family_num'].value_counts())
print()

# 홀로 승선했는지 파악하는 컬럼 추가
all_df['alone'] = (all_df['family_num'] == 0).astype(int)
all_df['alone'] = all_df['alone'].fillna(0)

# 불필요한 컬럼 삭제
all_df = all_df.drop(['PassengerId', 'Name', 'family_name', 'name', 'Ticket', 'Cabin'], axis=1)
all_df.info()
print()

# 기타 호칭을 other 로 통합
# Series, where(조건, 대체값)
major_title = ['Mr', 'Miss', 'Mrs', 'Master']
all_df['honorific'] = all_df['honorific'].where(
    all_df['honorific'].isin(major_title),
    'other'
)

# Embarked 결측치 처리
all_df['Embarked'] = all_df['Embarked'].fillna('S')

print('\n======== 통합데이터 결측치 ========\n')
print(all_df.isnull().sum())
print()

# 자료형을 카테고리로 바꿀 컬럼 추출
categories = all_df.columns[all_df.dtypes=='object']
print(categories)
print()

# 레이블 인코딩
for cat in categories:
    le = LabelEncoder()
    all_df[cat] = le.fit_transform(all_df[cat])

print(all_df.head())
print()

print('\n========================= 모델 학습 준비 =========================\n')
train_df = all_df[all_df['Survived'].notnull()]
test_df = all_df[all_df['Survived'].isnull()].drop('Survived', axis=1)

# train_df = all_df['Survived'].notna()
# test_df = all_df['Survived'].isna()

# 학습용 특성(X)과 타겟(y) 분리
X_train = train_df.drop('Survived', axis=1)
y_train = train_df['Survived']

# X_train = all_df.loc[train_df].drop(columns=['Survived'])
# y_train = all_df.loc[train_df, 'Survived'].astype(int)

print('\n================ 데이터 사이즈 확인 ================\n')
print('트레인: ', X_train.shape)
print('타겟: ', y_train.shape)
print('테스트: ', test_df.shape)
print()

# 검증 데이터셋 분리 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(
    X_train, y_train, test_size=0.2, random_state=1234
)

#범주형으로 넣을 컬럼들
categories = ['Embarked', 'Pclass', 'Sex', 'honorific', 'alone']

# 컬럼들 자료형을 카테고리로
for c in categories:
    X_train[c] = X_train[c].astype('category')
    X_test[c] = X_test[c].astype('category')
    test_df[c] = test_df[c].astype('category')

# 모델 정의
lgbm = lgb.LGBMClassifier(
    objective='binary',             # 이진분류
    metric='binary_logloss',        # 손실평가

    n_estimators=3000,              # 얕은 트리
    learning_rate=0.03,             # 학습률

    num_leaves=31,                  # 최대 리프수
    max_depth=-1,                   # 트리깊이 제한x
    min_child_samples=30,           # 샘플 30개는 남아있음
    min_child_weight=1e-3,          # 최소 정보량

    min_split_gain=0.0,             # 이만큼 이상의 정보량 획득
    reg_alpha=0.0,                  # L1
    reg_lambda=0.5,                 # L2

    subsample=0.8,                  # 트리당 사용 샘플수
    colsample_bytree=0.8,           # 트리당 사용 컬럼수

    random_state=1234,
    n_jobs=-1,
    verbosity=1
)

lgbm.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    eval_metric='binary_logloss',
    categorical_feature=categories,
    callbacks=[
        lgb.early_stopping(stopping_rounds=20),
        lgb.log_evaluation(period=10)
    ]
)

importance_df = pd.DataFrame({
    'featuer': X_train.columns,
    'importance': lgbm.booster_.feature_importance(importance_type='split') # split, gain
}).sort_values(by='importance', ascending=False)

print(importance_df)
print()

print('\n========================= 모델 평가 및 최종 예측 =========================\n')
y_pred = lgbm.predict(X_test, num_iteration=lgbm.best_iteration_)
accuracy = accuracy_score(y_test, y_pred)
print(f'\n[검증 데이터 정확도]: {accuracy:.4f}')
print()


# 생존 확률 예측
final_preds = lgbm.predict(test_df)
preds_series = pd.Series(final_preds)
print(f"예측 생존율: {(preds_series.mean() * 100):.2f}%")
print()


submission['Survived'] = final_preds.astype(int)
submission.to_csv('./data/titanic/titanic_submit_01.csv', index=False)
print(submission['Survived'].value_counts())