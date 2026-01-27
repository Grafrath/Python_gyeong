import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)

print('\n================ 데이터 정보 ================\n')
print(f'전체 샘플 수: {X.shape[0]}')
print(f'특성 수: {X.shape[1]}')
print()

train_input, test_input, train_target, test_target = train_test_split(
    X, y, test_size=0.2, random_state=42
)

ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

print('\n================ 모델 훈련 (SVR) ================\n')
svr = SVR(kernel='rbf', C=100, epsilon=0.1)
svr.fit(train_scaled, train_target)

print('\n================ 테스트셋 예측 ================\n')
y_pred = svr.predict(test_scaled)

mae = mean_absolute_error(test_target, y_pred)
mse = mean_squared_error(test_target, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(test_target, y_pred)

print('\n================ 성능 지표 요약 ================\n')
print(f'MAE (평균 절대 오차)   : {mae:.4f}')
print(f'MSE (평균 제곱 오차)   : {mse:.4f}')
print(f'RMSE (제곱근 MSE)     : {rmse:.4f}')
print(f'R2 Score (결정계수)   : {r2:.4f}')
print()

print('\n================ 시각화 데이터 생성 ================\n')
line_x = np.linspace(train_scaled.min(), train_scaled.max(), 100).reshape(-1, 1)
line_y = svr.predict(line_x)

plt.scatter(train_scaled, train_target, color='gray', alpha=0.5, label='Train Data')
plt.scatter(test_scaled, test_target, color='red', label='Test Data')
plt.plot(line_x, line_y, color='blue', linewidth=2, label='SVR Regression Line')

plt.title(f"SVR Regression (R2: {r2:.2f})")
plt.xlabel("Feature (Scaled)")
plt.ylabel("Target Value")
plt.legend()
plt.show()