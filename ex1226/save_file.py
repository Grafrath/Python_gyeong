import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ 'A', 'A+', 'B'],
        'basic' : [ 'C', 'B', 'B+'],
        'c++' : [ 'B+', 'C', 'C+']}

df = pd.DataFrame(data)
print(df)
print()

df = df.set_index('name')
print(df)
print()

print('\n-------- csv로 저장하기 --------\n')

df.to_csv('./data/output_sample.csv', encoding='utf-8-sig')
print('csv 파일로 저장 완료')
print()

print('\n-------- Json로 저장하기 --------\n')

df.to_json('./data/output_sample.json')
print('Json 파일로 저장 완료')
file_path = './data/output_sample.json'
df = pd.read_json(file_path)
print(df)
print()

df.to_json('./data/output_split_sample.json', orient='split')
print('Json_split 파일로 저장 완료')
file_path = './data/output_split_sample.json'
df = pd.read_json(file_path)
print(df)
print()

df.to_json('./data/output_records_sample.json', orient='records')
print('Json_records 파일로 저장 완료')
file_path = './data/output_records_sample.json'
df = pd.read_json(file_path)
print(df)
print()

df.to_json('./data/output_index_sample.json', orient='index')
print('Json_index 파일로 저장 완료')
file_path = './data/output_index_sample.json'
df = pd.read_json(file_path)
print(df)
print()

print('\n-------- Excel로 저장하기 --------\n')

df.to_excel('./data/output_sample.xlsx', index=True)
print('Excel 파일로 저장 완료')
file_path = './data/output_sample.xlsx'
df = pd.read_excel(file_path)
print(df)
print()


df.to_excel('./data/output_noindex_sample.xlsx', index=False)
print('Excel_noindex 파일로 저장 완료')
file_path = './data/output_noindex_sample.xlsx'
df = pd.read_excel(file_path)
print(df)
print()

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ 'A', 'A+', 'B'],
         'basic' : [ 'C', 'B', 'B+'],
         'c++' : [ 'B+', 'C', 'C+']}

data2 = {'c0':[1, 2, 3],
         'c1':[4, 5, 6],
         'c2':[7, 8, 9],
         'c3':[10, 11, 12]}

df1 = pd.DataFrame(data1)
df1 = df1.set_index('name')
print(df1)
print()