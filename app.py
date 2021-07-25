from flask import Flask, render_template
import json
import mariadb
import matplotlib.pyplot as plt
from io import BytesIO
import base64

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
headers = ('Sticker', 'Name', 'Sector', 'Industry')
jsonData = []

#creates the base home page
@app.route('/')
def index():
    conn = mariadb.connect(**config)
    cur = conn.cursor()

    cur.execute("select * from stockinfo")

    # serialize results into JSON
    rv = cur.fetchall()
    for result in rv:
        jsonData.append(result)

    return json.dumps(jsonData)


#the index file has to be in a dir named templates in webapp
#creates the table sub page
@app.route('/stockinfo')
def tables():
    conn = mariadb.connect(**config)
    cur = conn.cursor()

    cur.execute("select * from stockinfo")

    # serialize results into JSON
    rv = cur.fetchall()
    for result in rv:
        jsonData.append(result)

    return render_template('index.html', headings=headers, data=jsonData)

@app.route('/stockgraph')
def stockgraph():
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("select * from stockinfo")
    rv = cur.fetchall()
    for result in rv:
        jsonData.append(result)

    img = BytesIO()
    y = [1, 2, 3, 4, 5]
    x = [0, 2, 1, 3, 4]

    plt.plot(x, y, label='line name')
    plt.xlabel('x axis name')
    plt.ylabel('x axis name')
    plt.title('test graph')
    plt.legend()
    plt.savefig(img, format='jpg')
    plt.close()
    img.seek(0)

    plot = base64.b64encode(img.getvalue())

    return render_template('stockgraph.html', graph=plot)





app.run()