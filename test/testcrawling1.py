import requests
from bs4 import BeautifulSoup

search_word = '선풍기'

#사용할 고정 url을 선언한다.
url = 'https://search.shopping.naver.com/search/all?query=%EC%84%A0%ED%92%8D%EA%B8%B0&cat_id=&frm=NVSHATC'

#requests.get()함수를 사용하여 해당 url을 사용 친화적으로 만든다.
req = requests.get(url)

#Requests_text 함수를 이용하여 현재 접속된 url 정보를 html로 BeautifulSoup에 넘김
html = req.text
#BeautifulSoup()함수를 사용하여 html을 parsing 한다.
#이러면, 해당 웹사이트에서 F12을 눌러 html을 열람한 후, 원하는 기능을 수행하면 된다.
soup = BeautifulSoup(html, 'html.parser')

#선풍기 상품 리스트는 select_one() 함수로 추출한다.
search_result = soup.select_one('div.style_content_wrap__Cdqnl')

#위의 이미지대로 차례차례 내려간다.
shop_list = search_result.select('div.basicList_title__VfX3c > a')

links = []
for shop in shop_list[:5]:
    link = shop['href']  # a에서 웹사이트 url 정보를 추출해준다.
    links.append(link)

print(links)  # 네이버 쇼핑 선풍기 페이지에 있는 5개의 선풍기 웹사이트 정보를 출력해준다.
