# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://element.eleme.cn/#/zh-CN/component/cascader")
# 同级弟弟元素
driver.find_element(By.XPATH, '//span[text()="默认" click 触发子菜单]/following-sibling::div/div').click()


sleep(3)
driver.close()
