from flask import render_template
from testapp import app

@app.route('/')
def index():
    return render_template('testapp/index.html')

@app.route('/test')
def other1():
    return "テストページです！"
