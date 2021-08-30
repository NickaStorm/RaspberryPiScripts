from flask import Flask, render_template, Response
import mysql.connector
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/templates/"
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from io import BytesIO
import mpld3
from mpld3 import fig_to_html, plugins

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

#this script needs to be in home/pi/webapp along with the templates dir

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)

headers = ('Ticker', 'Name', 'Sector', 'Industry')

#creates the base home page
@app.route('/')
def index():
    data = []
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='user',
        password="blueberry",
        db='dividendchampions',
    )
    cur = conn.cursor()
    cur.execute("select * from stockinfo")
    rv = cur.fetchall()
    for result in rv:
        data.append(result)

    fig = plt.figure()
    plt.plot([1, 2, 3, 4, 5, 6], [217, 215, 213, 205, 231, 197])
    plt.xlabel("Date", fontweight='bold', fontsize=24)
    plt.ylabel("Price", fontweight='bold', fontsize=24)
    plt.title("<NOT REAL>Dividend Stock Price", fontweight='bold', fontsize=36)

    graph = mpld3.fig_to_html(fig)
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<style>
    *{
    margin: 0;
    padding: 0;
    font-family: fantasy;
    }

    .title {
    text-align:left;
    border-bottom: 2px solid black;
    font-size: 85px;
    font-family: fantasy;
    background-color: dimgray;
    color: white;
    padding-left: 10px;
    height: 25%;
    width: 100%;
    }

    .link {
    text-decoration: none;
    font-family: fantasy;
    font-size: 40px;
    color: gainsboro;
    padding: 0px;
    padding-left: 50px;
    }
    
    .graph {
    border: 2px solid black
    text-align: center;
    }
    @media screen and (min-width: 601px) {
                div.example {
                    font-size: 40px;
                }
                .a{
                    font-size: 25px;
                    text-align: center;
                }
            }
            @media screen and (max-width: 600px) {
                div.example {
                    font-size: 30px;
                }
                .a{
                    font-size: 18px;
                    text-align: center;
                }
            }
            @media screen and (min-width: 800px) {
                div.example {
                    font-size: 60px;
                }
                .a{
                    font-size: 35px;
                }
</style>
    <meta charset="UTF-8">
    <title>Explore Prometheus</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background-color: whitesmoke;">

<div class="example">Project Prometheus
    <a href="/stockinfo" class="link">Table</a>
    <a href="/" class="link">Info</a>
</div>
<center style="padding-top: 50px;">
""" + graph + """
</center>

</body>
</html>
"""

#the index file has to be in a dir named templates in webapp
#creates the table sub page
@app.route('/stockinfo')
def tables():
    data = []
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='user',
        password="blueberry",
        db='dividendchampions',
    )
    cur = conn.cursor()
    cur.execute("select * from stockinfo")
    rv = cur.fetchall()
    for result in rv:
        data.append(result)

    return render_template('index.html', headings=headers, data=data)