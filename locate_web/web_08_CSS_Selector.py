# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com")
# 根据ID定位
# driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")
# driver.find_element(By.CSS_SELECTOR, "#su").click()

# 根据class属性值定位
# driver.find_element(By.CSS_SELECTOR, ".nav-search-input").send_keys("2024好运")
# 根据name属性值定位
# driver.find_element(By.CSS_SELECTOR,"[name='wd']").send_keys("selenium")
# 根据标签属性定位
# driver.find_element(By.CSS_SELECTOR,"a[href='http://image.baidu.com/']").click()
# 模糊匹配-包含
# driver.find_element(By.CSS_SELECTOR,"a[href*='http://image.baidu.com']").click()
# 模糊匹配-匹配开头
# driver.find_element(By.CSS_SELECTOR,"a[href^='http://image.baidu.com']").click()
# 模糊匹配-匹配结尾
# driver.find_element(By.CSS_SELECTOR, "a[href$='image.baidu.com/']").click()
# 组合定位
# driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys("selenium")

# 定位子元素
# driver.find_element(By.CSS_SELECTOR, "div#s-top-left>a").click()
# driver.find_element(By.CSS_SELECTOR, "#s-top-left>a").click()
# driver.find_element(By.CSS_SELECTOR, "div.s-top-left-new.s-isindex-wrap>a").click()

# 打开地图
# driver.find_element(By.CSS_SELECTOR, "div.s-top-left-new.s-isindex-wrap>a:nth-child(3)").click()
# 打开贴吧
# driver.find_elements(By.CSS_SELECTOR, "div#s-top-left>a")[3].click()
# 打开新闻
# driver.find_element(By.CSS_SELECTOR, "div#s-top-left>a:first-child").click()
# 打开贴吧
driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(4)").click()
sleep(5)
driver.close()
driver.quit()
