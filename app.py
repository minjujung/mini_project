from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'
client = MongoClient('localhost', 27017)
db = client.team35_db


@app.route('/')
def main():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return render_template("index.html")

@app.route('/write')
def write():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('diary.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return render_template("index.html")

@app.route('/diary', methods=['POST'])
def save_diary():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        title_receive = request.form['title_give']
        img_receive = request.form['image_give']
        place_receive = request.form['place_give']
        content_receive = request.form['content_give']

        today = datetime.now()
        postingTime = today.strftime('%Y.%m.%d %H:%M')

        doc = {
            'username': user_info["username"],
            'title': title_receive,
            'img' : img_receive,
            'place' : place_receive,
            'content': content_receive,
            'date': postingTime
        }
        db.articles.insert_one(doc)
        return jsonify({"result": "success",'msg': '당신은 우리와 함께 갈 수 있습니다'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return render_template("index.html")

@app.route('/diary', methods=["GET"])
def listing():
    token_receive = request.cookies.get('mytoken')
    if token_receive:
        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            diaries = list(db.articles.find({}))
            for diary in diaries:
                diary["_id"] = str(diary["_id"])
                diary["count_heart"] = db.likes.count_documents({"post_id": diary["_id"], "type": "heart"})
                diary["heart_by_me"] = bool(db.likes.find_one({"post_id": diary["_id"], "type": "heart", "username": payload['id']}))
            return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "all_articles": diaries})
        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return render_template("index.html")    
    else:
        diaries = list(db.articles.find({}, {'_id': False}))
    return jsonify({"result": "noheart", 'all_articles': diaries})

@app.route('/update_like', methods=['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        diary_id_receive = request.form["diary_id_give"]
        type_receive = request.form["type_give"]
        action_receive = request.form["action_give"]
        doc = {
            "diary_id": diary_id_receive,
            "username": user_info["username"],
            "type": type_receive
        }
        if action_receive =="like":
            db.likes.insert_one(doc)
        else:
            db.likes.delete_one(doc)
        count = db.likes.count_documents({"diary_id": diary_id_receive, "type": type_receive})
        return jsonify({"result": "success", 'msg': 'updated', "count": count})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return render_template("index.html")

@app.route('/sign_up')
def signUp():
    # msg = request.args.get("msg")
    return render_template('signup.html')


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(
        password_receive.encode('utf-8')).hexdigest()
    nickname_receive = request.form['nickname_give']
    doc = {
        "username": username_receive,                               # 아이디
        "nickname": nickname_receive,                                # 닉네임
        "password": password_hash                                  # 비밀번호
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})




@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():

    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

    
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
