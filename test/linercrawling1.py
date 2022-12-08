from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
'''
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
CHROMEDRIVER_PATH = './chromedriver.exe'
service = ChromeService(executable_path=CHROMEDRIVER_PATH)


driver = webdriver.Chrome(service=service, options=options)

delay=0.1

url = 'https://getliner.com/feeds/user/7203684?shareOption=profile'

# 라이너 접속
driver.get(url)

time.sleep(1)

'''
# 로그인 클릭
login_path='//*[@id="root"]/main/header/nav/section[2]/button[1]'
login_button = driver.find_element(By.XPATH,login_path)
login_button.click()

time.sleep(1)

input_id = driver.find_element(By.NAME, "email")
input_id.send_keys("fly_juice@naver.com")
input_id.submit()

time.sleep(1)

input_pw = driver.find_element(By.NAME, "password")
input_pw.send_keys("uptothesky1@")
input_pw.submit()

time.sleep(1)

pw_path = '//*[@id="local-password"]'
pw_button = driver.find_element(By.XPATH,login_path)
pw_button.click()

time.sleep(1)

login_path = '//*[@id="root"]/main/section/div[2]/article/div/div/form/button/span'
login_button = driver.find_element(By.XPATH,login_path)
login_button.click()

time.sleep(10)
'''

'''
prev_height = driver.execute_script("return document. body.scrollHeight")
while True:
	#첫번째로 스크롤 내리기
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	#시간대기
	time.sleep(2)
	#현재높이 저장
	current_height = driver.execute_script("return document. body.scrollHeight")
	#현재높이와 끝의 높이가 끝이면 탈출
	if current_height == prev_height:
		break
	#업데이트해줘서 끝낼 수 있도록
	prev_height == current_height

time.sleep(60)
'''