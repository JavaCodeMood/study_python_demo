#!/usr/bin/python3
#coding:utf-8

"""
python3使用def关键字来定义函数，如下：
def 函数名（参数列表）:
    函数体
"""

import math

#计算矩形的面积
def area(width,height):
    return width * height

#计算圆的面积
def arcle(r):
    return math.pi * r * r

n = int(input("请输入1或2："))
if n == 1:
    print("计算矩形的面积")
    w = int(input("请输入宽："))
    h = int(input("请输入长："))
    s = area(w,h)
    print("矩形的面积：",s)
elif n == 2:
    print("计算圆的面积")
    r = int(input("请输入圆的半径："))
    s = arcle(r)
    print("圆的面积：",s)
else:
    print("错误的输入")
