from datetime import datetime
from flask import Flask, render_template, request
from flask.json import jsonify

app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.team35_db

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/diary')
def listing():
    articles = list(db.articles.find({}, {'_id':False}))
    return jsonify({'all_articles':articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    img_receive = request.form['image_give']
    place_receive = request.form['place_give']
    content_receive = request.form['content_give']

    today = datetime.now()
    postingTime = today.strftime('%Y.%m.%d %H:%M')

    doc = {
        'title': title_receive,
        'img' : img_receive,
        'place' : place_receive,
        'content': content_receive,
        'date': postingTime
    }
    db.articles.insert_one(doc)
    
    return jsonify({'msg': '당신은 우리와 함께 갈 수 있습니다'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
