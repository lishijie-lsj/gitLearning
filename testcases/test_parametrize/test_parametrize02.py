# -*- coding:utf-8 -*-
# created by Mason Li
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from utils.read import read_yaml


# @pytest.mark.parametrize("data", read_yaml()['userinfos'])
# def test_baidu(driver, data):
#     driver.get("http://sellshop.5istudy.online/sell/user/login_page")
#     driver.find_element(By.ID, "username").send_keys(data['username'])
#     driver.find_element(By.ID, "password").send_keys(data['password'])
#     driver.find_element(By.CSS_SELECTOR,'#login > form > p.login.button > input[type=submit]').click()
#     sleep(1)
@pytest.mark.parametrize("username,password", read_yaml()['userinfo_list'])
def test_login(driver,username,password):
    driver.get("http://sellshop.5istudy.online/sell/user/login_page")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'#login > form > p.login.button > input[type=submit]').click()
    if username=='admin':
        text=driver.find_element(By.CSS_SELECTOR,'body > div > div > div > div > strong').text
        assert text=="用户不存在"
    sleep(2)

