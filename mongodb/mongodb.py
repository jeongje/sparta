from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# db.users.insert_one({'name':'bobby', 'age':21})
# db.users.insert_one({'name':'kay', 'age':27})
db.users.insert_one({'name':'john', 'age':33})

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({}))

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age':21}))

# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
    # print(user)

# user = db.users.find_one({'name':'bobby'},{'age':1})
# print (user)

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})