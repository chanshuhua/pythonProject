# -*- coding: utf-8 -*-
import math
import operator
from filecmp import cmp
from functools import reduce

from jsonpath import xrange


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

    print(tuple(range(10)))
    print(list(range(10)))
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
    print(reduce((lambda x,y:x if x<y else y),[-1,2,0,3,-10])) #cmp
    print(reduce(operator.add,[1,3,5]))
    # reduce(function, iterable, initializer=None)
    print(reduce(operator.mul,[1,2,3],9)) # 9*1*2*3


def locals_def():
    sex = 1
    name = [1,2]
    return locals()

def diff_list_tuple():
    a = [1,2,3]
    b = (1,2,3,2,2)
    a.append(4)
    print(a)
    print(b.count(2)) #返回value存在的次数
    # b.__add__((4))
    b = b[1:] +(888,) # 加
    print(b)
    b = b[:-2] # 减
    print(b)

def frozenset_def():
    a = [1,2,4]
    a.append(5)
    print(a)
    a = frozenset(a)
    a.append(6)

class a_vars():
    b_init = 1
    def a_init(self,a_init):
        self.a_init = a_init
def vars_def ():
    object1 = a_vars()
    print(vars(a_vars)) #类的所有属性值
    print(vars(object1)) #实例的属性值（不返回）


# classmethod test
class method():
    def method_1(self): #self 指object 即需要实例化后才可调用
        print("这不是classmethod装饰的！")
    @ classmethod
    def method_2(cls): #cls不需要实例化
        print("这是classmethod装饰的方法")

        # method.method_1()
        method().method_1()
        method.method_2()


class getattr_class(object):
    attr2 = 'atrr2'
    def getattrs(self,attr1):
        self.attr1 = attr1

def getattr_def():
    exam = getattr_class()  # 类名不可以和方法重名！！否则会找不到对应对象！！
    # print(getattr(exam, 'attr1'))
    print(getattr(exam, 'attr2'))

def map_def():
    #map也是返回迭代器
    print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))  # 等价：list(map(square, [1,2,3,4,5]))
    print(list(map((lambda y: y ** 2), [1, 2, 3, 4])))
    print(reduce((lambda x, y: (x + y) * 2), [1, 2, 3]))
    print(reduce((lambda a, b: a + b), [2, 4, 6, 8]))  #找规律小游戏 reduce（）用于两个参数的计算，map（）用于一个参数的计算。。

def repr_def():
    s = "s1 \t s2 \t \n 1 \t 2"
    print(s)  #会转义 转义符
    print(repr(s))  # 转义符直接转换成string输出

def cmp_def():
    # print(cmp(1,2)) #cmp python3.x种变为Operator
    print(operator.le(1,1))
    print(operator.lt(1,2))
    print(operator.ge(2,2))
    print(operator.gt(2,1))
    # print(cmp('a','A'))

def reverse_def():
    a = [1,2,3]
    b = a.reverse() # 直接返回反向列表
    print(b)  # 无返回值 none
    print(a)

def zip_def():
    a = [1,2]
    b = [3,4,5]  #这方法有啥用啊？？
    c = zip(a,b)
    print(c)
    print(list(c))
    d,e = zip(*zip(a,b))
    print(d,e)

def compile_def():
    '''
    eval - accepts only a single expression.
    exec - It can take a code block that has Python statements, class and functions, and so on.
    single - if it consists of a single interactive statement
    :return:
    '''
    str = 'for i in range(10):print(i)'
    do = compile(str,'','exec')
    exec(do)    # 执行str中转换为二进制的命令
    str = '(3+1)*3'
    do = compile(str, '', 'eval')
    eval(do)

def memoryview_def():
    return 1  # 感觉这里有点陌生。应该有别的调用方式。后面再看吧


def round_def(float):
    return round(float)

def complex_def(a,b):
    # a,b为数字 输入1，2 输出(1+2j)
    # 但是谁会用复数呢？？我反正不会用。用来干嘛。。
    return complex(a,b)

def hash_def(s):
    print(hash(s))  # 算法中常出现


def set_def():
    x = set('hello')
    y = set('xiaochen')
    z = ('hello')
    print('去重{}'.format(x))  # 对象中删除重复元素
    print(z)   # 直接输出字符串
    print('交集{}'.format(x&y)) # 取交集
    print('并集{}'.format(x|y)) # 取并集
    print('差集{}'.format(x-y))  # 取差集 同y-x
    print('补集{}'.format(x^y))  #补集 同y^x

class abc():
    abc_i = 1

def attr_def():
    ABC = abc()
    print(getattr(ABC,'abc_i'))
    print(vars(ABC))
    setattr(ABC,'abc_m',2)
    print(getattr(ABC,'abc_m'))
    print(vars(ABC))  #vars

def slice_def():
    '''
    slice(stop)
    slice(start, stop[, step])
    :return:slice(object)
    '''
    arr1 = [1,2,3,4,5,6,7,8,9,10]
    slice_arr = slice(1,10,2)
    print(arr1[slice_arr])
    # 约等于
    print(arr1[1:10:2])


def sort_def():
    arr = [4,6,2,1,4,7,8]
    sorted_arr = sorted(arr)
    print(sorted_arr)

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ]
    sorted_student_tuples_age = sorted(student_tuples, key=lambda student: student[2])  # sort by age
    print(sorted_student_tuples_age)

def exec_def():

    exec(input("please:"))
    exec(hello="print('hello')")


if __name__ == '__main__':
    exec_def()