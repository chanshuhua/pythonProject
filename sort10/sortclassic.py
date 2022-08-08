#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject2 
@File    ：sortclassic.py
@IDE     ：PyCharm 
@Author  ：chenshuhua
@Date    ：2022/7/1 8:46 
'''



def bubblsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def insertSort(arr):
    for i in range(1,len(arr)):
        print('i:%s' %i)
        # for j in range(i-1,-1,-1):
        #     print('j:%s' %j)
        j = i-1
        print('j:%s' % j)
        while arr[j]>=arr[j+1] :
            if j<0:
                break
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j-=1
            print(arr)
    return arr

'''
归并排序
'''
def merge_sort(arr):
    # 一步步分治递归过程！！常看看
    # 只剩下一个元素时返回
    if len(arr) == 1:
        return arr
    # 分治
    mid = len(arr)//2
    left_arr = arr[0:mid]
    right_arr = arr[mid:]
    # print(left_arr)
    # print(right_arr)
    # 递归
    return merge(merge_sort(left_arr),merge_sort(right_arr))

def merge(left,right):
    # 合并
    # 最终两个的有序数组进行合并才有意义
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    # 如果left 或者 right 任一数组排序完毕
    if left:
        res +=left
    if right:
        res +=right
    return res

def quick_sort(arr):
    # 跳出递归的条件
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]

        # 直接获取arr中的值与基线值进行比对
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)

def shell_sort(arr):
    pass

if __name__ == '__main__':
    res = quick_sort([3,2,4,1,1,5])
    print(res)