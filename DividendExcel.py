# from openpyxl import load_workbook
#
# data_file = r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx'
#
# # Load the entire workbook.
# wb = load_workbook(data_file)
#
# # List all the sheets in the file.
# print("Found the following worksheets:")
# for sheetname in wb.sheetnames:
#     print(sheetname)



import pandas as pd
data_xls = pd.read_excel(r'c:\users\nicka\pycharmprojects\raspberrypiscripts\usdividendchampions.xlsx', 'Champions', engine='openpyxl')
data_xls.to_csv('csvfile.csv', encoding='utf-8')