# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://sahitest.com/demo/selectTest.htm")
sleep(2)
select = Select(driver.find_element(By.ID, "s1"))
# 根据index下标获取，从0开始
select.select_by_index(1)
# 根据option的value进行选择
# select.select_by_value("51")
#根据实际看到的内容进行选择
# select.select_by_visible_text("Cell Phone")
sleep(5)
driver.close()
