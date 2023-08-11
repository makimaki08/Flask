from flask import render_template, request, redirect, url_for
from testapp import app
from random import randint
from testapp import db
from testapp.models.employee import Employee

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


@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('testapp/sampleform.html')

    if request.method == 'POST':
        # ジャンケンの手を文字列の数じ0~2で受け取る
        hands = {
            '0':'グー',
            '1':'チョキ',
            '2':'パー',
        }
        janken_mapping = {
            'draw':'引き分け',
            'win':'勝ち',
            'lose':'負け'
        }

        player_hand_ja = hands[request.form['janken']] # 日本語表示用
        player_hand = int(request.form['janken']) # 辞書型で利用するため、str型→int型に変換
        enemy_hand = randint(0,2)
        enemy_hand_ja = hands[str(enemy_hand)]

        if player_hand == enemy_hand:
            judgement = 'draw'

        elif (player_hand == 0 and enemy_hand == 1) or (player_hand == 1 and enemy_hand == 2) or (player_hand == 2 and enemy_hand == 0):
            judgement = 'win'

        else:
            judgement = 'lose'

        result = {
            'enemy_hand_ja':enemy_hand_ja,
            'player_hand_ja':player_hand_ja,
            'judgement':judgement
        }
        return render_template('testapp/janken_result.html', result=result)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('testapp/add_employee.html')
    if request.method == 'POST':
        # str型の値を取得
        form_name = request.form.get('name')
        form_mail = request.form.get('mail')
        form_department = request.form.get('department')

        # bool型の値を取得
        form_is_remote = request.form.get("is_remote", default=False, type=bool)

        # int型の値を取得
        form_year = request.form.get('year', default=0, type=int)


        employee = Employee(
            name = form_name,
            mail = form_mail,
            is_remote = form_is_remote,
            department = form_department,
            year = form_year
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/employees')
def employee_list():
    employees = Employee.query.all()
    return render_template('testapp/employee_list.html', employees = employees)

@app.route('/employees/<int:id>')
def employee_detail(id):
    employee = Employee.query.get(id)
    return render_template('testapp/employee_detail.html', employee=employee)
