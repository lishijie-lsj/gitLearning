# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/cascader")
sleep(2)
driver.find_element(By.XPATH,"//input[@class='ivu-input ivu-input-default']").click()
sleep(2)
driver.find_element(By.XPATH,'//li[contains(text(),"北京")]').click()
sleep(3)
driver.find_element(By.XPATH,'//li[contains(text(),"王府井")]').click()
sleep(5)
driver.close()
