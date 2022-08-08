#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：BinaryTree.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/5/21 18:59 
'''

class BiNode():
    def __init__(self,item,lchild=None,rchild=None):
        '''
        定义树节点
        '''
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class BiTreeOrder():
    # def __init__(self,root):
    #     self.root = root

    def preorder(self,node):
        '''
        递归实现先序遍历
        先序遍历：在先序遍历中，我们先访问根节点，然后递归使用先序遍历访问左子树，再递归使用先序遍历访问右子树
        :param root:
        :return:
        '''
        if node is None:
            return
        print(node.item)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def preorder_func1(self,root):
        '''
        非递归线性遍历：采用临时遍历保存中间结构，用循环结构代替递归过程，利用栈保存中间结果
        利用栈结构通过回溯访问二叉树的每个节点
        :param node:
        :return:
        '''
        cur = root
        stack = []
        list = []
        stack.append(cur)
        while stack:
            cur = stack.pop(-1)
            # print(cur.item)
            list.append(cur.item)
            while cur:
                if cur.lchild:
                    # print(cur.lchild.item)
                    list.append(cur.lchild.item)
                if cur.rchild:
                    stack.append(cur.rchild)
                cur = cur.lchild
        return list

    def inorder(self,node):
        '''
        递归实现中序遍历
        中序遍历：先遍历左子树，在访问根节点，在遍历右子树
        :param node:
        :return:
        '''
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item)
        self.inorder(node.rchild)

    def backorder(self,node):
        '''
        递归实现后序遍历
        后序遍历：先遍历左子树，在遍历右子树，最后访问根节点
        :param node:
        :return:
        '''
        if node is None:
            return
        self.backorder(node.lchild)
        self.backorder(node.rchild)
        print(node.item)


class stack_order():


    def pre_stack_order(self,root):
        '''
        栈实现先序遍历
        根-左-右
        :return:
        '''
        mystack = []
        if root is None:
            return
        else:
            # 根节点开始遍历
            node = root
            # 栈和节点不为空
            while node or mystack:
                while node:
                    print(node.item)
                    mystack.append(node)
                    node = node.lchild
                node = mystack.pop(-1)
                node = node.rchild

    def in_stack_order(self,root):
        '''
        栈实现中序遍历
        左-根-右
        :param root:
        :return:
        '''
        mystack = []
        if root is None:
            return
        else:
            node = root
            while node or mystack:
                while node:
                    mystack.append(node)
                    node = node.lchild
                node = mystack.pop(-1)
                print(node.item)
                node = node.rchild

    def back_stack_order(self,root):
        '''
        双栈实现后序遍历 （超级好理解）
        左-右-根()
        :param root:
        :return:
        '''
        stack1 = []
        stack2 = []
        if root is None:
            return
        else:
            stack1.append(root)
            while stack1:
                node = stack1.pop(-1)
                stack2.append(node)
                if node.lchild:
                    stack1.append(node.lchild)
                if node.rchild:
                    stack1.append(node.rchild)
            while stack2:
                node = stack2.pop(-1)
                print(node.item)


        def back_stack_order2(root):
            '''
            单栈实现后序遍历
            :param root:
            :return:
            '''
            if root is None:
                return





if __name__ == '__main__':
    aNode = BiNode('a')
    bNode = BiNode('b')
    cNode = BiNode('c')
    aNode.lchild = bNode
    aNode.rchild = cNode
    dNode = BiNode('d')
    eNode = BiNode('e')
    bNode.lchild = dNode
    bNode.rchild = eNode
    fNode = BiNode('f')
    cNode.lchild = fNode

    # stack_order().pre_stack_order(aNode)
    # stack_order().in_stack_order(aNode)

    # print("preorder")
    # BiTreeOrder().preorder(aNode)
    # print("preorderfunc1-------------")
    # answer = BiTreeOrder().preorder_func1(aNode)
    # print(answer)

    # print("inorder")
    # BiTreeOrder().inorder(aNode)

    print("backorder")
    BiTreeOrder().backorder(aNode)

    print("----------")
    stack_order().back_stack_order(aNode)

    # a = [1,2,3]
    # print(a.pop(0))
    # print(a.pop(-1))
    # print(a)

