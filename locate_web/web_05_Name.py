# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element(By.NAME,"wd").send_keys("根据name属性定位")
sleep(3)
driver.close()
driver.quit()