print('\n======= 문자열 더하기 =======')

head = "Python"
tail = " is fun!"
print(head + tail)


a = "python"
print(a * 2)


print("=" * 50)
print("My Program")
print("=" * 50)


print("\n======= 문자열 길이 구하기 =======")

a = "Life is too short"
print(len(a))  #17



print("\n======= 문자열 인덱싱 =======")

a = "Life is too short, You need Python"
print(a[3])  #e
print(a[0])  #L
print(a[-1]) #n
print(a[-2]) #o
print(a[-5]) #y



print("\n======= 문자열 슬라이싱 =======")

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b) #Life

a = "Life is too short, You need Python"
b = a[0:4]
print(b) #Life

b = a[0:3]  # 0 <= a < 3
print(b) #'Lif'

b = a[0:5]  
print(b) # 'Life ' 

b = a[5:7]
print(b)  # is

b = a[12:17]
print(b) # short

b = a[19:]
print(b) # You need Python

b = a[:17]
print(b) # Life is too short

b = a[:]
print(b) 

b = a[19:-7]
print(b)


print("\n======= 문자열 나누기 =======")

a = "20250821Sunny"
date = a[:8]
weather = a[8:]
print("오늘 날짜 = ", date)
print("오늘 날씨 = ", weather)


a = "20250821Sunny"
year = a[:4]
day = a[4:8]
weather = a[8:]

print("올해 년도 = ", year)
print("오늘 날짜 = ", day)
print("오늘 날씨 = ", weather)

print()
print("-" * 10)
print()


a = "Pithon"
print(a[:1] + 'y' + a[2:])
# Python













