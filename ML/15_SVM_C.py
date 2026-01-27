import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = make_classification(n_samples=400, n_classes=2,
                           n_features=2, n_redundant=0, random_state=42)

# n_samples 총 샘플수
# n_classes 클래스 수
# n_features 특성 수
# n_redundant 불필요한 특성 수

train_input, test_input, train_target, test_target = train_test_split(
    X, y, stratify=y, random_state=42)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

def plot_decision_boundary(model, X_sc, y, title):
    # 격자 생성
    xx, yy = np.meshgrid(np.linspace(X_sc[:, 0].min()-1, X_sc[:, 0].max()+1, 100),
                         np.linspace(X_sc[:, 1].min()-1, X_sc[:, 1].max()+1, 100))
    
    # 예측값 계산
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    
    # 결정 경계 그리기
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
    # 실제 데이터 산점도
    plt.scatter(X_sc[:, 0], X_sc[:, 1], c=y, edgecolors='k', cmap='RdYlBu', s=20)
    
    plt.title(title)
    plt.xlabel('Feature 1 (Scaled)')
    plt.ylabel('Feature 2 (Scaled)')
    plt.show()

model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
model.fit(train_scaled, train_target)

model_linear = SVC(kernel='linear', C=1.0, random_state=42)
model_linear.fit(train_scaled, train_target)
plot_decision_boundary(model_linear, train_scaled, train_target, "SVM: Linear Kernel")

model_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
model_rbf.fit(train_scaled, train_target)
plot_decision_boundary(model_rbf, train_scaled, train_target, "SVM: RBF Kernel")

y_pred = model.predict(test_scaled)

print(f"정확도: {accuracy_score(test_target, y_pred):.4f}")
print("\n[오차 행렬]\n", confusion_matrix(test_target, y_pred))
print("\n[상세 리포트]\n", classification_report(test_target, y_pred))

xx, yy = np.meshgrid(np.linspace(train_scaled[:, 0].min()-1, train_scaled[:, 0].max()+1, 100),
                     np.linspace(train_scaled[:, 1].min()-1, train_scaled[:, 1].max()+1, 100))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)