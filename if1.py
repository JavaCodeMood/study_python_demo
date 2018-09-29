#!/usr/bin/python3
# coding:utf-8

"""
#猜数字
number = 10
guess = -1
print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入一个数："))
    if guess == number :
        print("恭喜你，猜对了")
    elif guess < number:
        print("猜小了。。。")
    elif guess > number:
        print("猜大了。。。")

"""

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的既可以整除2，也可以整除3")
    else:
        print("你输入的数只能整除2，不能整除3")
else:
    if num % 3 == 0:
        print("你输入的数只能整除3，不能整除2")
    else:
        print("你输入的数既不能整除2也不能整除3")