import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, RocCurveDisplay

from xgboost import XGBClassifier

# 1. 데이터 준비
# train/test 분리
# early stopping을 위한 valid 셋 분리

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

sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

# 2. 모델& 옵션 설정
xgb = XGBClassifier(n_estimators=2000, learning_rate=0.05, max_depth=4, random_state=42,
                    min_child_weight=1, # 분할 후 노드에 필요한 최소 정보량
                    gamma=0.0,  #분할 최소 이득(규제)
                    subsample=0.8,  # row 샘플링( 트리 하나 만들때마다 매번 다른 80% 샘플을 뽑아 사 용)
                    colsample_bytree=0.8,   #  feature 샘플링(트리 하나 만들때, 전체 특성중 80%만 사용)

                    # 규제(정규화)
                    reg_lambda=1.0, # L2 높을 수록 leaf weight가 커지는걸 억제
                    reg_alpha=0.0,   # L1 높을 수록 leaf weight가 0으로 수렴

                    # 학습속도 알고리즘 선택
                    tree_method='hist',
                    early_stopping_rounds=50,
                    n_jobs=-1,

                    # 목적 함수 설정 (이진 분류)
                    objective='binary:logistic',
                    eval_metric='logloss')

# 3. 학습
xgb.fit(
    sub_input, sub_target,
    eval_set=[(sub_input, sub_target), (val_input, val_target)], # 훈련/검증 손실을 동시에 확인
    verbose=100 
)

# 4. 평가
print(f"\n최적 반복 횟수: {xgb.best_iteration}")

# [수정] test_input 전체를 넣어야 하며, [:, 1]로 '1'이 될 확률만 추출합니다.
proba = xgb.predict_proba(test_input)[:, 1] 
pred = (proba >= 0.5).astype(int)

acc = accuracy_score(test_target, pred)
auc = roc_auc_score(test_target, proba)

print(f"정확도(Accuracy): {acc:.4f}")
print(f"ROC-AUC: {auc:.4f}")
print("\n[분류 보고서]")
print(classification_report(test_target, pred))

# 특성 중요도 확인
print('\n================ 특성 중요도 ================')
# 특성 이름과 매칭해서 보기 좋게 출력
fi = pd.Series(xgb.feature_importances_, index=data.columns)
print(fi.sort_values(ascending=False))

# 5. roc 커브 그리기

RocCurveDisplay.from_predictions(test_target, proba)
plt.title('XGBoost ROC curve ')
plt.show()