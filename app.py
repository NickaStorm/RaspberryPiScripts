from flask import Flask, render_template

#this script needs to be in home/pi/webapp along with the templates dir

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)

#creates the base home page
@app.route('/')
def index():
    return 'Home page'

#the index file has to be in a dir named templates in webapp
#creates the table sub page
@app.route('/tables')
def tables():
    return render_template('index.html')

#runs the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
