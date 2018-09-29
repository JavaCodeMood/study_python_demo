#!/usr/bin/python3
# coding:utf-8

import sys

#定义一个列表
list = [100,90,80,"没了你","万杯觥筹","不过是","提醒","寂寞"]
#使用iter方法遍历这个列表
it = iter(list)
print(next(it),end=" ")


#使用for循环遍历列表
for x in it:
    print(x,end=",")


#使用next方法遍历列表
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()





