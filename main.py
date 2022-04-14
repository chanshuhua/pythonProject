# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from datetime import datetime, timedelta

# def search(a,n):
#
#     # print('h')
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#     maxs = len(a) - 1
#     mid = (maxs - mins) // 2
#
#     if mins > maxs:
#         return -1
#     elif a[mid] < n:
#         mid = mid
#         print(a[mid],a[mid+1])
#         return search(a[mid+1:], n)
#     elif n < a[mid]:
#         mid = mid
#         print(a[mid], a[mid - 1])
#         return search(a[:mid], n)
#     else:
#         print(a[mid], mid, n)
#         return a[mid] , mid ,n
#     # return a[mid] , mid ,n
#
#
# def find(n):
#     if a[mid] == n:
#         # if a[midl]<a[mid]:
#         #     return midl,a[midl]
#         # if a[mid]<a[midr]:
#         #     return midr,a[midr]
#         for i in range(maxs):
#             midl = mid - 1
#             midr = mid + 1
#             if a[midl] != a[mid] and midr != a[mid]:
#                 return midl, midr
#         return mid


# Press the green button in the gutter to run the script.
from threading import Timer

if __name__ == '__main__':
    # a = [0,1,1,1,2,3,5,5,5,6,7,8,9,10]
    # n = 1
    # mins,maxs,mid = 0,0,0
    # midr = 0
    # midl = 0
    # # maxs = len(a) - 1
    # # mid = (maxs - mins) // 2
    # # search(a,n)
    # a[mid], mid, n = search(a,n)
    # print(a[mid], mid, n)
    # a,b,c = find(n)
    #
    # print(a[mid])
    # print(mid)
    # print(a[midr],a[midl])
    # print(midr,midl)


    # zimubiao = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't',
    #             'y', 'u', 'i', 'o', 'p']
    # flag = 0
    # s = "j?qg??b"
    # for i in s:
    #     if i == '?':
    #         flag += 1
    #     elif i in zimubiao:
    #         zimubiao.remove(i)
    #     else:
    #         continue
    # str1 = random.choice(zimubiao)
    #
    # if flag > 1:
    #     print(flag)
    #     str1 = random.sample(zimubiao, flag)
    #     print(str1)
    #     for i in s:
    #         if i == "?":
    #             str = s.replace('?',str1[flag-1],1)
    #             flag -=1
    # else:
    #     str = s.replace("?", str1)
    #
    # print(str)


    #
    # today = datetime.now()
    # yesterday = today + timedelta(days = -1)
    # tomorrow = today + timedelta(days = 1)
    # print(yesterday,today,tomorrow)

    # nums = [2,7,11,15]
    # target = 9
    # index = []
    # for i in range(len(nums)):
    #     if nums[i] < target:
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] == target - nums[i]:
    #                 index.append(i)
    #                 index.append(j)
    #
    # print(index)

    # suiji = random.choice(["a","b","c"])
    #
    # for i in range(3):
    #   moji = random.choice(["a","b","c"])
    #   print(moji)


    # b=[100,2,20]
    # print(b[1:])
    # print(b.index(2))
    # c = b[1]
    # b[1] = b[0]
    # b[0] = c
    # print(b)






# 冒泡算法
#     nums = [18,20,77,1,3,4]
#     nums = [8,8,89,62,6]
    def dubble(nums ):
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j] >= nums[j+1]:
                    continue
                else:
                    logo = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = logo
        return nums

#
#     def exchange(num1,num2):
#
#
#         logo = num1
#         num1 = num2
#         num2 = logo
#         return num1,num2
#
# # 规则
#     #第一位数字
#
#     nums = [8,8,62,6,68,89]
#     # for n in nums:
#     #     lenmax = 0
#     #     if len(str(n))>=lenmax:
#     #         lenmax=len(str(n))
#     #         print("lens-max:{}".format(lenmax))
#
#         # first = str(i)[0:1]
#         # print(first)
#
#     for i in range(len(nums) - 1):
#         for j in range(len(nums) - 1 - i):
#             if len(nums[j]) == len(nums[j+1]):
#                 a = 0
#                 while a < len(nums[j]):
#                     if nums[j][a:a+1] > nums[j+1][a:a+1]:
#                         break
#                     elif nums[j][a:a+1] == nums[j+1][a:a+1]:
#                         a+=1
#                         continue
#                     else:
#                         exchange(nums[j],nums[j+1])
#                         break
#             elif len(nums[j]) > len(nums[j+1]):
#                 a = 0
#                 while a < len(nums[j]):
#                     if a == len(nums[j+1]):
#                         if nums[j][a-1:a] >= nums[j][a:a+1]:
#                             exchange(nums[j],nums[j+1])
#                         break
#                     if nums[j][a:a + 1] > nums[j + 1][a:a + 1]:
#                         break
#                     elif nums[j][a:a + 1] == nums[j + 1][a:a + 1]:
#                         a += 1
#                         continue
#                     else:
#                         exchange(nums[j], nums[j + 1])
#                         break


import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        # print(a)
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        # print(next(f), end=" ")
        print(next(f))
        print(' ')
        # next(f)
        # print(format(list(f)))
    except StopIteration:
        sys.exit()
















