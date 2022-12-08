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
for i in range(len(remove_list)):
    nope = remove_list[i]
    j = list.count(nope)
    while j > 0:
        list.remove(nope)
        j = j-1
'''

# 텍스트 임의 변경
translate_list=[[['크롤','롤링'],'크롤링'],[['테이블'],'스테이블']]
for i in range(len(translate_list)):
    for j in range(len(translate_list[i][0])):
        nope = translate_list[i][0][j]
        yeap = translate_list[i][1]
        k = list.count(nope)
        while k > 0:
            list.remove(nope)
            list.append(yeap)
            k = k-1


from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = Image.open('son.png') # 이미지 파일 읽어오기
mask = np.array(img) # 픽셀 값 배열 형태 변환

word_counts = Counter(list)
  
wordcloud = WordCloud(font_path='malgun',  background_color="white", colormap='Greens', width = 700, height = 700, random_state = 43, max_font_size=60, mask=mask).generate_from_frequencies(word_counts)

plt.figure(figsize = (6,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file('wordcloud.png')