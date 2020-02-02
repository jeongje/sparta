import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')


musics = soup.select('.list-wrap > tbody > .list')

# 테스트
# rank = musics[0].select_one('td.number').text.strip()
# title = musics[0].select_one('td.info > a.title.ellipsis').text.strip()
# artist = musics[0].select_one('td.info > a.artist.ellipsis').text.strip()

def select_strip(music, txt):
    return music.select_one(txt).text.strip()

rank = 1
for music in musics:
    title = select_strip(music, 'td.info > a.title.ellipsis')
    artist = select_strip(music, 'td.info > a.artist.ellipsis')

    doc = {
        'rank': rank,
        'title': title,
        'artist': artist,
    }

    db.genie.insert_one(doc)
    rank +=1

results = list(db.genie.find({}))

for result in results:
    print(result)


