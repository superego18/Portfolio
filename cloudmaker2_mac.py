import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Configure Selenium options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver', options=options)

# Wait time for page loading
delay = 2

# URL to scrape
url = 'https://getliner.com/user-profile/7203684'

# Load URL in Selenium
driver.get(url)
time.sleep(delay)

# Parse HTML using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Extract collection data
sec = soup.select_one('section.css-auc73u')
tags = sec.select('li.css-zr54ay')

# Close Chrome driver
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

# Wait for 1 second
time.sleep(1)

# Define font and font path for the WordCloud
font = "NanumBarunGothicBold"
font_path = f"{font}.ttf"

# Define mask image for the WordCloud
icon = Image.open('mask_img/Apple_logo.png')
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)

# Generate WordCloud using WordCloud library
word_counts = collections
wordcloud = WordCloud(font_path=font_path, background_color="black", colormap='Reds', random_state=43,
                      max_font_size=150, min_font_size=5, max_words=5000, mask=mask).generate_from_frequencies(word_counts)

# Display the WordCloud
plt.figure(figsize=(6, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show(block=False)

# Wait for 3 seconds before automatically closing the window
plt.pause(3)
plt.close()

# Save the WordCloud image to a file
wordcloud.to_file('wordcloud2_mac.png')
