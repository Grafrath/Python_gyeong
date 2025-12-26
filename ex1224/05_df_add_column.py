import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)


students = {'이름':['서준', '우현', '인아'],
            '수학':[90, 80, 70], 
            '영어':[88, 77, 66], 
            '사회':[30, 40, 50]}

df = pd.DataFrame(students)
print(df)
print()

df.index=['가', '나', '다']
print(df)
print()

# 이름 컬럼을 인덱스로 쓰고싶어
df = df.set_index('이름')
print(df)
print()


print("\n======= 열 추가하기 =======\n")
# 수학 컬럼 선택해서 뽑기 (복습)
print(df['수학'])
print()

# 국어 컬럼추가
df['국어'] = [80, 90, 100]
print(df)
print(df.shape)
print()

df['미술'] = 100 
print(df)


print("\n======= 행 추가하기 =======\n")

df.loc['동수'] = 0
print(df)
print()

df.loc['말숙'] = [34, 54, 77, 88, 90]
print(df)



print("\n======= 원소 값 변경 =======\n")

df.loc['동수', '수학'] = 65
print(df)
print()

# 동수 영어 70점 
df.iloc[3, 1] = 70
print(df)
print()

# 동수의 사회부터 미술까지 90, 98, 70
df.loc['동수', '사회':'미술'] = [90, 98, 100]
print(df)
print()

# 동수의 수학 국어 80, 60
df.loc['동수', ['수학', '국어']] = [80, 90]
print(df)


print("\n======= 행, 열 자리바꾸기 (전치) =======\n")

df = df.transpose()
print(df)
print()

df = df.T
print(df)
print()
