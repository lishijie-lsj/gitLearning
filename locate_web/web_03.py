# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.bilibili.com")
# driver.find_element(By.CLASS_NAME,"nav-search-input").send_keys("2024好运")
# driver.find_element(By.CLASS_NAME,"channel-link").click()
# channel_lst=driver.find_elements(By.CLASS_NAME,"channel-link")
# for ele in channel_lst:
#    print(ele.text)
sleep(3)
