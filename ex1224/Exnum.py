import numpy as np

print('\n-------- 넘피배열 --------\n')

a = np.array([1,2,3])
print(a)
print(type(a))

print('\n-------- 데이터 타입 --------\n')

a = np.array([1,2,3])
print(a.dtype)
print()
b = np.array([1.0, 2.0])
print(b.dtype)
print()
c = np.array([1, 2.0, 3])
print(c.dtype)

print('\n-------- numpy 함수 --------\n')

print(np.zeros([1,2,3]))
print(np.ones([1,2,3]))
print(np.arange(1,2,3))
print(np.linspace(1, 2, 3))

print('\n-------- 차원? --------\n')

a = np.array([[1,2,3],[4,5,6]])

print(a)
print()
print(a.shape)
print()
print(a.ndim)
print()

b = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(b)
print()
print(b.shape)
print()
print(b.ndim)

print('\n-------- 인덱싱, 슬라이싱 --------\n')


a = np.array([10, 20, 30, 40])
print(a[0])
print()
print(a[1:3])
print()

a = np.array([[1,2],[3,4]])
print(a[0,1])
print()
print(a[0:2])

print('\n-------- 브로드 캐스팅 --------\n')

a = np.array([1, 2, 3])
print(a+10)

print('\n-------- 벡터 연산 --------\n')

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)

print('\n-------- 집계함수 --------\n')

a = np.array([1, 2, 3, 4])
print(a.sum())
print(a.mean())
print(a.max())
print(a.min())