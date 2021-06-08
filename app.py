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
    return render_template("index.html")

@app.route('/diary')
def listing():
    diaries = list(db.articles.find({}, {'_id': False}))
    return jsonify({'all_articles': diaries})

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
    return render_template('login.html')
    
@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
