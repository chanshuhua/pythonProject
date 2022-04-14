class Person:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def head(self):
        print("headattribute")
        return 1
    def body(self):
        print("bodyattribute")
        return 1


class  Person_info(object):
    def __init__(self,name,heigh,weight,sex=0):
        self.name = name
        self.sex = sex
        self.heigh = heigh
        self.weight = weight

    def psex(self):
        if self.sex!=0:
            return "male"
        else:
            return "female"

    def pheigh(self):
        return self.heigh

    def pweight(self):
        return str(self.weight)+"kg"

    # def preturn(self):
    #     return self.pweight(),self.pheigh(),self.psex()

if __name__ == '__main__':


    # try:
    #     fh = open("testfile", "x")
    #     fh.write("file for test")
    # except IOError:
    #     print("Error: 没有找到文件或读取文件失败")
    #     print(IOError)
    # else:
    #     print("内容写入文件成功")
    #     fh.close()
    #
    # print("continue")



    example1 = Person_info('csh',162,52)
    print(example1)
    example2 = Person_info('cqc',161,60,1)
    example2.beat = 'beat'
    # print(example2.__getattribute__('beat'))
    print(example2)
    twins = [example1,example2]
    print(twins)

    print(example1.__dict__)  # 获取整个实例类的属性及值
    print(example2.__dict__)
    print(example1.__class__)

    print(hasattr(example1,'sex'))
    print(getattr(example1,'sex','heigh'))
    print(getattr(example2, 'sex',  'beat'))




