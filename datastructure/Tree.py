#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：Tree.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/22 22:36 
'''


class Node():
    def __init__(self,item,lchild=None,rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    def __init__(self):
        self.root = Node()
        self.treeQueue = []

    def add(self,tree):
        '''
        添加节点
        :param tree:
        :return:
        '''
        treeNode = Node(tree)
        # 根节点为空
        if self.root is None:
            self.root = treeNode
            self.treeQueue.append(self.root)
        else:
            # 根节点不为空，左子树为空
            # 根节点不为空，右子树为空
            # 遍历查找
            rootQueue = self.treeQueue[0]
            if rootQueue.lchild is None:
                rootQueue.lchild = treeNode
                self.treeQueue.append(treeNode.item)
            else:
                rootQueue.rchild = treeNode
                rootQueue.append(treeNode.item)
                self.treeQueue.pop(0)


