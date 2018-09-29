#!/usr/bin/python3
# coding:utf-8

day = int(input("请输入星期数："))
print("")
if day == 1 :
    print("今天是周一")
elif day == 2 :
    print("今天是周二")
elif day == 3 :
    print("今天是周三")
elif day == 4 :
    print("今天是周四")
elif day == 5 :
    print("今天是周五")
elif (5 < day <8) :
    print("愉快的周末")
else:
    print("错误的输入")

