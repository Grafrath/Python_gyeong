import pandas as pd

file_path = './data/train.csv'

df = pd.read_csv(file_path, encoding='UTF-8')

print('\n-------- pipe --------\n')

print(df)
print()
df.info()
print()
df_col = ['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
df_pipe = df[df_col].copy()
print(df.head())
print()

print('\n-------- 결측치 개수 --------\n')

print(df_pipe.isnull().sum())
print()

print('\n-------- 결측치 채우기 --------\n')

# age 결측치 평균으로 채우기
age_mean = df_pipe['Age'].mean()
df_pipe['Age'] = df_pipe['Age'].fillna(age_mean)

# Embarked 결측치 최빈값으로 채우기
emb_mode = df_pipe['Embarked'].mode()[0]
df_pipe['Embarked'] = df_pipe['Embarked'].fillna(emb_mode)

# 성별을 숫자로 변환
df_pipe['Sex'] = df_pipe['Sex'].map({'female': 0, 'male': 1})

print(df_pipe.isnull().sum())
print()

print('\n-------- 전처리 후 --------\n')

print(df_pipe.head())
print()
print(df_pipe.describe())
print()
df_pipe.info()
print()

print('\n-------- 함수로 구현 --------\n')

print(df.head())
print()
print(df.isnull().sum())
print()

def sel_col(df):
    df_res = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']].copy()
    return df_res

def fill_agemean(df):
    df_res = df.copy()
    df_res['Age'] = df_res['Age'].fillna(df_res['Age'].mean())
    return df_res

def fill_embmode(df):
    df_res = df.copy()
    df_res['Embarked'] = df_res['Embarked'].fillna(df_res['Embarked'].mode()[0])
    return df_res

def encode_sex(df):
    df_res = df.copy()
    df_res['Sex'] = df_res['Sex'].map({'female': 0, 'male': 1})
    return df_res

df_clean = encode_sex(fill_embmode(fill_agemean(sel_col(df))))
df_clean.info()
print()

print('\n-------- pipe로 구현 --------\n')

df_final = (df[df_col].copy()
            .pipe(sel_col)
            .pipe(fill_agemean)
            .pipe(fill_embmode)
            .pipe(encode_sex))

print(df_final.head())
print()
df_final.info()
print()

print('\n-------- pipe() 추가작업 --------\n')

def null_check(df, msg):
    print(f'\n======== [{msg}] ========\n')
    print(df.head(3))
    print('\n-------- 결측치 개수 --------\n')
    print(df.isnull().sum())
    
    return df

df_cl = (
    df
    .pipe(sel_col)
    .pipe(null_check, '컬럼 선택 후')
    .pipe(fill_agemean)
    .pipe(null_check, 'age 결측처리 후')
    .pipe(fill_embmode)
    .pipe(null_check, 'emb 결측처리 후')
    .pipe(encode_sex)
)

df_cl.info()
print()