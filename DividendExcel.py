import mariadb
import openpyxl
import csv

#workbook = openpyxl.load_workbook(r'/home/pi/USDividendChampions1.xlsx')
workbook = openpyxl.load_workbook(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx')

if "Champions" in workbook.sheetnames:
    sheet = workbook["Champions"]
else:
    print("Error, unable to find champions sheet name = Champions")

def convertXlToCsv():
    with open('test.csv', 'w', newline='') as file:
        tempcsv = csv.writer(file, delimiter = '%')
        #deletes the head rows that display names
        sheet.delete_rows(1, 3)
        #deletes everything that isn't necessary
        sheet.delete_cols(6, 33)
        sheet.delete_cols(3, 1)
        sheet.delete_cols(5, 1)
        for row in sheet.iter_rows():
            tempcsv.writerow([cell.value for cell in row])

def insertData(info):
    con = mariadb.connect(
        user="root",
        password="blueberry",
        host="127.0.0.1",
        port=3306,
        database="dividendchampions"
    )
    cur = con.cursor()
    yearsonlist = info.pop(3)
    cur.execute("insert into stockinfo (stickersymbol, stockname, sector, industry) values (?, ?, ?, ?)", info)
    cur.execute("insert into stockdates (dateofinfo, yearsonlist) values (?, ?)", ('curdate()', yearsonlist))
    con.commit()
    con.close()

def convertCsvPrep():
    with open('test.csv', 'r') as file:
        for line in file:
            list = line.split('%')
            list[4] = list[4].strip('\n')
            insertData(list)

convertXlToCsv()
convertCsvPrep()
