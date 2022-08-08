#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：json_check.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/7/7 20:02 
'''
jsondata = {"person": {"name": "pig","age": "18","sex": "man","hometown":[ {"province": "江西省","city": "抚州市","county": "崇仁县" },
                                                                           {"province": "广东省","city": "深圳市","county": "宝安区" } ] }}

if __name__ == '__main__':
    hh = jsondata["person"]["hometown"]
    for i in hh:
        if i.get("province") == "广东省":
            print(i)
    for h in hh:
        for key,value in h.items():
            if value == "广东省":
                 print(h)