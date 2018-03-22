from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def weather():
    return "hello World!"
    render_template('index.html')

app.run()

