import yfinance as yf
import datetime
import time
import mysql.connector

temptime = time.strftime('%Y-%m-%d')
curDate = datetime.date.today()
Date1 = curDate - datetime.timedelta(days=1)
# Date2 = curDate - datetime.timedelta(days=2)
sqlData = []

conn = mysql.connector.connect(
        host='localhost',
        user='user',
        password='blueberry',
        # port=3306,
        database='dividendchampions',
        auth_plugin='mysql_native_password'
    )
cur = conn.cursor(prepared=True)
graphData_query = """ INSERT INTO graphdata
                       (name, currentprice, forwardPE, sector, curDate) VALUES (%s,%s,%s,%s,%s)"""

# cur.execute("select stickersymbol from stockinfo")
# rv = cur.fetchall()
# for result in rv:
#     sqlData.append(result)
#     print(result)

# tickerSymbol = 'DOV'

# tickerData = yf.Ticker(tickerSymbol)
# stockInfo = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], curDate]

# indexNum = 0

def getTickerData(ticker, index):
    # strTicker = ''.join(ticker)
    tickerData = yf.Ticker(ticker)
    listOfTicker = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], temptime]
    print(tickerData.info["shortName"])
    # print(tickerData.info["Name"])
    return listOfTicker

cur.execute("select stickersymbol from stockinfo")
rv = cur.fetchall()
for result in rv:
    sqlData.append(result)
indexNum = 0

for item in sqlData:
    cur.execute(graphData_query, getTickerData(item[0], indexNum))
    indexNum += 1
    print(item[0])

print(sqlData)

conn.commit()
conn.close()


