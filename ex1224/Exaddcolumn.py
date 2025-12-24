import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

students = {'이름':['서준','우현','인아'],
            '수학':[90,80,70],
            '영어':[80,70,90],
            '음악':[70,60,80] }
df = pd.DataFrame(students)
df.index=['가','나','다']
print(df)
print()

df = df.set_index('이름')
print(df)
print()

print('\n-------- 열 추가 --------\n')

print(df['수학'])
print()

df['국어'] = [80,90,70]
print(df)
print(df.shape)
print()

df['미술'] = 100
print(df)
print(df.shape)
print()

print('\n-------- 행 추가 --------\n')

df.loc['민수'] = [85, 95, 100, 80, 90]
print(df)
print()

new_student = pd.DataFrame({
                            '수학': [95],
                            '영어': [85],
                            '음악': [90],
                            '국어': [90],
                            '미술': [90]},
                            index=['지아'])
df = pd.concat([df, new_student])
print(df)
print()