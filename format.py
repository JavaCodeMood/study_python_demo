#!/sur/bim/python3
# coding:utf-8

import math

"""
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
ljust() 方法，它可以将字符串靠左，并在右边填充空格。
center() 方法，将字符串居中，左右填空格。
zfill() 方法 在数字的左边填充0
format格式化
"""
def geshi():
    for x in range(1, 11):
        print(repr(x ))
        print(repr(x).rjust(2), repr(x*x).rjust(3),end=' ')
        print(repr(x*x*x).rjust(4))

def geshi1():
    for x in range(1,11):
        print('{0:2d} {1:3d},{2:4d}'.format(x,x*x,x*x*x))

#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用
def geshi2():
    table = {'中国':1,'俄罗斯':2,'美国':3,'日本':4}
    for name,number in table.items():
        print('{0:10}==>{1:10d}'.format(name,number))


def geshi3():
    table = {'中国': 1, '俄罗斯': 2, '美国': 3, '日本': 4}
    print('中国:{0[中国]:d};俄罗斯:{0[俄罗斯]:d}'.format(table))


if __name__== '__main__':
    geshi()
    geshi1()
    print("234".zfill(6))
    print('{}网址: "{}!"'.format('百度','www.baidu.com'))
    print('姓名：{0},性别：{1},罩杯：{2}'.format('小美','女','C'))
    print('姓名：{name},年龄：{age}'.format(age=20,name='将军'))
    print("常量PI：{}".format(math.pi))
    print("常量PI: {0:.4f}".format(math.pi))
    geshi2()
    geshi3()
