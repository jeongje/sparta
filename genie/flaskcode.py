from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
    rank_receive = request.args.get('rank_give')
    rank_receive = int(rank_receive)
    genie_info = db.genie.find_one({'rank':rank_receive},{'_id':0})
    return jsonify({'result':'success', 'info':genie_info})

if __name__ == '__main__':
    app.run(port=5000,debug=True)