# -*- coding:utf-8 -*-
# created by Mason Li

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/MyAll/Study/WebAutoTest/HTML/iframe_test.html")
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("6666")
sleep(3)
# 用下标
# driver.switch_to.frame("iframe_id")
# driver.find_element(By.XPATH, '//span[text()="番剧"]').click()
# 用name
driver.switch_to.frame("iframe_name")
driver.find_element(By.XPATH, '//span[text()="番剧"]').click()

sleep(3)
driver.close()
