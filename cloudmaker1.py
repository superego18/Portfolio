from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from collections import Counter

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://getliner.com/user-profile/7203684' # 지속적으로 url 바뀌는 거 확인
driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-146yy6b') # 지속적으로 sec 바뀌는 거 확인
titles = [title.get_text() for title in sec.select('span.css-137vrda')]
contents = [content.get_text() for content in sec.select('span.css-dtt6h1')]

driver.quit()

list=[]

from konlpy.tag import Okt

okt=Okt()

for title in titles:
    words = okt.nouns(title)
    words2 = [n for n in words if len(n) > 1]
    list.extend(words2)

for content in contents:
    words = okt.nouns(content)
    words2 = [n for n in words if len(n) > 1]
    list.extend(words2)

# 텍스트 임의 제거
'''
remove_list=['수','것']
for nope in remove_list:
    while nope in nouns:
        nouns.remove(nope)
'''

# 텍스트 임의 변경
translate_list = [['크롤', '크롤링'], ['롤링', '크롤링'], ['테이블', '스테이블'],['설제','제설제'],['메타','메타버스']]
for old, new in translate_list:
    while old in list:
        list.remove(old)
        list.append(new)
 # 텍스트 임의 제거
remove_list=['버스']
for unuse in remove_list:
    while unuse in list:
        list.remove(unuse)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

font = "fonts/NanumBarunGothicBold"
font_path = "%s.ttf" % font

# https://noanswercode.tistory.com/8 참고
icon = Image.open('mask_img\Son.png') # 이미지 파일 읽어오기
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask) # 픽셀 값 배열 형태 변환

word_counts = Counter(list)
  
wordcloud = WordCloud(font_path=font_path, background_color="black", colormap='Blues', random_state = 43, max_font_size=150, min_font_size=5, max_words=5000, mask=mask).generate_from_frequencies(word_counts)

plt.figure(figsize = (6,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# 2초 후 자동으로 닫게 하기
plt.show(block=False)
plt.pause(3) 
plt.close()

wordcloud.to_file('wordcloud_image\wordcloud1.png')