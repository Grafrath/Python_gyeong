# 군집화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = np.load('./data/fruits_300.npy')

print('\n================ 과일 전체 배열 ================\n')
print(fruits[:1].shape) 
print()

# 사진 출력 - 흑백 사진이기 떄문에 cmap-'gray' 지해줘야 한다.
# 0~255 사이 숫자로 이루어짐, 255 일수록 하얀색
# 원래 바탕은 하얗고 사과는 어두운 사진
# (모델학습 등) 컴퓨터는 높은 숫자에 주목하기 때문에
# 우리는 흑백반전을 미리 준 데이터임


print('\n================ 과일 출력 ================\n')
# 사과
# plt.imshow(fruits[0], cmap='gray_r')
# plt.show()

# 파인애플 과 바나나
# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].imshow(fruits[100], cmap='gray_r')
# axs[1].imshow(fruits[200], cmap='gray_r')
# plt.show()

# 과일별로
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)

print('\n================ 데이터 확인 ================\n')
print(apple.shape)
print(pineapple.shape)
print(banana.shape)
print()

apple_mean = apple.mean(axis=0)
pineapple_mean = pineapple.mean(axis=0)
banana_mean = banana.mean(axis=0)

print('================ 평균값 수치 확인 ================')
print(f"사과 평균값 (앞의 5개): {apple_mean[:5]}")
print(f"파인애플 평균값 (앞의 5개): {pineapple_mean[:5]}")
print(f"바나나 평균값 (앞의 5개): {banana_mean[:5]}")
print()

# 3. 전체 평균의 분포 확인 (각 과일 그룹의 특징 수치)
print(f"사과 전체 픽셀 평균: {apple_mean.mean():.2f}")
print(f"파인애플 전체 픽셀 평균: {pineapple_mean.mean():.2f}")
print(f"바나나 전체 픽셀 평균: {banana_mean.mean():.2f}")


# plt.figure(figsize=(10, 6))
# plt.hist(apple.mean(axis=1), alpha=0.8, label='apple')
# plt.hist(pineapple.mean(axis=1), alpha=0.8, label='pineapple')
# plt.hist(banana.mean(axis=1), alpha=0.8, label='banana')
# plt.title('Fruit Mean Histogram')
# plt.xlabel('Pixel Mean Value')
# plt.ylabel('Frequency')
# plt.legend()
# plt.show()

apple_mean = apple.mean(axis=0).reshape(100, 100)
pineapple_mean = pineapple.mean(axis=0).reshape(100, 100)
banana_mean = banana.mean(axis=0).reshape(100, 100)

# fig, axs = plt.subplots(1, 3, figsize=(15, 5))
# axs[0].imshow(apple_mean, cmap='gray_r')
# axs[1].imshow(pineapple_mean, cmap='gray_r')
# axs[2].imshow(banana_mean, cmap='gray_r')
# plt.show()

abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis=(1,2))
print(abs_mean.shape)
print()

apple_index = np.argsort(abs_mean)[:100]
apple_index = apple_index.reshape(10, 10)

# fig, axs = plt.subplots(10, 10, figsize=(10, 10))
# for i in range(10):
#     for j in range(10):
#         axs[i, j].imshow(fruits[apple_index[i, j]], cmap='gray_r')
#         axs[i, j].axis('off')
# plt.show()

idx = np.arange(fruits.shape[0])
np.random.seed(42)
np.random.shuffle(idx)

fruits_shuffled = fruits[idx]

fig, axs = plt.subplots(10, 10, figsize=(10, 10))
for i in range(10):
    for j in range(10):
        target_idx = i * 10 + j
        axs[i, j].imshow(fruits_shuffled[target_idx], cmap='gray')
        axs[i, j].axis('off')
plt.show()

shuffled_mean = np.mean(fruits_shuffled, axis=(1, 2))
sorted_index = np.argsort(shuffled_mean)
sorted_mean_fruits = fruits_shuffled[sorted_index]

fig, axs = plt.subplots(10, 10, figsize=(10, 10))
for i in range(10):
    for j in range(10):
        target_idx = i * 10 + j
        axs[i, j].imshow(sorted_mean_fruits[target_idx], cmap='gray')
        axs[i, j].axis('off')
plt.show()

# 1. 100개씩 슬라이싱
group1 = sorted_mean_fruits[:100]
group2 = sorted_mean_fruits[100:200]
group3 = sorted_mean_fruits[200:]

# 2. 각 그룹의 평균 이미지 계산
group1_mean = np.mean(group1, axis=0)
group2_mean = np.mean(group2, axis=0)
group3_mean = np.mean(group3, axis=0)

# 3. 시각화하여 확인
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(group1_mean, cmap='gray')
axs[0].set_title("First 100 (Darkest)")
axs[1].imshow(group2_mean, cmap='gray')
axs[1].set_title("Middle 100")
axs[2].imshow(group3_mean, cmap='gray')
axs[2].set_title("Last 100 (Brightest)")
plt.show()