# -*- coding:utf-8 -*-
# created by Mason Li

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sahitest.com/demo/iframesTest.htm")
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("666")
sleep(3)
# 用下标
# driver.switch_to.frame("iframe_id")
# driver.find_element(By.XPATH, '//span[text()="番剧"]').click()
# 用name
# driver.switch_to.frame("iframe_name")
# driver.find_element(By.XPATH, '//span[text()="番剧"]').click()

# 进入iframe
ele = driver.find_element(By.CSS_SELECTOR, "body>iframe")
driver.switch_to.frame(ele)

# 退出iframe,切换到上一级
driver.switch_to.parent_frame()

# 切换到主界面
driver.switch_to.default_content()
driver.find_element(By.ID, "checkRecord").clear()
driver.find_element(By.ID, "checkRecord").send_keys("777")

sleep(3)
driver.close()
