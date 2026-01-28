import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

import lightgbm as lgb
from lightgbm import LGBMClassifier

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
    data, target, test_size=0.2, random_state=42, stratify=target)

sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42, stratify=train_target)

lgbm = LGBMClassifier(random_state=42,
                      # 기본 성능/과적합 관련
                    n_estimators=2000,
                    learning_rate=0.05,

                    # 핵심 복잡도 파라미터
                    max_depth=-1,   # 깊이 제한 없음
                    num_leaves=31,  # 최대 리프 숫자

                    # 분할/노드제어
                    min_child_samples= 20,  # 최소 샘플 수
                    min_child_weight=1e-3, # 분할 후 노드에 필요한 최소 정보량

                    # 규제(정규화)
                    reg_lambda=0.0, # L2 높을 수록 leaf weight가 커지는걸 억제, 트리가 완만해짐
                    reg_alpha=0.0,   # L1 높을 수록 leaf weight가 0으로 수렴

                    # 랜덤성 관련
                    subsample=0.8,
                    colsample_bytree=0.8,

                    # 목적 함수 설정 (이진 분류)
                    objective='binary',
                    n_jobs=-1,)

# 3. 학습
lgbm.fit(
    sub_input, sub_target,
    eval_set=[(val_input, val_target)], 
    eval_metric='binary_logloss',
    callbacks=[
        lgb.early_stopping(stopping_rounds=50), 
        lgb.log_evaluation(period=100)          
    ]
)

print('\n================ 학습 스코어 점수 ================\n')
print('\n 트레인 스코어 ', lgbm.score(sub_input, sub_target))
print('\n 테스트 스코어 ', lgbm.score(val_input, val_target))
print()


# 4. 평가
proba = lgbm.predict_proba(test_input)[:, 1] 
pred = (proba >= 0.5).astype(int)

thresholds = np.arange(0.1, 1.0, 0.1)
results = []

# 2. 각 임계점별 지표 계산
# proba는 이미 위에서 lgbm.predict_proba(test_input)[:, 1]로 구한 값을 사용합니다.
for threshold in thresholds:
    # 임계점 적용
    temp_pred = (proba >= threshold).astype(int)
    
    # 혼동 행렬 추출 (TN, FP, FN, TP)
    tn, fp, fn, tp = confusion_matrix(test_target, temp_pred).ravel()
    
    # 지표 계산
    acc = accuracy_score(test_target, temp_pred)
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0  # 재현율 (TPR)
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0    # 위양성률
    
    results.append({
        'Threshold': round(threshold, 1),
        'Accuracy': round(acc, 4),
        'Recall (TPR)': round(recall, 4),
        'FPR': round(fpr, 4)
    })

# 3. 결과 출력 (표 형태)
df_results = pd.DataFrame(results)
print("\n[임계점 변화에 따른 지표 분석]")
print(df_results.to_string(index=False))

# 시각화 (선택 사항: 지표 변화 흐름 확인)
plt.figure(figsize=(8, 5))
plt.plot(df_results['Threshold'], df_results['Recall (TPR)'], label='Recall (TPR)', marker='o')
plt.plot(df_results['Threshold'], df_results['FPR'], label='FPR', marker='s')
plt.plot(df_results['Threshold'], df_results['Accuracy'], label='Accuracy', linestyle='--')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Trade-off: Recall vs FPR by Threshold')
plt.legend()
plt.grid(True)
plt.show()