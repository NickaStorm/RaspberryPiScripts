import pandas as pd
import sqlite3
import openpyxl

#use /home/pi/USDividendChampions1.xlsx on the raspberry pi

data_xls = pd.read_excel(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx', sheet_name='Champions', engine='openpyxl', skiprows=2, index_col=0, usecols='A,B,D,E,AN')
#A = Symbol, B = Company, D = Sector, E = No Years, AN = Industry

data_xls.to_csv('csvfile.csv', encoding='utf-8')
data = pd.read_csv('csvfile.csv')

con = sqlite3.connect('dividendchampions.db')
cur = con.cursor()

def insertdata(info):
    indexnumber = 0
    for row in info:
        stockinfo = info[indexnumber].tolist()
        yearsonlist = stockinfo.pop(3)
        cur.execute("insert into stockinfo (stockname, stickersymbol, sector, industry) values (?, ?, ?, ?)", stockinfo)
        cur.execute("insert into stockdates (dateofinfo, yearsonlist) values (?, ?)", ('curdate()', yearsonlist))
        indexnumber += 1



insertdata(data.iloc)

con.commit()
con.close()