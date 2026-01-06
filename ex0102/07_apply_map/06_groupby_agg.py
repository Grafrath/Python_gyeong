import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]

# class 로 그룹바이
grouped = df.groupby(['class'], observed=True)
print(grouped)
print()

# 표준편차 집계
std_all = grouped.std(numeric_only=True)
print(std_all)
print()

# groupby(~~~~, as_index=False)  옵션 추가해보기
std_all_index = df.groupby(['class'], observed=True, as_index=False).std(numeric_only=True) 
print(std_all_index)


print('\n============================\n')

print(type(std_all))
std_all.info()
print()

# 그룹화(grouped) -> 집계(std_all) -> 컬럼선택(std_all['fare'])
print(std_all['fare'])
print()

# 그룹화 -> 컬럼선택 -> 집계
std_fare = grouped['fare'].std(numeric_only=True)
print(std_fare)
print()

std_age_survived = grouped[['age', 'survived']].std(numeric_only=True)
print(std_age_survived)


print('\n======= 그룹화 후 describe =======\n')

print(grouped.describe())
print()
print(df.describe())



print('\n======= 그룹화 후 value_counts =======\n')

print(grouped[['class', 'sex']].value_counts())
print()

# 원래 value_counts 작동
print(df['class'].value_counts())
print()

# grouped 와 비교
print(df[['class', 'sex']].value_counts())
print()


print('\n======= agg 메서드 =======\n')

# 여러 함수나 컬럼별 다른 함수를 쓰기 위한 agg 메서드
# aggregate() 애그리거트 - 합계, 총합...

# 그룹 객체에 aggregate() 메서드 적용
agg_mean = grouped.aggregate('mean', numeric_only = True)
print(agg_mean)
print()

# agg 로도 쓸 수 있다. 
agg_mean2 = grouped.agg('mean', numeric_only = True)
print(agg_mean2)
print()

# (원본에 문자열 male female)
# agg_mean2 = grouped.agg('mean') # 문자열은 mean이 안되므로 오류
# print(agg_mean2)
# print()

# max/min 은 문자열에서도 작동 가능해서 오류X
agg_mean2 = grouped.agg('max') # numeric_only = True 이거 추가 해줘도 작동함
print(agg_mean2)
print()

# 여러 집계함수를 적용 # 이 경우는 어떻게 해도 안됨.
# agg_all = grouped.agg(['mean', 'std']) 
# print(agg_all)
# print()

agg_all = grouped.agg(['min', 'max']) # numeric_only = True 이 옵션 자체가 작동 X
print(agg_all)
print()

# 더 구체적으로 적용 (권장)
agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
print(agg_sep)
print()


# 함수를 만들어 적용
def min_max(x):
    return x.max() - x.min()

agg_minmax =  grouped[['age', 'fare']].agg(min_max)
print(agg_minmax)
print()

# 좀 더 안정적인 방법
agg_minmax2 = grouped.agg({'age': min_max, 'fare': min_max})
print(agg_minmax2)