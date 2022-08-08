#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：xmind_toexcel.py.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/8/5 0:32 
'''
import time
from xmindparser import xmind_to_dict
import xlwt

class xmind2excel:
    excel_name = 'default_name'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def __init__(self,xmindFilePath):
        try:
            self.create_excel()
            self.input_data(self.newExcel,self.newSheet,0, 0, "")
            self.input_data(self.newExcel,self.newSheet,1, 0, "行1")
            self.input_data(self.newExcel,self.newSheet, 0, 1, "列1")
            self.content_data = self.readXmind(xmindName=xmindFilePath)
            self.newExcel.save(excel_name+'.xlsx')
            print("init_content complete!!")
        except Exception:
            print("请查看该路径下是否已生成同名文件！")

    def create_excel(self):
        # 新建工作簿
        self.newExcel = xlwt.Workbook()
        # 新建一个sheet
        self.newSheet = self.newExcel.add_sheet('xmind1', cell_overwrite_ok=True)
        return self.newExcel, self.newSheet

    def input_data(self, newExcel, newSheet, row=1, col=1, label="labelname"):
        newSheet.write(row, col, label)

    def readXmind(self,xmindName):
        global excel_name
        global topic
        excel_name = xmind_to_dict(xmindName)[0]['topic']['title']
        # print(len(xmind_to_dict(xmindName)[0]['topic']['topics']))
        return xmind_to_dict(xmindName)[0]['topic']['topics']  # xmind内容

    def get_child_topic(self,title):
        print(self.content_data)
        for i in range(len(self.content_data)):
            tmp = self.content_data[i]
            print(tmp)



if __name__ == '__main__':
    xmind2excel(r'C:\Users\chan\Desktop\系统设置.xmind').get_child_topic("阈值管理")

