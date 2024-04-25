# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/checkbox")
# 文本等于定位
# driver.find_element(By.XPATH, '//span[text()="香蕉"]').click()
# sleep(2)
# driver.find_element(By.XPATH, '//span[text()="苹果"]').click()
# sleep(2)
# driver.find_element(By.XPATH, '//span[text()="西瓜"]').click()
# sleep(2)
# 同级哥哥定位
driver.find_element(By.XPATH, '//span[text()="香蕉"]/preceding-sibling::span/input').click()
sleep(2)
driver.find_element(By.XPATH, '//span[text()="苹果"]/preceding-sibling::span/input').click()
sleep(2)
driver.find_element(By.XPATH, '//span[text()="西瓜"]/preceding-sibling::span/input').click()
sleep(3)
driver.close()
