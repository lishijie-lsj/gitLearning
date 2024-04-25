# -*- coding:utf-8 -*-
# created by Mason Li
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.get_filepath import *

file=get_file_path()+"/LATEST_RELEASE"
if os.path.exists(file):
    print("文件存在")
    os.remove(file)
    print("文件已删除")

chromeOptions= webdriver.ChromeOptions()
prefs={"download.default_directory":"{}".format(get_file_path())}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a').click()
time.sleep(3)

driver.close()
