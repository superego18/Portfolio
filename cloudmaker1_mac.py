import time
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
from konlpy.tag import Mecab
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from wordcloud import WordCloud

#파이썬 인터프리터 설정: shift+command+p => /usr/bin/python3 => Python 3.9.6 64-bit

# Constants
DELAY = 2
FONT = "NanumBarunGothicBold"
FONT_PATH = f"{FONT}.ttf"
MAX_FONT_SIZE = 150
MIN_FONT_SIZE = 5
MAX_WORDS = 5000
RANDOM_STATE = 43

# Initialize Chrome driver
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open URL
url = 'https://getliner.com/user-profile/7203684'
driver.get(url)
time.sleep(DELAY)

# Extract titles and contents
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
sec = soup.select_one('section.css-oi8mt1')
titles = [title.get_text() for title in sec.select('span.css-137vrda')]
contents = [content.get_text() for content in sec.select('span.css-dtt6h1')]

# Close Chrome driver
driver.quit()

# Extract words using Mecab
mecab = Mecab()
words = [word for line in titles + contents for word in mecab.nouns(line) if len(word) > 1]

# Generate word cloud
icon = Image.open('mask_img/Son.png')
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)

word_counts = Counter(words)

wordcloud = WordCloud(font_path=FONT_PATH, background_color="black", colormap='Blues',
                      random_state=RANDOM_STATE, max_font_size=MAX_FONT_SIZE,
                      min_font_size=MIN_FONT_SIZE, max_words=MAX_WORDS, mask=mask).generate_from_frequencies(word_counts)

# Display and save word cloud
plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show(block=False)
plt.pause(3)
plt.close()

wordcloud.to_file('wordcloud1_mac.png')
