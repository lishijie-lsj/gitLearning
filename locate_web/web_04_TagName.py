# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.bilibili.com")
driver.find_element(By.TAG_NAME,"input").send_keys("学习selenium")
sleep(3)
driver.close()
driver.quit()