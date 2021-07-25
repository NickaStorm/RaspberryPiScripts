from flask import Flask, render_template, Response
import json
import mariadb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

#this script needs to be in home/pi/webapp along with the templates dir

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)

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

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x1 = [1, 2, 3, 4]
    y1 = [2, 6, 1, 3]
    axis.plot(x1, y1)
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

#blah
app.run()