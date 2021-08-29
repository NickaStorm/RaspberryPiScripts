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

def getTickerData(ticker, stockNum):
    # strTicker = ''.join(ticker)
    print(ticker)
    stockTicker = ticker.replace(".", "")

    # FIX THIS ABOMINATION LATER
    if stockTicker == "BFB":
        stockTicker = "BF-B"

    tickerData = yf.Ticker(stockTicker)
    listOfTicker = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], temptime]
    print(str(stockNum) + " " + ticker + " = " + tickerData.info["shortName"])
    return listOfTicker

cur.execute("select stickersymbol from stockinfo")
rv = cur.fetchall()
for result in rv:
    sqlData.append(result)

indexNum = 1

for item in sqlData:
    # stockTicker = item[0].replace(".", "")
    cur.execute(graphData_query, getTickerData(item[0], indexNum))
    # print(item[0])
    indexNum += 1

print(sqlData)

conn.commit()
conn.close()


