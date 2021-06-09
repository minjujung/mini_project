from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

#---------------------[app 설정]---------------------#
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"
SECRET_KEY = 'SPARTA'

#---------------------[db 연결]---------------------#
client = MongoClient('localhost', 27017)
db = client.team35_db

#---------------------[main page]---------------------#


@app.route('/')
def main():
    return render_template("index.html")

#---------------------[write page]---------------------#


@app.route('/write')
def write():
    return render_template("diary.html")


@app.route('/diary')
def listing():
    diaries = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles': diaries})


@app.route('/diary', methods=['POST'])
def save_diary():
    today = datetime.now()

    title_receive = request.form['title_give']
    if not title_receive:
        title_receive = today.strftime('%Y.%m.%d %H:%M')
    place_receive = request.form['place_give']
    if not place_receive:
        place_receive = '디폴트'
    content_receive = request.form['content_give']
    if not place_receive:
        place_receive = '디폴트'
    postingTime = today.strftime('%Y.%m.%d %H:%M')

    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    file = request.files["file_give"]

    if file:
        filename = f'file-{mytime}'
        extension = file.filename.split('.')[-1]
        save_to = f'static/articleIMGs/{filename}.{extension}'
        file.save(save_to)

        doc = {
            'title': title_receive,
            'file': f'{filename}.{extension}',
            'place': place_receive,
            'content': content_receive,
            'date': postingTime
        }
        db.articles.insert_one(doc)

    else:
        doc = {
            'title': title_receive,
            # 'img' : img_receive,
            'file': f'static/defaultImg.jpg',
            'place': place_receive,
            'content': content_receive,
            'date': postingTime
        }
        db.articles.insert_one(doc)

    return jsonify({'msg': '당신은 우리와 함께 갈 수 있습니다!'})

#---------------------[sign up page]---------------------#


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

#---------------------[login page]---------------------#


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


#---------------------[app 실행]---------------------#
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
