from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
CHROMEDRIVER_PATH = './chromedriver.exe'
service = ChromeService(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

delay=0.1

url = 'https://www.bobaedream.co.kr/'
driver.get(url)

time.sleep(1)

x_path='//*[@id="bobaeHead"]/div[2]/div/div[2]/ul/li[1]/button/span'
searchbox = driver.find_element(By.XPATH,x_path)

searchbox.click()

element = driver.find_element(By.NAME, "keyword")

element.send_keys("쏘렌토")
element.submit()

m_morebox = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div/a')
m_morebox.click()

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('div.content')
commu_list = search_result.select('td > a.title')

links = []
for commu in commu_list[:5]:
    link = commu['href']
    link = url + link      #href 형태가 보배드림 기본 url이 빠져있어 url 합침
    links.append(link)
print(links) 