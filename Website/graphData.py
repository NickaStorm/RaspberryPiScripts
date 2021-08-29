import yfinance as yf
import datetime
import mysql.connector

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

cur.execute("select * from stockinfo")
rv = cur.fetchall()
for result in rv:
    sqlData.append(result)
    print(result)

# tickerSymbol = 'DOV'

# tickerData = yf.Ticker(tickerSymbol)
# stockInfo = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], curDate]

def getTickerData(ticker):
    tickerData = yf.Ticker(ticker)
    listOfTicker = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], curDate]
    return listOfTicker

indexNum = 0

for item in sqlData:
    # cur.execute(graphData_query, getTickerData(sqlData[indexNum]))
    indexNum += 1
    print(item)

conn.commit()
conn.close()


