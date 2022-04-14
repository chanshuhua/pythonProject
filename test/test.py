# -*- coding: utf-8 -*-
import math
import operator
from functools import reduce


def dict_test():
    dict= {"name":"hely","sex":"male"}
    name,sex= dict.get("name"),dict.get("sex")
    num = dict.get("dnks")
    print(name,sex)
    print(num)

def input_test():
    a = input("please input a:")
    print(a)
    print("a+10 =",int(a)+10)

def open_test():
    a = open(file="open.txt",mode='a+')
    a_content = a.read()
    print(a_content)
    a.write("这是我插入的内容。")
    print(a.read())


class foo(object):
    @staticmethod
    def foo_def1():
        print("foo_def1")
        return 1

    def foo_def2(self):
        print("foo_def2")
        return 1

# foo.foo_def1() #class不需要实例化
# foo().foo_def2() #一定需要class()

class foo_info(foo):
    # foo_info继承foo类
    def foo_info_def1(self):
        return foo.foo_def1()

# all()等价
def all_test(m):
    for i in m:
        if not i:
            return False
        else:
            return True
    print(all_test([1,2,3]))
    print(all[1,2,3])  #全为true才是true
    print(any([0,1,2,4])) #全为false才是false
    #元素除了是 0、空、None、False 外都算 True。

def enumerate_test():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(tuple(enumerate(seasons)))
    print(list(enumerate(seasons)))

def ord_test():
    return ord('A')

def eval_test():
    return eval('3*9'),eval('pow(2,3)')

def pow_test(x,y,z=None):
    return pow(x,y,z)

def sum_def():
    return sum([1,2,3])

def iter_def(nums):
    list = [1, 2, 3, 4]
    list = list.__iter__() #若没有这一步则未完成迭代对象转换，则调用__next__()方法会报错。
    a = list.__next__() #内存释放
    print(a)

def filter_def(n):
    return n % 2 == 0
# 需要讲过滤后的数组转换为list/tuple
# print(list(filter(filter_def,[1,2,3,4,5])))
class Person():
    def __init__(self,name):
        self.name = name
    def state(self):
        return 1
def property_test():
    person1 = Person("chen")
    print(property(person1))

def range_def():
    for i in range(0,-10,-2):
        print(i)
# for函数等循环函数中使用

def bytearray_def():
    print(bytearray(10))
    print(bytearray('hello','utf-16'))
    print(bytearray([1,2,255]))
    print(bytearray())

def format_def():
    print("{name} is a pig!".format(name='chenshuhua'))
    dict = {'name':'chenshuhua','animal':'pig'}
    print("{name} is a {animal}".format(**dict))
    list = ['chenshuhua','pig']
    print("{0[0]} is a {0[1]}".format(list))
    print("{} is a {}".format('chenshuhua','pig'))

class lam():
    def lambad_def(self):
        return lambda a,b : a**b

    def lambad2_def(self):
        return lambda x,y:x if x<y else y

# exam1 = lam().lambad_def()
# exam2 = lam().lambad2_def()
# print(exam1(2, 4))
# print(lam().lambad_def()(2,4))
# print(exam2(10,-10))

def reduce_def():
    print(reduce((lambda a,b:a+b),[2,4,6,8]))
    print(reduce((lambda x,y:x if x<y else y),[-1,2,0,3,-10]))
    print(reduce(operator.add,[1,3,5]))
    print(reduce(operator.mul,[1,2,3],9)) # 9*1*2*3
                                          # reduce(function, iterable, initializer=None)

def locals_def():
    sex = 1
    name = [1,2]
    return locals()



if __name__ == '__main__':
   print(locals_def())