from flask import Flask, render_template
import json
import mariadb

#this script needs to be in home/pi/webapp along with the templates dir

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)
app.config["DEBUG"] = True

config = {
    'host': '127.0.0.1',
    'port': 5000,
    'user': 'root',
    'password': 'blueberry',
    'database': 'dividendchampions'
}

#creates the base home page
@app.route('/')
def index():
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    cur.execute("select * from stockinfo")

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # return the results!
    return json.dumps(json_data)


#the index file has to be in a dir named templates in webapp
#creates the table sub page
@app.route('/tables')
def tables():
    return render_template('index.html')







app.run()