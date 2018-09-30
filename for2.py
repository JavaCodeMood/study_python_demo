#!/usr/bin/python3
# coding:utf-8

import  time

#多重循环，在循环内部，还可以嵌套循环
def for1():
    for x in ['A','B','C','D','E','F','G']:
        for y in ['1','2','3','4','5','6','7']:
            print(x+y)


#对100以内的两位数，使用一个两重循环打印出所有十位数数字比个位数数字小的数
def for2():
    for a in [1,2,3,4,5,6,7,8,9]:    #十位
        for b in [0,1,2,3,4,5,6,7,8,9]:   #各位
            if a < b:
                print(a * 10 + b)


if __name__=='__main__':
    for1()
    time.sleep(10)
    for2()



