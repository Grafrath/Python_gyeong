import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 200)

df = pd.read_csv("./data/train.csv")

print(df)
print()
df.info()

df2 = df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]].copy()


print('\n======= 결측치 확인 =======\n')

missing = df2.isnull()
print(missing.sum())


# Age 결측치 평균으로 채우기
age_mean = df2["Age"].mean()
df2["Age"] = df2["Age"].fillna(age_mean)


# Embarked 결측치 최빈값으로 채우기
emb_mode = df2["Embarked"].mode()[0]
df2["Embarked"] = df2["Embarked"].fillna(emb_mode)


# 성별을 숫자로 변환
df2["Sex"] = df2["Sex"].map({"male": 0, "female": 1})



print('\n======= 전처리 후 =======\n')

print(df2.head())
print()
print(df2.describe())
print()
df2.info()


print('\n======= 함수로 구현 =======\n')

def select_columns(df):
    return df[["Survived", "Pclass", "Sex", "Age", "Fare", "Embarked"]]

def fill_age_mean(df):
    df = df.copy()
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df

def fill_embarked_mode(df):
    df = df.copy()
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    return df

def encode_sex(df):
    df = df.copy()
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    return df

df_clean = encode_sex(fill_embarked_mode(fill_age_mean(select_columns(df))))
df_clean.info()


print('\n======= pipe() 함수 사용 =======\n')

df_clean2 = (
    df
    .pipe(select_columns)
    .pipe(fill_age_mean)
    .pipe(fill_embarked_mode)
    .pipe(encode_sex)
)

df_clean2.info()


print('\n======= pipe() 함수 추가작업 =======\n')

def null_check(df, msg):
    print(f"\n======= [{msg}] =======\n")
    print(df.head(3))
    print("\n결측치 개수\n")
    print(df.isnull().sum())
    return df

df_clean3 = (
    df
    .pipe(select_columns)
    .pipe(null_check, "컬럼 선택 후")
    .pipe(fill_age_mean)
    .pipe(null_check, "Age 결측 처리 후")
    .pipe(fill_embarked_mode)
    .pipe(null_check, "Embarked 결측 처리 후")
    .pipe(encode_sex)
)
