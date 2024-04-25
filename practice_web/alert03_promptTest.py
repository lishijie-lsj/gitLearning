# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")
sleep(2)
driver.find_element(By.ID, 'file').click()
sleep(2)
driver.switch_to.alert.send_keys("测试alert")
sleep(2)
# 点击确定
driver.switch_to.alert.accept()
# 点击取消
# driver.switch_to.alert.dismiss()
sleep(5)
driver.close()
