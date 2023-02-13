import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from konlpy.tag import Okt
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from collections import Counter
# from memory_profiler import profile
from konlpy.tag import Mecab

# JVM_PATH = '/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/lib'

# driver = webdriver.Firefox()

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# # # 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

# # options = webdriver.ChromeOptions()
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option("useAutomationExtension", False)
# # CHROMEDRIVER_PATH = './chromedriver.exe'
# # service = ChromeService(executable_path=CHROMEDRIVER_PATH)

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# def set_chrome_driver():
#     chrome_options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     return driver
# driver = set_chrome_driver()
# webdriver.Chrome("/opt/homebrew/bin/chromedriver")

delay = 2

url = 'https://getliner.com/user-profile/7203684'

driver.get(url)

time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-oi8mt1')
titles = sec.select('span.css-137vrda')
contents = sec.select('span.css-dtt6h1')

time.sleep(2)

driver.quit()

list = []

mecab = Mecab()

'''
jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home"

# FileNotFoundError: [Errno 2] JVM DLL not found: /Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home

okt = Okt(jvmpath=jvm_path)
'''

for title in titles:
    line1 = title.get_text()
    words = mecab.nouns(line1)
    words2 = [n for n in words if len(n) > 1]
    list.extend(words2)


for content in contents:
    line2 = content.get_text()
    words = mecab.nouns(line2)
    words2 = [n for n in words if len(n) > 1]
    list.extend(words2)

'''
# 텍스트 임의 변경
translate_list = [['크롤', '크롤링'], ['롤링', '크롤링'], [
    '테이블', '스테이블'], ['설제', '제설제'], ['메타', '메타버스']]
for old, new in translate_list:
    while old in list:
        list.remove(old)
        list.append(new)
 # 텍스트 임의 제거
remove_list = ['버스']
for unuse in remove_list:
    while unuse in list:
        list.remove(unuse)
'''

font = "NanumBarunGothicBold"
font_path = "%s.ttf" % font

# https://noanswercode.tistory.com/8 참고
icon = Image.open('mask_img/Son.png')  # 이미지 파일 읽어오기
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)  # 픽셀 값 배열 형태 변환

word_counts = Counter(list)

wordcloud = WordCloud(font_path=font_path, background_color="black", colormap='Blues', random_state=43,
                      max_font_size=150, min_font_size=5, max_words=5000, mask=mask).generate_from_frequencies(word_counts)

plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# 2초 후 자동으로 닫게 하기
plt.show(block=False)
plt.pause(3)
plt.close()

wordcloud.to_file('wordcloud1_mac.png')
