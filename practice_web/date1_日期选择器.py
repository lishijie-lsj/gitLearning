# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/date-picker")
sleep(2)
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix" ]').send_keys('2024-04-24')
sleep(2)
driver.find_elements(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix" ]')[1].send_keys('2024-04-24-2024-05-31')

sleep(5)
driver.close()
