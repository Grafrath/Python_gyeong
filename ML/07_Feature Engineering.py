import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

np.set_printoptions(linewidth=500, precision=3)
# linewidth => 한줄 최대 문자수(ex. 한줄 최대 500자)
# precision => 소수점 자리수

perch_full = pd.read_csv('./ML/perch_data.csv')
print(perch_full.head())
perch_full.info()
print()

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight, random_state=42 )

print('\n================ 특성 엔지니어링 진행 ================\n')
# PolynomialFeatures 설정 (include_bias=False로 절편용 1 제외)
poly = PolynomialFeatures(degree=2, include_bias=False)

# 훈련 세트를 기준으로 특성 변환 규칙 학습 및 변환
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print(f'변환 전 특성 개수: {train_input.shape }')
print(f'변환 후 특성 개수: {train_poly.shape}')
print(f'생성된 특성 조합: {poly.get_feature_names_out()}')
print()