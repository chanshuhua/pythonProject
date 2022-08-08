#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：enqueue.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/14 17:50 
'''
class Queue():
    '''
    队列-顺序表-先进先出
    '''
    def __init__(self):
        self.__item = []

    def is_empty(self):
        '''
        判空操作 判断队列是否为空
        :return:
        '''
        return self.__item == []

    def enqueue(self,item):
        '''
        向队列中新增元素
        :param item:
        :return:
        '''
        self.__item.append(item)

    def dequeue(self):
        '''
        队列中删除最先进去的元素
        :return:
        '''
        self.__item.pop(0)

    def last(self):
        if self.__item == None:
            return None
        else:
            return self.__item[-1]

    def size(self):
        '''
        返回队列的个数
        :return:
        '''
        return len(self.__item)

    def travel(self):
        for i in self.__item:
            yield i
    def items(self):
        return self.__item

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("queue is :".format(q.items()))
    for i in q.travel():
        print(i)

    print("queue last item is :".format(q.last()))

    print("if queue is empty:{}".format(q.is_empty()))

    q.dequeue()
    print("after pop item:{}".format(q.items()))
