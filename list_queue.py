#!/usr/bin/python3
# coding:utf-8

"""
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，
第一个取出来；但是拿列表用作这样的目的效率不高。在
列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快
（因为所有其他的元素都得一个一个地移动）。
"""

from collections import deque

#队列先进先出
queue = deque([1,3,5,7,9,11])
#向列表中队列中添加元素
queue.append(13)
queue.append(15)
print("queue=",queue)
#出列
print(queue.popleft())
print(queue.popleft())
