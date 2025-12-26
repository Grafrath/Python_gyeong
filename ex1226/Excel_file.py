import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

file_path = './data/남북한발전전력량.xlsx'

df = pd.read_excel(file_path)
print(df)
print()

df2 = pd.read_excel('C:\\Users\\admin\\Desktop\\New\\Python_gyeong\\data\\남북한발전전력량.xlsx')
print(df2)
print()