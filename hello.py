from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html', title = 'Stanton, Inc.')

@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html', title = 'Bitcoin Price')

@app.route('/weather')
def weather():
    return render_template('weather.html', title = 'Weather Forecast')

app.run()