# This is a sample Python script.

import time

import jmespath as jmespath


def cost(func):
    def warpper():
        t1 = time.time()
        res = func()
        t2 = time.time()
        print(func.__name__ + "执行耗时" + str(t2-t1))
        return res

    return warpper

@cost
def print_say():
    print("here begin")
    time.sleep(1)
    print("here over")


if __name__ == '__main__':
    # print_hi('PyCharm')

    print_say()

