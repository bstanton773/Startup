from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

app.run()