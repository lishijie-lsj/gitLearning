# -*- coding:utf-8 -*-
# created by Mason Li
import yaml

from utils.get_filepath import get_yaml_path
path=get_yaml_path()
print(path)
def read_yaml():
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

if __name__ == '__main__':
    print(read_yaml())