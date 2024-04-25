# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://sahitest.com/demo/alertTest.htm")
sleep(2)
driver.find_element(By.NAME, 'b1').click()
sleep(2)
# 使用alert.text获取弹框的文字
print(driver.switch_to.alert.text)
# 点击确定
driver.switch_to.alert.accept()

sleep(5)
driver.close()
