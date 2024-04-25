# -*- coding:utf-8 -*-
# created by Mason Li
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.bilibili.com')
# 1.找到输入框的位置，发送软件测试老白
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys('软件测试老白')
# 2.找到搜索框的位置，点击搜索
driver.find_element(By.CLASS_NAME, 'nav-search-btn').click()
time.sleep(3)
driver.close()
