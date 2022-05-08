# encoding = utf-8

# 基本数据结构: 顺序表、链表、队列、栈、树


### 1、链表
# head(self._head仅指向头节点，作为开始标志) ->(item1)|item1.next ->(item1)|item1.next ->(itemn)|itemn.next->
# ###
import sys


class Node(object):
    '''
    node 由item+next构成
    '''


    # 1、定义节点 数据结构=数据元素（item）+指针（next）
    def __init__(self,item):
        self.item = str(item)  # item存放数据元素
        self.next = None  # next指向下一个节点


    # 2、定义单向链表 链表首地址指针head
class SingleLinkList(object):
    '''
    link-head 定义头节点指向地址
    '''
    def __init__(self):
        self._head = None
    def is_empty(self):
        '''
        判断链表是否为空
        :return:
        '''
        return self._head is None

    def length(self):
        '''
        链表长度
        :return:
        '''
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        '''
        遍历链表
        :return:
        '''
        cur = self._head
        while cur is not None:
            yield cur.item   # 返回当前链表元素
            cur = cur.next   # 指针下移


    def add(self,item):
        '''
        向列表头部添加元素
        :return:
        '''
        node = Node(item=item) # 将新增的元素变为一个节点
        node.next = self._head  # 原头部指针指向的节点是新元素的下一个节点
        self._head = node  # 新头部节点指向新元素

    def append(self,item):
        '''
        向尾部新增元素
        :param item:
        :return:
        '''
        node = Node(item)  # 新增元素设为节点
        # 先判断是否为空链表
        if self.is_empty():
            # 是则头节点直接指向新节点
            self._head = node
        else:
            # 不是则遍历找到最后一个节点
            cur = self._head
            while cur.next != None: # while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self,index,item):
        '''
        指定位置插入元素
        :param index:
        :param item:
        :return:
        '''
        node = Node(item)   # 插入的元素构造一个节点
        if index <= 0:
            self.add(node)
        elif index > (self.length() - 1):
            self.append(node)
        else:
            cur = self._head
            #while cur && cur.next is not None
            for i in range(index-1):  # 循环才能保持右移!!!
                cur = cur.next # 完成节点右移
            # 完成节点插入
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        '''
        删除节点
        :param item:
        :return:
        '''
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item != item:
                # 节点后移，cur变成pre，cur下个节点变为当前节点
                pre = cur
                cur = cur.next
                # print(cur.item)
            else:
                if pre is None: #if not pre:
                    self._head = cur.next
                else:
                    # print(cur.item,item)
                    # print(cur.next)
                    if cur.next is None:
                        pre.next = None
                    else:
                        pre.next = cur.next
                return True

    def find(self,item):
        '''
        寻找item是否在链表中
        :param item:
        :return:
        '''
        if item in self.items():
            print(item)
            return True
        else:
            return False

# exam1:创建链表
if __name__ == '__main__':
    # 1、创建链表
    link_list = SingleLinkList()
    # 2、创建节点
    node1 = Node(1)
    node2 = Node(2)
    # 3、节点添加到链表中
    link_list._head = node1
    node1.next = node2

    # 4、访问链表
    print("first's item={}".format(link_list._head.item)) # 访问第一个节点
    print("second's item={}".format(link_list._head.next.item)) # 访问第二个节点
    print("length={}".format(link_list.length()))

    link_list.add('before')  # 添加首节点
    link_list.append('last')  # 添加尾节点
    link_list.insert(1,'insertitem')

    # 循环取迭代器中的元素并打印出来 ?? 其实不是和理解这个yield应该已经返回了当前的
    for i in link_list.items():
        print(i, end='\t')
    print('\n')

    # 删除
    link_list.remove('last')
    for i in link_list.items():
        print(i, end='\t')

    print('\n')
    print(link_list.find('last'))

    link_list2 = SingleLinkList()
    print(link_list2.is_empty())




