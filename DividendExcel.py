import pandas as pd
import sqlite3

#use /home/pi/USDividendChampions1.xlsx on the raspberry pi

data_xls = pd.read_excel(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx', sheet_name='Champions', engine='openpyxl', skiprows=2, index_col=0, usecols='A,B,D,E,AN')
#A = Symbol, B = Company, D = Sector, E = No Years, AN = Industry

data_xls.to_csv('csvfile.csv', encoding='utf-8')
data = pd.read_csv('csvfile.csv')

con = sqlite3.connect('dividendchampions.db')
cur = con.cursor()

def insertdata(info, table1, table2):
    indexnumber = 0
    for row in info:
        stockinfo = info[indexnumber].tolist()
        yearsonlist = stockinfo.pop(3)
        print(yearsonlist)
        print(stockinfo)
        #cur.execute(
        print(f'insert into {table1} (stockname, stickersymbol, sector, industry) values ({stockinfo[1]}, {stockinfo[0]}, {stockinfo[2]}, {stockinfo[3]})')
        indexnumber += 1



insertdata(data.iloc, 'stockinfo', 'stockdates')

con.commit()