import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from bs4 import BeautifulSoup
# from collections import Counter

options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# CHROMEDRIVER_PATH = './chromedriver.exe'
# service = ChromeService(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome('chromedriver', options=options)

delay = 2

url = 'https://getliner.com/user-profile/7203684'

driver.get(url)

time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-auc73u')
tags = sec.select('li.css-zr54ay')


collections = {}
for tag in tags:
    attr = tag['data-folder-data']  # type = str
    # attr = attr.rstrip # 우공백 지우기 -> 하면 다 지워짐
    # type(attr) = str
    # 결과 예시
    # {"id":7382319,"name":"헬스케어 스타트업","emoji":null,"order":13,"status":"normal","description":"","openState":"public","hashKey":"NzM4MjMxOQ==","savedPageCount":1,"viewCount":0}
    # => 정규표현식으로 해결해보자!
    name = re.findall('"name":"(.*?)",', attr)[0]
    page = re.findall('"savedPageCount":(.*?),', attr)[0]
    page = int(page)
    split_str = ', '
    if split_str in name:
        split_list = name.split(', ')
        for n in split_list:
            name = n
            collections[name] = page
    else:
        collections[name] = page

time.sleep(1)


font = "NanumBarunGothicBold"
font_path = "%s.ttf" % font

# https://noanswercode.tistory.com/8 참고
icon = Image.open('mask_img/Apple_logo.png')  # 이미지 파일 읽어오기
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)  # 픽셀 값 배열 형태 변환

word_counts = collections

wordcloud = WordCloud(font_path=font_path, background_color="black", colormap='Reds', random_state=43,
                      max_font_size=150, min_font_size=5, max_words=5000, mask=mask).generate_from_frequencies(word_counts)

plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# 2초 후 자동으로 닫게 하기
plt.show(block=False)
plt.pause(3)
plt.close()

wordcloud.to_file('wordcloud2_mac.png')
