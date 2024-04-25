# -*- coding:utf-8 -*-
# created by Mason Li
import os


def get_logo_path():
    # print(os.path.realpath(__file__))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'file', 'AAlog.txt')
    return path

def get_file_path():
    # print(os.path.realpath(__file__))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'file')
    return file_path

def get_yaml_path():
    path=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data','data.yaml')
    return path

if __name__ == '__main__':
    print(get_file_path())
