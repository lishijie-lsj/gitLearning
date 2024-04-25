# -*- coding:utf-8 -*-
# created by Mason Li
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from utils.read import read_yaml


@pytest.mark.parametrize("key", read_yaml()['skill'])
def test_baidu(driver, key):
    driver.get("https://www.baidu.com/")
    driver.find_element(By.ID, "kw").send_keys(key)
    driver.find_element(By.ID, "su").click()
    sleep(1)
