#-*- coding:utf-8 -*-
# created by Mason Li
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_baidu():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    title=driver.title
    url=driver.current_url
    text=driver.find_element(By.CSS_SELECTOR,'a[href="http://news.baidu.com"]').text
    button_text=driver.find_element(By.ID,'su').get_attribute("value")
    # button_text=driver.find_element(By.ID,'su').get_property("value")
    print("button_text:"+button_text)
    assert title=="百度一下，你就知道"
    assert url=="https://www.baidu.com/"
    assert text=="新闻"
    assert button_text=="百度一下"