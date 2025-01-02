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
