from flask import Flask, render_template

#creates a web app at http://127.0.0.1:5000 then add any sub pages
app = Flask(__name__)

#creates the base home page
@app.route('/')
def index():
    return 'Home page'

#creates the table sub page
@app.route('/tables')
def tables():
    return render_template('index.html')

#runs the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
