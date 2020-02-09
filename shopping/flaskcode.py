from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['GET'])
def orders_view():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders':orders})


@app.route('/order', methods=['POST'])
def order_save():
    name_recieve = request.form['name_give']
    quantity_recieve = request.form['quantity_give']
    address_recieve = request.form['address_give']
    phone_recieve = request.form['phone_give']

    order = {'name': name_recieve, 'quantity': quantity_recieve, 'address': address_recieve, 'phone': phone_recieve}

    db.orders.insert_one(order)

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(port=5000,debug=True)