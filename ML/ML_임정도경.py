import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import random
import locale

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
import lightgbm as lgb

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)

# 랜덤 시드 설정
np.random.seed(1234)
random.seed(1234)

# 데이터 로드
train_df = pd.read_csv('./data/titanic/train.csv')
test_df = pd.read_csv('./data/titanic/test.csv')

print('\n======================== 데이터 개요 파악 ========================\n')
print('훈련 세트:', train_df.shape)
print('테스트 세트:', test_df.shape)
print()

print('\n[훈련 세트 요약정보]\n')
train_df.info()

print('\n[테스트 세트 요약정보]\n')
test_df.info()

# 결측치 확인
print('\n[훈련 세트 결측치]\n', train_df.isnull().sum())
print('\n[테스트 세트 결측치]\n', test_df.isnull().sum())
print()

'''
학습목표
    - 수업시간에 배운 머신러닝 모델 3가지를 학습 시킨 뒤, 성능을 비교/평가할것.
    - 사용모델 - 선형계열모델1, 트리계열모델1, SVC
    - 성능 비교 기준은 Accuracy, F1-Score

전처리를 왜, 어떻게 하였는지
모델 성능 개선을 위해 어떤 시도를 하였는지 등등
데이터 분석 + 모델 학습 전반에 있어서 설명이나 의견이 있으면 자유롭게 기술
'''

print('\n======================== 데이터 전처리 ========================\n')

# ======== 결측치 처리 ========
# 요금 기준으로 승선항 찾기
missing_embarked = train_df[train_df['Embarked'].isnull()]

# if not missing_embarked.empty:
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x='Embarked', y='Fare', hue='Pclass', data=train_df)
#     plt.axhline(missing_embarked['Fare'].iloc[0], color='red', linestyle='--',
#                 label='Missing Fare Value')
#     plt.title('요금 분포 확인')
#     plt.legend()
#     plt.show()

train_df['Embarked'] = train_df['Embarked'].fillna('C')
all_df = pd.concat([train_df, test_df], sort=False).reset_index(drop=True)

print('\n======== 통합데이터 결측치 ========\n')
print(all_df.isnull().sum())
print()

print('\n======== 호칭 분리 ========\n')
name_df = all_df['Name'].str.split('[,.]', n=2, expand=True).apply(lambda x: x.str.strip())
name_df.columns = ['family_name', 'honorific', 'name']
print(name_df.head())
print()

print(name_df['honorific'].value_counts())

print('\n======== 호칭 부여 ========\n')
all_df = pd.concat([all_df, name_df['honorific']], axis=1)
print(all_df.head())
print()

# 연령 결측치를 호칭별 쳥균 연령으로 보완하기.
all_df['Age'] = all_df['Age'].fillna(
    all_df.groupby('honorific')['Age'].transform('median')
)

bins = [0, 12, 18, 35, 60, 100]
labels = [0, 1, 2, 3, 4] # Child, Teenager, Young Adult, Adult, Senior
all_df['AgeBin'] = pd.cut(all_df['Age'], bins=bins, labels=labels)

rare = ['Dona', 'Lady', 'Countess','Capt', 'Col','Don', 'Dr',
                'Major', 'Rev', 'Sir', 'Jonkheer']
all_df['honorific'] = all_df['honorific'].replace(rare, 'Rare')
all_df['honorific'] = all_df['honorific'].replace(['Mlle', 'Ms'], 'Miss')
all_df['honorific'] = all_df['honorific'].replace('Mme', 'Mrs')

# 요금 결측치 처리
all_df['Fare'] = all_df['Fare'].fillna(all_df.groupby('Pclass')['Fare'].transform('median'))
all_df['Fare'] = np.log1p(all_df['Fare'])

# Cabin 활용
all_df['Deck'] = all_df['Cabin'].str[0]
all_df['Deck'] = all_df['Deck'].fillna('U')

print("\n======== 데크별 데이터 개수 ========\n")
print(all_df['Deck'].value_counts())
print()

all_df['Deck'] = all_df['Deck'].replace('T', 'U')

# 가족 수 피처 생성
all_df['FamilySize'] = all_df['SibSp'] + all_df['Parch'] + 1
all_df['IsAlone'] = (all_df['FamilySize'] == 1).astype(int)

def get_family_group(size):
    if size == 1:
        return 'Alone'
    elif size <= 4:
        return 'Small'
    else:
        return 'Large'

all_df['FamilyGroup'] = all_df['FamilySize'].apply(get_family_group)

# 불필요한 컬럼 삭제
drop_cols = ['Name', 'Ticket', 'Cabin', 'FamilySize', 'IsAlone']
all_df = all_df.drop(columns=drop_cols, axis=1)

# 모델별 데이터 변환
categories = ['Sex', 'Embarked', 'honorific', 'Deck', 'AgeBin', 'FamilyGroup']

all_df_tree = all_df.copy()
for cat in categories:
    le = LabelEncoder()
    all_df_tree[cat] = le.fit_transform(all_df_tree[cat].astype(str))
    all_df_tree[cat] = all_df_tree[cat].astype('category')

all_df_linear = pd.get_dummies(all_df, columns=categories, drop_first=True)

print("\n======== 인코딩 완료 후 데이터 헤드 ========\n")
print(all_df.head())
all_df.info()
print()

print('\n======== 결측치 최종확인 ========\n')
print(all_df.isnull().sum())
print()

print('\n======================== 데이터 분리 ========================\n')
# 트리 모델용 데이터
features_tree = ['Pclass', 'Sex', 'Age', 'AgeBin', 'SibSp', 'Parch', 'Fare', 
                 'Embarked', 'honorific', 'Deck', 'FamilyGroup']
X_tree = all_df_tree.iloc[:len(train_df)][features_tree]
y_tree = all_df_tree.iloc[:len(train_df)]['Survived'].astype(int)
X_test_final_tree = all_df_tree.iloc[len(train_df):][features_tree] # 최종 테스트 데이터

# 트리 모델 검증용 분리
X_train_t, X_val_t, y_train_t, y_val_t = train_test_split(
    X_tree, y_tree, test_size=0.2, random_state=1234, stratify=y_tree
)

# 선형 모델용 데이터
features_linear = [col for col in all_df_linear.columns if col not in ['Survived', 'PassengerId']]
X_linear = all_df_linear.iloc[:len(train_df)][features_linear]
y_linear = all_df_linear.iloc[:len(train_df)]['Survived'].astype(int)
X_test_linear_raw = all_df_linear.iloc[len(train_df):][features_linear] # 최종 테스트 데이터(Raw)

# 스케일링 적용
scaler = StandardScaler()
X_linear_scaled = scaler.fit_transform(X_linear)
X_test_final_linear = scaler.transform(X_test_linear_raw) # 최종 테스트 데이터(Scaled)

# 선형 모델 검증용 분리
X_train_l, X_val_l, y_train_l, y_val_l = train_test_split(
    X_linear_scaled, y_linear, test_size=0.2, random_state=1234, stratify=y_linear
)

X_train_l_df = pd.DataFrame(X_train_l, columns=features_linear)
X_val_l_df = pd.DataFrame(X_val_l, columns=features_linear)

print("데이터 분리 및 스케일링 완료")

print('\n======================== 모델 준비 ========================\n')
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1234)

lg = LogisticRegression(
    C=1.0,
    solver='liblinear',
    max_iter=1000,
    random_state=1234
)

lgbm = lgb.LGBMClassifier(
    objective='binary',
    metric='binary_logloss',

    n_estimators=300,
    learning_rate=0.02,

    num_leaves=24,
    max_depth=-1,
    min_child_samples=30,
    min_child_weight=1e-3,

    min_split_gain=0.0,
    reg_alpha=0.0,
    reg_lambda=1.0, 

    subsample=0.8,
    subsample_freq=1,
    colsample_bytree=0.8,

    random_state=1234,
    n_jobs=-1,
    verbosity=-1
)

svc = SVC(
    C=1.0,
    kernel='rbf',
    gamma='scale',
    probability=True,
    random_state=1234
)

print("모델준비 완료")
print()

print("\n======================== 모델 학습) ========================\n")
# LightGBM 학습 및 검증
cv_acc_lgbm = cross_val_score(lgbm, X_tree, y_tree, cv=skf, scoring='accuracy').mean()
cv_f1_lgbm = cross_val_score(lgbm, X_tree, y_tree, cv=skf, scoring='f1').mean()

# Logistic Regression 학습 및 검증
cv_acc_lg = cross_val_score(lg, X_linear_scaled, y_linear, cv=skf, scoring='accuracy').mean()
cv_f1_lg = cross_val_score(lg, X_linear_scaled, y_linear, cv=skf, scoring='f1').mean()

# SVC 학습 및 검증
cv_acc_svc = cross_val_score(svc, X_linear_scaled, y_linear, cv=skf, scoring='accuracy').mean()
cv_f1_svc = cross_val_score(svc, X_linear_scaled, y_linear, cv=skf, scoring='f1').mean()

lgbm.fit(
    X_train_t, y_train_t,
    eval_set=[(X_val_t, y_val_t)],
    eval_metric='binary_logloss',
    callbacks=[
        lgb.early_stopping(stopping_rounds=50),
        lgb.log_evaluation(period=0)
    ]
)

lg.fit(X_train_l_df, y_train_l)
svc.fit(X_train_l_df, y_train_l)

print("학습 완료")
print()

print("\n======================== 모델 성능 평가 ========================\n")
# 성능 기록용 리스트
model_names = []
acc_scores = []
f1_scores = []

# 성능 평가 루프
eval_list = [
    ('Logistic Regression', lg, X_val_l_df, y_val_l),
    ('SVC', svc, X_val_l_df, y_val_l),
    ('LightGBM', lgbm, X_val_t, y_val_t)
]

print(f"{'Model':<20} | {'Accuracy':<10} | {'F1-Score':<10}")
print("-" * 50)

for name, model, x_v, y_v in eval_list:
    pred = model.predict(x_v)
    acc = accuracy_score(y_v, pred)
    f1 = f1_score(y_v, pred)
    
    model_names.append(name)
    acc_scores.append(acc)
    f1_scores.append(f1)
    print(f"{name:<20} | {acc:.4f}     | {f1:.4f}")
print()

X_train_l_df = pd.DataFrame(X_train_l, columns=features_linear)
X_val_l_df = pd.DataFrame(X_val_l, columns=features_linear)
X_test_final_linear_df = pd.DataFrame(X_test_final_linear, columns=features_linear)

weights = [1, 1, 2]

# 보팅 앙상블 모델 정의
voting_model = VotingClassifier(
    estimators=[
        ('lr', lg),
        ('svc', svc),
        ('lgbm', lgbm)
    ],
    voting='soft',
    weights=weights
)

# 앙상블 모델 학습
voting_model.fit(X_train_l_df, y_train_l)

# 앙상블 모델 성능 평가 (Hold-out)
voting_pred = voting_model.predict(X_val_l_df)
v_acc = accuracy_score(y_val_l, voting_pred)
v_f1 = f1_score(y_val_l, voting_pred)

print(f"Voting Ensemble Accuracy: {v_acc:.4f}")
print(f"Voting Ensemble F1-Score: {v_f1:.4f}")

# 성능 결과 업데이트
model_names.append('Voting Ensemble')
acc_scores.append(v_acc)
f1_scores.append(v_f1)

print("\n======================== 시각화 ========================\n")
performance_df = pd.DataFrame({
    'Model': model_names,
    'Accuracy': acc_scores,
    'F1-Score': f1_scores
})

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.barplot(x='Model', y='Accuracy', data=performance_df, hue='Model', palette='viridis', legend=False)
plt.title('Model Accuracy Comparison')
plt.ylim(0.7, 0.9)

plt.subplot(1, 2, 2)
sns.barplot(x='Model', y='F1-Score', data=performance_df, hue='Model', palette='magma', legend=False)
plt.title('Model F1-Score Comparison')
plt.ylim(0.7, 0.9)
plt.tight_layout()
plt.show()

print("\n======================== 최종 제출 파일 생성 ========================\n")
final_submission_list = [
    ('Logistic_Regression', lg, X_test_final_linear_df),
    ('SVC', svc, X_test_final_linear_df),
    ('LightGBM', lgbm, X_test_final_tree), # 트리 모델은 전용 트리 데이터 사용
    ('Voting_Ensemble', voting_model, X_test_final_linear_df)
]

for name, model, target_test_data in final_submission_list:
    # 최종 예측 수행
    final_preds = model.predict(target_test_data)
    
    # 제출 양식 생성
    submission = pd.DataFrame({
        "PassengerId": test_df["PassengerId"],
        "Survived": final_preds
    })
    
    # 파일 저장
    file_name = f'submission_{name.lower()}.csv'
    submission.to_csv(file_name, index=False)
    print(f"ㄴ {name:20} -> {file_name} 저장 완료")

print("\n[프로젝트 종료] 모든 결과 파일이 생성되었습니다.")

'''
사용 모델은 Logistic Regression, Gradient Boosting, Svc 이며,
전처리 과정에 최대한 많은 공을 들였습니다.

항구는 요금을 기준으로 비교해서 대입하였고,
나이는 호칭을 이용했으며,
요금 결측치는 등급별 평균을 대입하였습니다.

기존에는 버리던 호실 정보를 이용하였습니다.
또한 SibSp와 Parch를 이용해 혼자 이용하였는지 여부도 체크하였습니다.

모델 학습과정에서는 트리 모델에는 Category 타입을,
선형 모델에는 원-핫 인코딩과 스케일링을 적용하였고,
각각의 데이터 셋을 분리하여 준비하였습니다.

======================== 모델 성능 평가 ========================       

Model                | Accuracy   | F1-Score
--------------------------------------------------
Logistic Regression  | 0.8212     | 0.7612
SVC                  | 0.8101     | 0.7500
LightGBM             | 0.8380     | 0.7717

Voting Ensemble Accuracy: 0.8436
Voting Ensemble F1-Score: 0.7846

======================== 모델 성능 평가 ========================       

Model                | Accuracy   | F1-Score
--------------------------------------------------
Logistic Regression  | 0.8212     | 0.7612
SVC                  | 0.8101     | 0.7536
LightGBM             | 0.8324     | 0.7581

Voting Ensemble Accuracy: 0.8492
Voting Ensemble F1-Score: 0.7970

======================== 모델 성능 평가 ========================       

Model                | Accuracy   | F1-Score
--------------------------------------------------
Logistic Regression  | 0.8324     | 0.7761
SVC                  | 0.8045     | 0.7407
LightGBM             | 0.7989     | 0.7049

Voting Ensemble Accuracy: 0.8212
Voting Ensemble F1-Score: 0.7647


'''