pip install pyautogui

import pyautogui 

#마우스 위치 좌표
pyautogui.position()




import xlwings as xw

app = xw.App(add_book=False)

wb = app.books.open('test.xlsx')

wb.sheets.add('newSheet1')
wb.sheets.add('newSheet2')
wb.sheets.add(name='test', before= 'newSheet1')





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
