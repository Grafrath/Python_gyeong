import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

fruits = np.load('./data/fruits_300.npy')

fruits_2d = fruits.reshape(-1, 100 * 100)

# s 모델 생성 및 학습
# n_clusters=3: 과일이 3종류이므로 3개의 그룹으로 나눔
km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)

# 분류 결과 확인
# print("부여된 레이블 종류:", np.unique(km.labels_))
# print("군집별 데이터 개수:", np.unique(km.labels_, return_counts=True))

# def draw_fruits(arr, ratio=1):
#     n = len(arr)
#     rows = int(np.ceil(n/10))
#     cols = n if n < 10 else 10
#     fig, axs = plt.subplots(rows, cols, figsize=(cols*ratio, rows*ratio), squeeze=False)
#     for i in range(rows):
#         for j in range(cols):
#             if i * 10 + j < n:
#                 axs[i, j].imshow(arr[i * 10 + j], cmap='gray_r')
#             axs[i, j].axis('off')
#     plt.show()

# # 6. 각 레이블별로 실제 어떤 과일이 들어갔는지 확인
# for label in range(3):
#     print(f"--- Label {label} 군집 결과 ---")
#     # 해당 레이블에 속하는 이미지만 필터링하여 출력
#     draw_fruits(fruits[km.labels_ == label])

inertia = []

for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)


plt.figure(figsize=(8, 5))
plt.plot(range(2, 7), inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.xticks(range(2, 7))
plt.grid(True)
plt.show()