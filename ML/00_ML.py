'''

======================== Dataset Check ========================
<내장 데이터셋 확인 (scikit-learn)>
- .data : 입력 데이터 (특성)
- .target : 정답 데이터 (라벨/수치)
- .feature_names : 특성(컬럼) 이름 확인 (예: age, bmi, bp 등)
- .DESCR : 데이터셋에 대한 전체 설명

======================== models ========================

<KNN> K - 최근접 이웃 모델
- KNeighborsClassifier - 분류 : 가장 가까운 이웃들을 조사하여 클래스 판단
- KNeighborsRegressor - 예측 : 가장 가까운 이웃들을 조사하여 평균으로 예측

<LinearRegression> 선형 회귀
- LinearRegression - 예측 : 'y = ax + b'
    일반식 (y = a1x1 + a2x2 ... + anxn + b)
    데이터를 가장 잘 대표하는 회귀선을 찾는다.
    즉, a b(파라미터)를 찾는 것.
    x = 특성 값, y = 에측 값
    손실함수 MSE 를 최소화 하는 a b를 찾는다

<Ridge, Lasso> 릿지, 라쏘회귀
- Ridge - 예측 : 파라미터들을 규제하여 안정적인 모델학습 가능
    선형 회귀 손실함수(MSE)에 정규항 L2를 추가

- Lasso - 예측 : 파라미터들을 규제하여 안정적인 모델학습 가능
    선형 회귀 손실함수(MSE)에 정규항 L1를 추가
    필요없는 특성의 파라미터는 0으로 만들어 버림

<Logistic Regression> 로지스틱 리그레이션 : 이름은 회귀지만 이진 분류에 주로 사용.
    - 선형회귀의 선형방정식 결과를 시그모이드 함수에 통과시켜 0 or 1로 분류 문제 수행
    - 선형회귀의 선형방정식 결과 = z
        다중분류(ovr) - 이진분류를 여러개 독립적으로 수행
        다중분류(softmax) - 소프트맥스를 활용하여 한번에 수행

<점진적 학습> partial_fit
- 데이터를 한꺼번에 모두 준비하기 어려운 경우, 일부분씩 나누어 학습 가능
- 기존에 학습한 모델의 파라미터를 유지하며 업데이트함

<SGDClassifier> 확률적 경사 하강법 분류기
- 대용량 데이터 처리에 최적화된 점진적 학습 모델
- loss='log_loss': 로지스틱 회귀 모델로 동작
- loss='hinge': 서포트 벡터 머신(SVM) 모델로 동작
- 특징: 훈련 세트에서 샘플을 하나씩 꺼내어 경사 하강법을 수행함
- 주의: 반드시 스케일링(StandardScaler)된 데이터를 사용해야 함

<SGDRegressor> 확률적 경사 하강법 회귀 계열
- 대용량 데이터에서 연속적인 수치(예: 당뇨 수치)를 예측할 때 사용
- loss='squared_error': 일반적인 선형 회귀 손실 함수 사용
- 특징: Classifier와 마찬가지로 점진적 학습(partial_fit)이 가능함
- 주의: 특성 간 스케일 차이에 매우 민감하므로 반드시 스케일링 후 학습

======================== 머신러닝 ========================
- 데이터 준비
- 모델 준비
- 모델 학습
- 모델 평가
- (그래프)

'''

'''

<스케일링>
필요한 경우 데이터를 스케일링 해주어야한다.
    - StandardScaler : 평균을 0, 표준편차 1 로 변환
    - MinMaxScaler : 최소값 0, 최대값 1 범위로 변환
    - RobustScaler : 중앙값과 IQR 사용해서 스케일링

<특성공학>
    - PolynomialFeatures : 특성을 인위적으로 늘리는 작업
    - Log Transformation : 데이터에 로그를 취하여 값의 범위를 압축
    - One-Hot Encoding : 범주형(문자) 데이터를 0과 1로 이루어진 여러 개의 특성으로 변환

<옵션탐색>
각 모델마다 최적의 옵션을 탐색하여 모델의 최고 성능을 뽑아내는 작업

'''

'''
======================== ETC ========================
<데이터 분할> train_test_split
    데이터 준비 과정에서 데이터를 훈련세트와 테스트 세트로 나누는 것

<평가 지표> Evaluation
- 분류(Classification): accuracy_score, f1_score, confusion_matrix
- 회귀(Regression): mean_squared_error(MSE), r2_score

<하이퍼파라미터 튜닝> Tuning
- GridSearchCV : 모든 조합을 다 시도하여 최적의 옵션 탐색
- RandomizedSearchCV : 랜덤하게 조합을 시도하여 빠르게 최적 옵션 탐색
  
'''

'''

<Decision Tree> 의사결정 나무
- DecisionTreeClassifier / Regressor
    - 데이터를 특정 기준에 따라 가지치기하며 분류/예측
    - 스케일링의 영향이 적고 시각화가 쉬움

<Random Forest> 랜덤 포레스트
- RandomForestClassifier / Regressor
    - 여러 개의 결정 나무를 만들어 다수결 또는 평균으로 결정
    - 과적합(Overfitting) 방지에 효과적

<Boosting> 부스팅 (XGBoost, LightGBM)
- 점진적으로 오차를 줄여나가는 강력한 모델
- 파라미터 튜닝이 중요하며 성능이 매우 뛰어남

<Cross Validation> 교차 검증 (예: K-Fold)
- 데이터를 여러 조각으로 나누어 학습과 검증을 반복
- 특정 데이터셋에만 잘 작동하는 '운'을 배제함

'''

# import pandas as pd
# import numpy as np
# import sklearn
# import scipy

# print("pandas version:", pd.__version__)
# print("numpy version:", np.__version__)
# print("scikit-learn version:", sklearn.__version__)
# print("scipy version:", scipy.__version__)

# pip install --upgrade pandas
# import pandas
# import numpy
# import scikit-learn
# import scipy

# pandas version: 2.3.3
# numpy version: 2.4.1
# scikit-learn version: 1.8.0
# scipy version: 1.17.0