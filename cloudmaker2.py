import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://getliner.com/user-profile/7203684' # 지속적으로 url 바뀌는 거 확인
driver.get(url)

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-auc73u')
tags = sec.select('li.css-zr54ay')
driver.quit()

collections = {}
for tag in tags:
    attr = tag['data-folder-data']
    name = re.findall('"name":"(.*?)",', attr)[0]
    page = re.findall('"savedPageCount":(.*?)}', attr)[0]
    page = int(page)
    if ', ' in name:
        names = name.split(', ')
        for n in names:
            collections[n] = page
    else:
        collections[name] = page

time.sleep(1)
font = "fonts/NanumBarunGothicBold"
font_path = f"{font}.ttf"

icon = Image.open('mask_img/Apple_logo.png')
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)

word_counts = collections
wordcloud = WordCloud(font_path=font_path, background_color="black", colormap='Reds', random_state=43, max_font_size=150, min_font_size=5, max_words=5000, mask=mask).generate_from_frequencies(word_counts)

plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")

plt.show(block=False)
plt.pause(3)
plt.close()
wordcloud.to_file('wordcloud_image/wordcloud2.png')