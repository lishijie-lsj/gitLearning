# -*- coding:utf-8 -*-
# created by Mason Li
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("https://www.baidu.com")
# 绝对路径
# driver.find_element(By.XPATH, '/html/body/div/div/div[3]/a').click()
# 根据ID定位
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys("selenium")
# 根据class定位
# driver.find_element(By.XPATH,"//input[@class='s_ipt']").send_keys("selenium")
# 根据name定位
# driver.find_element(By.XPATH,"//input[@name='wd']").send_keys("selenium")

# 多个属性组合定位
# driver.find_element(By.XPATH,"//input[@class='s_ipt'and @name='wd'and @autocomplete='off']").send_keys("selenium")

# 根据多组数据使用下标定位
# driver.find_element(By.XPATH, "//div[@id='s-top-left']/a[4]").click()

# 通过子元素找父元素
# driver.find_element(By.XPATH, "//div[@id='s-top-left']/../div[3]").click()

# 根据span文本内容定位,文本等于
# driver.find_element(By.XPATH, "//span[text()='习近平在重庆考察调研']").click()

# 通根据文本包含
# driver.find_element(By.XPATH, "//span[contains(text(),'央视')]").click()

#根据同级弟弟定位(同级向下)
# driver.find_element(By.XPATH,'//a[contains(text(),"贴吧" )and @class="mnav c-font-normal c-color-t"]/following-sibling::a[2]').click()

#根据哥哥定位（同级向上）
driver.find_element(By.XPATH,'//a[contains(text(),"贴吧" )and @class="mnav c-font-normal c-color-t"]/preceding-sibling::a[1]').click()
sleep(3)
driver.close()
