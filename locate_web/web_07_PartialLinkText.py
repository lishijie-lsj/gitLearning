# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 模糊查询，只定位可点击的a标签

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com")
# 部分匹配文本值
# driver.find_element(By.PARTIAL_LINK_TEXT,"闻").click()
driver.find_elements(By.PARTIAL_LINK_TEXT, "新闻")[0].click()
sleep(3)
driver.close()
driver.quit()
