import yfinance as yf
import datetime
import time
import mysql.connector

temptime = time.strftime('%Y-%m-%d')
curDate = datetime.date.today()
Date1 = curDate - datetime.timedelta(days=1)
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
                       (ticker, name, currentprice, forwardPE, sector, curDate) VALUES (%s,%s,%s,%s,%s,%s)"""

def getTickerData(ticker, stockNum):

    # FIX THIS ABOMINATION LATER
    if ticker == "ARTN.A":
        ticker = "ARTNA"
    elif ticker == "BF.B":
        ticker = "BF-B"
    elif ticker == "EV":
        ticker = "ETV"
    elif ticker == "JW.A":
        ticker = "JW-A"
    elif ticker == "MKC.V":
        ticker = "MKC-V"

    print(ticker)
    tickerData = yf.Ticker(ticker)
    listOfTicker = [ticker, tickerData.info["shortName"], tickerData.info["currentPrice"], tickerData.info["forwardPE"], tickerData.info["sector"], temptime]
    print(str(stockNum) + " " + ticker + " = " + tickerData.info["shortName"])
    return listOfTicker

cur.execute("select stickersymbol from stockinfo")
rv = cur.fetchall()
for result in rv:
    sqlData.append(result)

indexNum = 1

for item in sqlData:
    cur.execute(graphData_query, getTickerData(item[0], indexNum))
    indexNum += 1

conn.commit()
conn.close()


