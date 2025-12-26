import numpy as np

# 빠른 "배열" 계산
# 벡터/행렬 계산


print('\n======= 넘피배열 기본생성 =======\n')

a = np.array([1, 2, 3])
print(a)
print(type(a))

# 파이썬 list 보다 훨씬 빠름 (C로 만들어졌음)
# 벡터연산 가능



print('\n======= 데이터 타입 =======\n')

a = np.array([1, 2, 3])
print(a.dtype) # int64
print()

b = np.array([1.0, 2.0])
print(b.dtype) # float64
print()

# 자동 형변환
c = np.array([1, 2.0, 3])
print(c.dtype) # float64


print('\n======= 넘피 함수들 =======\n')

print(np.zeros(3)) # [0. 0. 0.]
print(np.ones(3)) # [1. 1. 1.]
print(np.arange(0, 10)) # 0~9
print(np.linspace(0, 1, 5))


print('\n======= 차원, 크기 =======\n')

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)
print(a.shape)
print(a.ndim)

print('\n====================\n')

# 3차원 배열
b = np.array([1, 2, 3]) # 선
print(b.shape)
print(b.ndim)
print()

b = np.array([[1, 2, 3],
             [4, 5, 6]]) # 면
print(b.shape)
print(b.ndim)
print()

b = np.array([[[1, 2, 3],
               [4, 5, 6]],

             [[7, 8, 9],
              [4, 5, 6]]]) # 3차원
print(b.shape)
print(b.ndim)
print(b)

print(b[1, 0 ,2]) # 9

print('\n======= 인덱싱 & 슬라이싱 =======\n')

a = np.array([10, 20, 30, 40])

print(a[0]) # 10
print(a[1:3]) # [20 30]


a = np.array([[1, 2],
              [3, 4]])

print(a[0, 1])  # 2


print('\n======= 브로드 캐스팅 =======\n')

a = np.array([1, 2, 3])
print(a + 10) # [11 12 13]
# 반복문 없이 자동 확장 계산


print('\n======= 벡터 연산 =======\n')

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b) # [5 7 9]
print(a * b) # [ 4 10 18]



print('\n======= 집계함수 =======\n')

a = np.array([1, 2, 3, 4])

print(a.sum())
print(a.mean()) # 평균
print(a.max())
print(a.min())

# pandas Series, DataFrame -> 내부는 NumPy
# int64, float64 -> NumPy dtype