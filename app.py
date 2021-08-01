#!python3
# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, make_response, redirect
import random

app = Flask(__name__, static_url_path='/static')

sub_list = [
    "スプラッシュボム", #0
    "キューバンボム", #1
    "クイックボム", #2
    "スプリンクラー", #3
    "ジャンプビーコン", #4
    "スプラッシュシールド", #5
    "ポイントセンサー", #6
    "トラップ", #7
    "カーリングボム", #8
    "ロボットボム", #9
    "ポイズンミスト", #10
    "タンサンボム", #11
    "トーピード", #12
]

sp_list = [
    "ジェットパック", #0
    "スーパーチャクチ", #1
    "マルチミサイル", #2
    "ハイパープレッサー", #3
    "アメフラシ", #4
    "インクアーマー", #5
    "イカスフィア", #6
    "バブルランチャー", #7
    "ナイスダマ", #8
    "ウルトラハンコ", #9
    "スプラッシュボムピッチャー", #10
    "キューバンボムピッチャー", #11
    "カーリングボムピッチャー", #12
    "ロボボムピッチャー", #13
    "クイックボムピッチャー", #14
]

weapon_list = [
    #[武器名, サブID, スペシャルID]
    ["わかばシューター", 0, 5], #0
    ["もみじシューター", 9, 4], #1    
    ["スプラシューター", 2, 1], #2
    ["スプラシューターコラボ",0 ,0 ], #3
    ["プロモデラーMG", 1, 12], #4
    ["プロモデラーRG", 3, 6], #5
    ["プライムシューター", 6, 4], #6
    ["プライムシューターコラボ", 1, 7], #7
    [".52ガロン", 6, 6], #8
    [".52ガロンデコ", 8, 3], #9
    [".96ガロン", 3, 5], #10
    [".96ガロンデコ", 5, 1], #11 
    ["ジェットスイーパー", 10, 2], #12
    ["ジェットスイーパーカスタム", 2, 3], #13
    ["N-ZAP85", 1, 5], #14
    ["N-ZAP89", 9, 2], #15
    ["L3リールガン", 8, 6], #16
    ["L3リールガンD", 2, 0], #17
    ["H3リールガン", 6, 2], #18
    ["H3リールガンD", 1, 5], #19
    ["シャープマーカー", 10, 0], #20 
    ["ボールドマーカー", 8, 1], #21
    ["ボールドマーカーネオ", 4, 2], #22
    ["パブロ", 0, 1], #23
    ["パブロ・ヒュー", 7, 6], #24
    ["ホクサイ", 9, 0], #25
    ["ホクサイ・ヒュー", 4, 2], #26
    ["カーボンローラー", 9, 4], #27
    ["スプラローラー", 8, 1], #28
    ["スプラローラーコラボ", 4, 6], #29
    ["ヴァリアブルローラー", 5, 10], #30
    ["ヴァリアブルローラーフォイル", 1, 2], #31
    ["ダイナモローラー", 7, 3], #32
    ["ダイナモローラーテスラ", 0, 5], #33
    ["スプラマニューバー", 2, 2], #34
    ["スプラマニューバーコラボ", 8, 0], #35
    ["クアッドホッパーブラック", 9, 1], #36
    ["スパッタリー", 4, 11], #37
    ["スパッタリー・ヒュー", 10, 4], #38
    ["ケルビン525", 7, 0], #39
    ["デュアルスイーパー", 6, 2], #40
    ["スクイックリンα", 6, 5], #41
    ["スプラチャージャー", 0, 3], #42
    ["スプラチャージャーコラボ", 5, 11], #43
    ["スプラスコープ", 0, 3], #44
    ["スプラスコープコラボ", 0, 11], #45
    ["リッター4K", 7, 4], #46
    ["リッター4Kカスタム", 4, 7], #47
    ["4Kスコープ", 7, 4], #48
    ["4Kスコープカスタム", 4, 7], #49
    ["14式竹筒銃・甲", 8, 2], #50
    ["ソイチューバー",1 , 1], #51
    ["ソイチューバーカスタム", 8, 0], #52
    ["ノヴァブラスター", 0, 6], #53
    ["ノヴァブラスターネオ", 7,11 ], #54
    ["ホットブラスター",10 , 1], #55
    ["ホットブラスターカスタム", 9, 0], #56
    ["ラピッドブラスター", 7, 10], #57
    ["ラピッドブラスターデコ", 1, 0], #58
    ["Rブラスターエリート", 10,4], #59
    ["ロングブラスター", 1, 4], #60
    ["クラッシュブラスター", 0, 3],#61 
    ["クラッシュブラスターネオ",8 , 2], #62
    ["バレルスピナー", 3, 3], #63
    ["バレルスピナー デコ", 5, 7], #64
    ["スプラスピナー", 2, 2], #65
    ["スプラスピナーコラボ",8 , 4], #66
    ["ハイドラント", 9, 1], #67
    ["バケットスロッシャー", 1, 2], #68
    ["バケットスロッシャーデコ", 3, 6],#69 
    ["ヒッセン", 2,5], #70
    ["ヒッセン・ヒュー", 0, 4], #71
    ["スクリュースロッシャー", 9, 3], #72
    ["スクリュースロッシャーネオ", 6, 10], #73
    ["パラシェルター",3 , 4], #74
    ["パラシェルターソレーラ", 9, 10], #75
    ["キャンピングシェルター", 4, 7], #76
    ["スパイガジェット", 7, 1]#77
]


    

@app.route('/')
def index():
    level = request.cookies.get('level')
    if level is None:
        level = "level1"

    if level == "level1":
        i = random.randint(0, 9)
    elif level == "level2":
        i = random.randint(0, 29)
    else:
        i = random.randint(0, len(weapon_list) - 1)

    if level == "level1":
        level = "Level1(10問から出題)"
    elif level == "level2":
        level = "Level2(30問から出題)"
    else:
        level = "Level3(全問から出題)"
        
    #武器
    weapon1 = random.randint(0, len(weapon_list) - 1)
    while(weapon1 == i):
        weapon1 = random.randint(0, len(weapon_list) - 1)

    weapon2 = random.randint(0, len(weapon_list) - 1)
    while(weapon2 == i or weapon2 == weapon1):
        weapon2 = random.randint(0, len(weapon_list) - 1)

    #サブ
    i_sub = weapon_list[i][1]

    sub1 = random.randint(0, len(sub_list) - 1)
    while(sub1 == i_sub):
        sub1 = random.randint(0, len(sub_list) - 1)

    sub2 = random.randint(0, len(sub_list) - 1)
    while(sub2 == i_sub or sub2 == sub1):
        sub2 = random.randint(0, len(sub_list) - 1)

    #スペシャル
    i_sp = weapon_list[i][2]

    sp1 = random.randint(0, len(sp_list) - 1)
    while(sp1 == i_sp):
        sp1 = random.randint(0, len(sp_list) - 1)

    sp2 = random.randint(0, len(sp_list) - 1)
    while(sp2 == i_sp or sp2 == sp1):
        sp2 = random.randint(0, len(sp_list) - 1)

    tmp0 = [i, weapon1, weapon2]
    tmp1 = [i_sub, sub1, sub2]
    tmp2 = [i_sp, sp1, sp2]

    random.shuffle(tmp0)
    random.shuffle(tmp1)
    random.shuffle(tmp2)


    winlose = request.cookies.get('winLose')
    if winlose is None:
        winlose = "00000000000000000000"
    
    latest20 = getLatest20(winlose)
    renzoku = getRenzoku(winlose)

    return render_template('index.html',
        weapon=weapon_list[i][0],
        weapon_one=weapon_list[tmp0[0]][0],
        weapon_two=weapon_list[tmp0[1]][0],
        weapon_three=weapon_list[tmp0[2]][0],
        sub_one=sub_list[tmp1[0]],
        sub_two=sub_list[tmp1[1]],
        sub_three=sub_list[tmp1[2]],
        sp_one=sp_list[tmp2[0]],
        sp_two=sp_list[tmp2[1]],
        sp_three=sp_list[tmp2[2]],
        i=i,
        latest20=latest20,
        renzoku=renzoku,
        level=level)

def getLatest20(winlose):
    ret = 0
    for i in range(len(winlose)):
        if winlose[i] == "1":
            ret = ret + 1
    return ret/20.0*100

def getRenzoku(winlose):
    ret = 0
    t = winlose[::-1]
    for i in range(len(t)):
        if t[i] == "1":
            ret = ret + 1
        else:
            break
    return ret


@app.route('/setting', methods=['GET'])
def set_():
    level = request.cookies.get('level')
    if level is None:
        level = "level1"    
    return render_template("setting.html",level=level)

@app.route('/setting', methods=['POST'])
def setting():
    t1 = request.form['trigger']
    res = make_response(redirect('/'))

    res.set_cookie('level', t1)

    return res 

@app.route('/', methods=['POST'])
def form():
    t0 = request.form['trigger0']
    t1 = request.form['trigger']
    t2 = request.form['trigger2']
    i =  int(request.form['i'])

    winlose = request.cookies.get('winLose')
    if winlose is None:
        winlose = "00000000000000000000" 
    winlose = winlose[1:]
    if t0 == weapon_list[i][0] and t1 == sub_list[weapon_list[i][1]] and t2 == sp_list[weapon_list[i][2]]:
        winlose = winlose + "1"
    else:
        winlose = winlose + "0"        

    latest20 = getLatest20(winlose)
    renzoku = getRenzoku(winlose)

    level = request.cookies.get('level')
    if level is None:
        level = "level1"

    if level == "level1":
        level = "Level1(10問から出題)"
    elif level == "level2":
        level = "Level2(30問から出題)"
    else:
        level = "Level3(全問から出題)"

    res = make_response(render_template('result.html',
        weapon=weapon_list[i][0], 
        your_ans_weapon=t0,   
        your_ans_sub=t1,
        correct_ans_sub=sub_list[weapon_list[i][1]],
        your_ans_sp=t2,
        correct_ans_sp=sp_list[weapon_list[i][2]],
        i=i,
        latest20=latest20,
        renzoku=renzoku,
        level=level,
        sub_id=weapon_list[i][1],
        sp_id=weapon_list[i][2],
        ))

    res.set_cookie('winLose', winlose)
    return res

if __name__ == '__main__':
    app.debug = True
    #app.run(host='localhost')
    app.run(debug=False, host='0.0.0.0', port=80)