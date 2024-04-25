# -*- coding:utf-8 -*-
# created by Mason Li

import pytest


@pytest.fixture(scope="function",autouse=True)
def fixture1():
    print("我是前置步骤1。。。")
    return 1


@pytest.fixture(scope="function")
def fixture2():
    print("我是前置步骤2。。。")
    return 1


def test_fixture1(fixture1,fixture2):
    assert fixture1 == 1
    assert fixture2==1


def test_fixture2():
    assert 2 == 2


if __name__ == '__main__':
    pytest.main()
