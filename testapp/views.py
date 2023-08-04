from flask import render_template, request
from testapp import app
from random import randint

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
    return render_template('testapp/add_employee.html')