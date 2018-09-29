#!/usr/bin/python3
#coding:utf-8

#for循环 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(5):
    print(i)
print("-------")

#使用range指定区间的值
for x in range(5,10):
    print(x)
print("-------")

#可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for y in range(0,15,3):
    print(y)
print("-------")

for z in range(-10,-100,-30):
    print(z)
print("-------")

#结合range()和len()函数以遍历一个序列的索引
list1 = ["Java","c","c++","go","python"]
for j in range(len(list1)):
    print(j,"->",list1[j])
print("----------")

#可以使用range()函数来创建一个列表
list2 = list(range(5))
print(list2)
print(type(list2))   #查看类型
print("----------")

#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for letter in 'abcdefghijk':
    if letter == 'e':
        break
    print("当前字母：",letter)

print("------------")
var = 10
while var > 0:
    print("当前变量：",var)
    var = var - 1
    if var == 5:
        break


