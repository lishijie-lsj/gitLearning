# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.get_filepath import get_logo_path
driver_path = r'D:\install\Python\Python39\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")
sleep(2)
# 获取input文件上传元素
upload=driver.find_element(By.ID,'file')
path=get_logo_path()
upload.send_keys(r"{}".format(path))
driver.find_element(By.NAME,'submit').click()
sleep(5)
driver.close()
