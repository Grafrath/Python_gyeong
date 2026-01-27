import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import  RocCurveDisplay, mean_absolute_error, mean_squared_error 
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor

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

print('\n================ 인풋 데이터 스케일링 ================\n')
ss = StandardScaler()
train_scaled = ss.fit_transform(train_input)
test_scaled = ss.transform(test_input)

print('\n================ 모델 훈련 ================\n')
sg = SGDRegressor(max_iter=2000, loss="squared_error", penalty='l2',\
                   alpha=0.0001, tol=1e-3, random_state=42)
sg.fit(train_scaled, train_target)

print('\n================ 테스트셋 예측 ================\n')
print('트레인 스코어: ', sg.score(train_scaled, train_target))
print('테스트 스코어: ', sg.score(test_scaled, test_target))


y_pred = sg.predict(test_scaled)

mae = mean_absolute_error(test_target, y_pred)
mse = mean_squared_error(test_target, y_pred)
rmse = np.sqrt(mse)
r2 = sg.score(test_scaled, test_target) # sg.score는 Regressor에서 R^2를 반환함

print('\n================ 성능 지표 요약 ================\n')
print(f'MAE (평균 절대 오차)   : {mae:.4f}')
print(f'MSE (평균 제곱 오차)   : {mse:.4f}')
print(f'RMSE (제곱근 MSE)      : {rmse:.4f}')
print(f'R2 Score (결정계수)    : {r2:.4f}')

print('\n================ 시각화 데이터 생성 ================\n')
RocCurveDisplay.from_predictions(test_target, y_pred)
plt.title("ROC Curve - Breast Cancer Detection (SGDRegressor)")
plt.show()  