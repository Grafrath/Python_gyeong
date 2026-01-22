import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy.special import expit
from scipy.special import softmax

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, \
roc_auc_score, recall_score, confusion_matrix, classification_report, RocCurveDisplay
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data=load_breast_cancer()
x = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

y = 1 - y

print('\n================ 데이터 정보 ================\n')
print(f'전체 샘플 수: {x.shape[0]}')
print(f'특성 수: {x.shape[1]}')
print(f'클래스 종류: {data.target_names}')
print()

train_input, test_input, train_target, test_target = train_test_split(
    x, y, stratify=y, random_state=42
)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

lr = LogisticRegression(max_iter=1000)
lr.fit(train_scaled, train_target)

print('\n================ 로지스틱 회귀 결과 ================\n')
print('트레인 스코어: ', lr.score(train_scaled, train_target))
print('테스트 스코어: ', lr.score(test_scaled, test_target))
print('\n클래스 순서(0:양성, 1:악성):', lr.classes_) 

# 예측 및 확률
y_pred = lr.predict(test_scaled)
proba = lr.predict_proba(test_scaled)

print(y_pred)
print(np.round(proba, decimals=4))
print()

# 지표계산
acc = accuracy_score(test_target, y_pred)
pre = precision_score(test_target, y_pred)
rec = recall_score(test_target, y_pred)
f1 = f1_score(test_target, y_pred)
auc = roc_auc_score(test_target, proba[:, 1])

print('\n================ 성능 지표 요약 ================\n')
print(f'정확도 (Accuracy)  : {acc:.4f}')
print(f'정밀도 (Precision) : {pre:.4f}')
print(f'재현율 (Recall)    : {rec:.4f}')
print(f'F1 스코어 (F1)     : {f1:.4f}')
print(f'AUC 스코어 (AUC)   : {auc:.4f}')

print('\n================ 분류 상세 리포트 (Classification Report) ================\n')
report = classification_report(test_target, y_pred, target_names=['Benign', 'Malignant'])
print(report)

print('\n================ 오차 행렬 (Confusion Matrix) ================\n')
cm = confusion_matrix(test_target, y_pred)
print(cm)
print(f"\n※ 실제 암(1)을 정상(0)으로 오진한 사례: {cm[1, 0]}건")

# ROC Curve 시각화
print('\n================ 시각화 데이터 생성 ================\n')
RocCurveDisplay.from_estimator(lr, test_scaled, test_target)
plt.title("ROC Curve - Breast Cancer Detection")
plt.show()