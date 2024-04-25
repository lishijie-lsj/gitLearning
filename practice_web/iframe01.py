# -*- coding:utf-8 -*-
# created by Mason Li

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/iframesTest.htm")
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("6666")
sleep(3)
# 用下标
driver.switch_to.frame(1)
driver.find_element(By.ID, 'open-self').click()
sleep(3)
driver.close()
