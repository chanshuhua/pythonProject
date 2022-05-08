####slice 切片
#####正向slice 
list [start : end : step]  

step为正时，切片方向为从左至右，start→end，start、end方向在填写时候也必须从左到右。
#####反向slice
list [start : end : -step]  

step为负数时，切片方向为从右至左，start←end，start、end方向在填写时候也必须从右到左。切出来的结果与原list相比，反向了。

#### 类实例化中，变量名称不可以和类方法同名，会优先使用变量名称进行调用。

#### Python3 迭代器与生成器
#####迭代器
#####https://blog.csdn.net/mpu_nice/article/details/107299963
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器。

迭代器优点：

1. 提供了一种通用不依赖索引的迭代取值方式；

2. 节省内存，迭代器在内存中相当于只占一个数据的空间：因为每次取值都上一条数据会在内存释放，加载当前的此条数据。

迭代器缺点：

1. 因为有next方法，即只能往后取值,不能往前，取值不如按照索引的方式灵活，不能取指定的某一个值；

2. 无法预测迭代器的长度。

#####StopIteration
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

#####生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。


#### 内置函数
##### 全套 https://www.runoob.com/python/python-built-in-functions.html
```
abs(n) #返回绝对值
divmod(n,m) #返回除数和余数
input("") && raw_input()  #输入函数（int/float/str）
open(file,mode) #mode=a+ #打开文件夹
all() #判断迭代函数（iterable--元组或列表）中元素是否都为true，是则返回True，否则返回False
      #元素除了是 0、空、None、False 外都算 True
any() #判断迭代函数（iterable--元组或列表）中元素是否都为False，是则返回False，否则返回True
      #元素除了是 0、空、None、False 外都算 True
enumerate() #将可遍历的数据对象组合为一个索引，并返回数据及其下标
int() #强转整型
str() #强转字符串
ord() #返回对应的 ASCII 数值，或者 Unicode 数值
chr() #返回 unicode 的字符
eval() #用来执行一个字符串表达式，并返回表达式的值
isinstance()  #判断一个对象是否是一个已知的类型，类似 type()
pow(x,y,z) #x^y,若z存在则结果对z取模(取余)并返回 pow(x,y) %z
sum(iterable) #对iterable内容循环相加
execfile(filename) #可以用来执行filename文件
issubclass(class, classinfo) # 如果 class 是 classinfo 的子类返回 True，否则返回 False
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
super() #用于调用父类(超类)的一个方法,来解决多重继承问题的,直接用类名调用父类方法在使用单继承的时候没问题,但是如果使用多继承,会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题.
bin(int) #返回二进制
oct() #函数将一个整数转换成8进制字符串
chr() #返回十六进制
hex() #函数用于将10进制整数转换成16进制，以字符串形式表示
iter() #函数用来生成迭代器
property() #函数的作用是在新式类中返回属性值 !!!!review one more time
tuple() #函数将列表转换为元组
float() #数字转换为浮点数
list() #函数转换为列表
dict #创建一个字典 key:value
bool() #函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
filter() #函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
len() #返回对象（字符、列表、元组等）长度或项目个数
range() #函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
xrange() = range() #所不同的是生成的不是一个数组，而是一个生成器。
type() && isinstance() #type() 不会认为子类是一种父类类型，不考虑继承关系；isinstance() 会认为子类是一种父类类型，考虑继承关系。如果要判断两个类型是否相同推荐使用 isinstance()。
bytearray([source[, encoding[, errors]]]) # 返回新字节数组
callable #用于检查一个对象是否是可调用的
format #基本语法是通过 {} 和 : 来代替以前的 %
locals() #返回当前位置的全部局部变量
dir() #不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
vars() #函数返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
globals #函数会以字典类型返回当前位置的全部全局变量
hasattr() # 函数用于判断对象是否包含对应的属性
frozenset() #返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
#lambda arguments : expression 匿名函数
reduce(function,iterable,initializer=None) #函数会对参数序列中元素进行累积,用于对list/tuple中的元素按照索引顺序连续操作或者返回，多个参数累计计算。
map() #会根据提供的函数对指定序列做映射，单个参数计算。
getattr() #函数用于返回一个对象属性值，getattr(object, name[, default])
setattr() #函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的
repr() #repr() 函数将对象转化为供解释器读取的形式，读取object返回string
operator.le/lt/ge/gt   e=equals t=than g=greater l=less
max() #求最大值
min() #求最小值
reverse() # 反向输出  list.reverse() 即为反向列表
zip() zip(*) #压缩迭代器，解压缩迭代器
compile() #函数将一个字符串编译为字节代码。
memoryview() #函数返回给定参数的内存查看对象(memory view)
round() #方法返回浮点数x的四舍五入值
__import__() #函数用于动态加载类和函数 
complex() #函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
hash() #用于获取取一个对象（字符串或者数值等）的哈希值  算法中常用！！
set() # 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
#交集 & : x&y，返回一个新的集合，包括同时在集合 x 和y中的共同元素。
#并集 | : x|y，返回一个新的集合，包括集合 x 和 y 中所有元素。
#差集 - : x-y，返回一个新的集合,包括在集合 x 中但不在集合 y 中的元素。
#补集 ^ : x^y，返回一个新的集合，包括集合 x 和 y 的非共同元素。
delattr(object, name) #函数用于删除属性   =del x._attr 
help() #函数用于查看函数或模块用途的详细说明
next() #返回迭代器的下一个项目。 next() 函数要和生成迭代器的iter() 函数一起使用。
slice(start, stop[, step]) #函数实现切片对象，主要用在切片操作函数里的参数传递
id() #函数用于获取对象的内存地址
sorted(iterable, cmp=None, key=None, reverse=False) #函数对所有可迭代的对象进行排序操作，sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
exec() #代码块执行，忽略global和local 全局变量和当前变量。

```

##### tuple和list的区别
```
tuple:  
1、不支持直接添加元素【增】

2、不支持直接删除元素【删】

3、不支持直接修改元素（修改操作的步骤是：先删除、再添加）【改】

https://blog.csdn.net/Gxysleeping/article/details/81038910
# 间接增删改元素

4、支持2种查找元素【查】

第一、根据下标查找元素，称为【访问】元素，时间复杂度为O（1）

第二、根据元素值获取下标，称为【查找】元素，时间复杂度为O（n）

list:  
列表 ：(列表可以嵌套，列表的中的元素可以为任意)

列表的创建：1.a = [1, 2, 3]  2.a = list([1, 2, 3])

1.查：
1.1索引（下标），都是从0开始
1.2切片
.count 查某个元素在列表中出现的次数
.index 根据内容找对应的位置（第一个匹配项所在的位置）
“二狗” in a       判断二狗是不是在列表a中 

2.增：
a. append()      用于在列表末尾追加新的对象追加 
a. insert(index, “内容”)，    用于将对象插入列表中 
a. extend        扩展（可以在列表的末尾一次性追加另一个序列中的多个值）
 
3.修改：
a[index] = “新的值” 
a[start:end] = [a, b, c]

4.删除：
remove(内容)
pop(index)         注:如果不加索引会默认删除最后一个；有一个返回值
del a  或 del a[index]
a. claer()           把列表a清空
 
5.排序：
sort()　　
reverce() 

6.身份判断（判断是不是一个列表）:
type(a) is list


```


#### 装饰器
##### @property @property.setter @property.deleter
.@property(用于场景方法不要传递参数，且有return可以使用。就是普通函数)  
property() 函数的作用是在新式类中返回属性值。把方法伪装成属性了。
```
 def aer(self): # 面积
     return self.r**2*pi
->  print(aa.aer()) 

 @property
    def aer(self):  # 面积
        return self.r ** 2 * pi
->  print(aa.aer)

```

.@方法名.setter：被 @方法名.setter 装饰的函数装饰函数名字必须和方法名字相同，调用时名字时可直接执行setter方法  
.@方法名.deleter： 调用时可通过公用的方法删除私有的属性
```
    # @property把方法变成属性方法访问 
    @property
    def name(self):
        return  self.__name

                
    @name.setter                   # 对象的修改   @name.setter 注意要和转换了属性的方法名称一致
    def name(self,new_name):
        self.__name=new_name
    
    @price.deleter                  # 对象的删除 
    def price(self):
        print('@price.deleter')
d=Persa("李四")
print(d.name)  # 不需要调用方法 d.name()
d.name='王五'   # 更改名字不需要调用方法，更改属性值即可
print(d.name)
del d.name # 执行删除方法
```



##### @classmethod
.@classmethod 使用场景：如果方法使用到当前类，就可以使用类方法，无需实例化对象即可调用。

```
class A():
    def a(self):
    print("not classmethod")
    @classmethod
    def b(cls):
    print("classmethod")

A().a() # 输出 "not classmethod"
A.A()   #报错
A.b()   # 输出 "classmethod"

```

##### @staticmethod
.@staticmethod 该方法不强制要求传递参数，返回函数的静态方法。  
该方法不需要实例化调用，但也可以实例化后进行调用。普通方法必须实例化。
```
class foo(object):
    @staticmethod
    def foo_def1(): #方法内不需要self
        print("foo_def1")
        return 1

    def foo_def2(self):
        print("foo_def2")
        return 1

foo.foo_def1() #class不需要实例化
foo().foo_def2() #一定需要class()

```


##### jsonpath用法
```
# 寻找json中某个关键词
jsonpath.jsonpath(res["data"]["records"], '$..' + 'checkId')
```

##### dict、bytes、str 转换
```
dict->json  json.dumps()  
json->dict  json.loads()  

string->bytes  encode()  
bytes->string  decode()  

```

##### return 和 yield 的区别
```
return 后面不可再执行代码
yield 后面可接续接需要执行的代码

def func1():
    do ...
    yield
    do ...

def func2(func1)
or 
def func2():
    func1()



```

