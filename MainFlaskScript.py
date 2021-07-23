from flask import Flask

app = Flask(__name__)

#creates the base home page
@app.route('/')
def index():
    return 'Hello world'

#creates the table sub page
@app.route('/tables')
def tables():
    return 'insert table here'

#runs the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
