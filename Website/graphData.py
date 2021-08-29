import yfinance as yf
import datetime
import mysql.connector

curDate = datetime.date.today()
Date1 = curDate - datetime.timedelta(days=1)
# Date2 = curDate - datetime.timedelta(days=2)
tickerSymbol = 'DOV'
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
graphData_query = """ INSERT INTO graphata
                       (name, currentprice, forwardPE, sector, curDate) VALUES (%s,%s,%s,%s,%s)"""

cur.execute("select stickersymbol from stockinfo")
rv = cur.fetchall()
for result in rv:
    sqlData.append(result)

tickerData = yf.Ticker(tickerSymbol)
stockInfo = [tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], curDate]

for item in sqlData:
    cur.execute(graphData_query, stockInfo)
    print(item)

conn.commit()
conn.close()


