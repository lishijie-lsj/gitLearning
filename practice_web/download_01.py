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

file = get_file_path()+"/LATEST_RELEASE"
if os.path.exists(file):
    print("文件存在")
    os.remove(file)
    print("文件已删除")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://registry.npmmirror.com/binary.html?path=chromedriver/")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/table/tbody/tr[156]/td[2]/a').click()
time.sleep(3)
# 假设你知道下载文件的名称，这里以'example.pdf'为例
download_filename = 'LATEST_RELEASE'
# 默认下载目录（这取决于你的操作系统和浏览器设置）
filepath = get_file_path()
default_download_dir = "C:\\Users\\67281\\Downloads"
# 指定的目标文件夹
target_dir = filepath

# 构建文件的完整路径
source_path = os.path.join(default_download_dir, download_filename)
target_path = os.path.join(target_dir, download_filename)

# 确保目标文件夹存在
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 移动文件到目标文件夹
try:
    shutil.move(source_path, target_path)
    print(f"File moved to {target_path}")
except FileNotFoundError:
    print(f"File {download_filename} not found in {default_download_dir}")
except Exception as e:
    print(f"Error moving file: {e}")
driver.close()
