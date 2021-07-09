import pandas as pd
data_xls = pd.read_excel(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx', sheet_name='Champions', engine='openpyxl', skiprows=2, index_col=0, usecols='A,B,D,E,AN')
#A = Symbol, B = Company, D = Sector, E = No Years, AN = Industry
data_xls.to_csv('csvfile.csv', encoding='utf-8')

data = pd.read_csv('csvfile.csv')

for row in data.iloc:
    print(row)
# print(data.iloc[0])