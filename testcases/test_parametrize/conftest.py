# -*- coding:utf-8 -*-
# created by Mason Li
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("打开浏览器")
    return driver
