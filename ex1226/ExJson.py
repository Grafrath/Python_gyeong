import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

file_path = './data/read_json_sample.json'

df = pd.read_json(file_path)
print(df)
print()

df2 = pd.read_json(file_path, orient='index')
print(df2)
print()

df3 = pd.read_json(file_path, orient='columns')
print(df3)
print()