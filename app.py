from datetime import datetime
from flask import Flask, render_template, request
from flask.json import jsonify

app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('54.180.114.126', 27017, username="test", password="test")
db = client.dbsparta_plus_week2
# client = MongoClient('localhost', 27017)
# db = client.team35_db

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/diary')
def listing():
    diaries = list(db.diary.find({}, {'_id': False}))
    return jsonify({'all_articles': diaries})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
