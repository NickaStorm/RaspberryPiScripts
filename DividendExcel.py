import sqlite3
import openpyxl
import csv

#workbook = openpyxl.load_workbook(r'/home/pi/USDividendChampions1.xlsx')
workbook = openpyxl.load_workbook(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx')
if "Champions" in workbook.sheetnames:
    sheet = workbook["Champions"]
else:
    print("Error, unable to find champions sheet name = Champions")

with open('test.csv', 'w', newline='') as file:
    csv = csv.writer(file, delimiter = '%')
    sheet.delete_rows(1, 3)
    sheet.delete_cols(6, 33)
    sheet.delete_cols(3, 1)
    sheet.delete_cols(5, 1)
    for col in sheet.iter_cols():
        for row in sheet.iter_rows():
            csv.writerow([cell.value for cell in row])

def insertdata(info):
    con = sqlite3.connect('dividendchampions.db')
    cur = con.cursor()
    yearsonlist = info.pop(3)
    cur.execute("insert into stockinfo (stockname, stickersymbol, sector, industry) values (?, ?, ?, ?)", info)
    cur.execute("insert into stockdates (dateofinfo, yearsonlist) values (?, ?)", ('curdate()', yearsonlist))
    con.commit()
    con.close()

# data_xls = pd.read_excel(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx', sheet_name='Champions', engine='openpyxl', skiprows=2, index_col=0, usecols='A,B,D,E,AN')
#A = Symbol, B = Company, D = Sector, E = No Years, AN = Industry

# data_xls.to_csv('csvfile.csv', encoding='utf-8')
# data = pd.read_csv('csvfile.csv')

with open('test.csv', 'r') as file:
    for line in file:
        list = line.split('%')
        list[4] = list[4].strip('\n')
        insertdata(list)
        #print(list)
