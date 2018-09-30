#!/usr/bin/python3
# coding:utf-8

"""
Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：

int('123')
123
int('123', 8)
83

int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。

函数的默认参数的作用是简化调用，你只需要把必须的参数传进去。
但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。

函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面
"""

#输入一个数计算，计算它的平方
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def green(str='world'):
    print("Hello, " + str + ".")

"""
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：

def fn(*args):
    print args
可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数

可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。

定义可变参数的目的也是为了简化调用。假设我们要计算任意个数的平均值，就可以定义一个可变参数
"""
#输入任意多个数，计算平均值
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for n in args:
        sum = sum + n
    print("平均值：", sum / len(args))


if __name__ == '__main__':
    print("4的平方：", power(4))
    print("2的三次方：", power(2,3))
    green()
    green('雪儿')
    average()
    average(1,2,3,4)
    average(100,90,80,70)
