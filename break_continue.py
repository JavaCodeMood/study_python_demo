#!/usr/bin/python3
# coding:utf-8

#用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
sum1 = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum1 = sum1 + x
    x = x * 2
    n = n + 1
    print(x)
print("sum1 = " , sum1)

#在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
L = [89,90,100,40,55,76,69,80,77]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print("大于60分的平均分：", sum / n)


sum2 = 0
x1 = 0
while True:
    x1 = x1 + 1
    if x1 > 100:
        break
    if x1 % 2 == 0:
        continue
    sum2 = sum2 + x1
print("0到100的奇数和：" , sum2)