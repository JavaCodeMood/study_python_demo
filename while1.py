#!/usr/bin/python3
#coding:utf-8

#在 while … else 在条件语句为 false 时执行 else 的语句块
count = 0
while count < 5:
    print(count, " 小于5")
    count = count + 1
else:
    print(count, " 大于或等于5")

#如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
float = 1
while (float): print("死循环开始。。。")