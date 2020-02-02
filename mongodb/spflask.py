from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
   return render_template('index.html')


## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   rank_receive = request.form['rank_give']
   rank_receive = int(rank_receive)

   star_receive = request.form['star_give']
   star_receive = int(star_receive)

   db.movies.update_one({'rank':rank_receive},{'$set':{'star':star_receive}})
   return jsonify({'result':'success'})


@app.route('/test', methods=['GET'])
def test_get():
   rank_receive = request.args.get('rank_give')
   rank_receive = int(rank_receive)
   movie_info = db.movies.find_one({'rank':rank_receive},{'_id':0})
   return jsonify({'result':'success', 'info': movie_info})


@app.route('/new', methods=['POST'])
def new_post():
    rank_receive = int(request.form['rank_give'])
    star_receive = request.form['star_give']
    title_receive = request.form['title_give']

    db.movies.insert_one({'rank': rank_receive, 'star': star_receive, 'title': title_receive})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
   app.run(port=5000,debug=True)