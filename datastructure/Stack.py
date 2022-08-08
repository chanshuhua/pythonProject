#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：Stack.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/14 15:51 
'''

class Stack():
    '''
    栈-顺序表-先进后出
    '''

    def __init__(self):
        '''
        定义空栈
        '''
        self.__items = []

    def is_empty(self):
        '''
        判断栈是否为空
        :return:
        '''
        return self.__items == []

    def push(self,item):
        '''
        添加一个新元素item到栈顶
        :return:
        '''
        self.__items.append(item)

    def pop(self):
        '''
        弹出一个栈顶元素并返回
        :return:
        '''
        return self.__items.pop(-1)

    def top(self):
        '''
        返回栈顶元素，有返回值
        :return:
        '''
        if self.is_empty():
            return None
        else:
            return self.__items[-1]
    def size(self):
        '''
        返回栈中的元素个数
        :return:
        '''
        return len(self.__items)

    def travel(self):
        '''
        遍历这个栈的元素
        :return:
        '''
        for i in self.__items:
            yield i
        # return stack.__items

    def items(self):
        return self.__items

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("stack is:{}".format(stack.items()))
    for i in stack.travel():
        print(i)

    print("stack top is:{}".format(stack.top()))
    print("if stack is empty:{}".format(stack.is_empty()))

    stack.pop()
    print("after pop item:")
    for i in stack.travel():
        print(i)




