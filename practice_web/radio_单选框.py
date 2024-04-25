# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/radio")
# driver.find_elements(By.XPATH, '//input[@type="radio"and@class="ivu-radio-input"]')[1].click()
# sleep(2)
# driver.find_elements(By.XPATH, '//input[@type="radio"and@class="ivu-radio-input"]')[2].click()
# sleep(2)
# driver.find_elements(By.XPATH, '//input[@type="radio"and@class="ivu-radio-input"]')[3].click()
# driver.find_element(By.XPATH, '//span[text()="Android"]').click()
# sleep(2)
# 文本等于定位
driver.find_element(By.XPATH, '//span[text()="Windows"]').click()
sleep(2)
# 同级哥哥定位
driver.find_element(By.XPATH, '//span[text()="Android"]/preceding-sibling::span/input').click()
sleep(3)
driver.close()
