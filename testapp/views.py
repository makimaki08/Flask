from flask import render_template, request
from testapp import app

@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です',
        'insert_something2': 'views.pyのinsert_something2部分です',
        'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route('/test')
def other1():
    return render_template('testapp/index2.html')


@app.route('/sampleform')
def sample_form():
    return render_template('testapp/sampleform.html')


@app.route('/sampleform-post', methods=['POST'])
def sample_form_temp():
    print('POSTデータを受け取ったので処理します')
    req1 = request.form['data1']
    return f'POSTデータを受け取ったよ: {req1}'
