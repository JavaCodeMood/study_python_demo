#!/usr/bin/python3
# coding:utf-8

"""
while 循环
Python中while语句的一般形式：

while 判断条件：
    语句
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
while 循环不会迭代 list 或 tuple 的元素，而是根据表达式判断循环是否结束。
"""

#输入一个数n，计算1+2+3+...+n之和
n = int(input("请输入一个数："))
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1->1到%d之和为：%d"%(n,sum))

#我们可以通过设置条件表达式永远不为 false 来实现无限循环
var = 1
sum = 0
num = 1
while var == 1:
    m = int(input("请输入一个数："))
    while num <= m:
        sum = sum + num
        num += 1;
    print("2->1到%d之和为：%d" %(m,sum))
