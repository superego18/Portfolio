from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from bs4 import BeautifulSoup
from collections import Counter

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
CHROMEDRIVER_PATH = './chromedriver.exe'
service = ChromeService(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

delay=0.1

url = 'https://getliner.com/feeds/user/7203684?shareOption=profile'

driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-0')
titles = sec.select('div.css-w3af2n > h2.css-o7qmg8')
contents = sec.select('div.css-w3af2n > section > section > div > section > div > div > div > p')

time.sleep(1)

list=[]

from konlpy.tag import Okt

okt=Okt()

for title in titles:
    line1 = title.get_text()
    words = okt.nouns(line1)
    words2 = [n for n in words if len(n) > 1]
    list.extend(words2)

for content in contents:
    line2 = content.get_text()
    words = okt.nouns(line2)
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

font = "NanumBarunGothicBold"
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

wordcloud.to_file('wordcloud2.png')