from flask import Flask, render_template
import json
import mariadb

#this script needs to be in home/pi/webapp along with the templates dir

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)
#app.config["DEBUG"] = True

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'blueberry',
    'database': 'dividendchampions'
}
headings = ('Sticker', 'Name', 'Sector', 'Industry')
jsonData = []

#creates the base home page
@app.route('/')
def index():
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    cur.execute("select * from stockinfo where stickersymbol like 'a%'")

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    for result in rv:
        jsonData.append(dict(zip(row_headers, result)))

    lst = jsonData.values()
    lst2 = list(lst)

    # return the results!
    return json.dumps(lst2)

valuesOfJson = jsonData.values()
valuesList = list(valuesOfJson)

#the index file has to be in a dir named templates in webapp
#creates the table sub page
@app.route('/tables')
def tables():
    return render_template('index.html', headings=headings, data=valuesList)







app.run()