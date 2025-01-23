pip install pyautogui

import pyautogui 

#마우스 위치 좌표
pyautogui.position()



##########################################
import xlwings as xw

app = xw.App(add_book=False)

wb = app.books.open('test.xlsx')

wb.sheets.add('newSheet1')
wb.sheets.add('newSheet2')
wb.sheets.add(name='test', before= 'newSheet1')




##########################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 크롬 옵션 설정
options = Options()
options.add_argument('--start-maximized')  # 전체 화면으로 열기

# 웹드라이버 인스턴스 생성 (옵션을 적용)
driver = webdriver.Chrome(options=options)

# URL 열기
url = "https://www.naver.com/"
driver.get(url)

# 검색 입력란에 '파이썬' 텍스트 입력
search_box = driver.find_element(By.CSS_SELECTOR, '.search_input')
search_box.send_keys('파이썬')
search_box.send_keys(Keys.ENTER)



##########################################
# 기본 설치 라이브러리
##########################################
pip install pyautogui
pip install selenium
pip install xlwings
pip install pandas
pip install datetime
pip install beautifulsoup4 #값 가져오기
pip install openai
pip install msoffcrypto-tool #비번걸린 엑셀 관리



##########################################
# GUI사용을 위한 모듈
##########################################
import pyautogui
import tkinter
from tkinter import messagebox
from tkinter import



##########################################
# Selenium사용을 위한 모듈
##########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



##########################################
# Selenium 항상 최신버전 유지
##########################################
iport os
os.system('pip install --upgrage selenium')
#코드의 상단에 위 코드 추가



##########################################
파이썬 셀레니움 요소 선택방법
##########################################
xpath = "//태그[@속성='속성값']
<div id = "site">
xpath = "//div[@id='site']"

# xpath의 형식 : '//태그[@속성="속성값"]'
xpath = '//input[@title="주문전송"]'
driver.find_element("xpath", xpath)



##########################################
# openAI 사용을 위한 모듈
##########################################
import os
os.environ["OPENAI_API_KEY] = "부여받은 key code"
from openai import OpenAI
client = OpenAI



##########################################
# r'string'으로 역슬러시 오류 방지 
##########################################
df = pd.read_csv(r'F:\파이썬\99.판다스\doit_pandas-master\data\gapminder.tsv', sep = '\t')


