#!/usr/bin/python3
#coding:utf-8

import math

L = []   #空集合
x = 1
while x<=100:
    L.append(x * x)
    x = x + 1
print("1*1 + 2*2 + 3*3 + ... + 100*100 =" , sum(L))

"""
在Python中，定义一个函数要使用 def 语句，
依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，
函数的返回值用 return 语句返回。

请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，
并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为 None。

return None可以简写为return。
"""
def square_of_sum(list):
    sum = 0
    for x in list:
        sum = sum + x * x
    return sum

print(square_of_sum([1,2,3,4,5,6]))
print(square_of_sum([-5,0,5,10,15]))

#Python的函数返回多值其实就是返回一个tuple
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

#ax^2 + bx + c = 0
def quadratic_equation(a,b,c):
    x = math.sqrt(b * b - 4 * a * c)
    return (-b + x)/(2 * a),(-b - x)/(2 * a)


"""
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

举个例子，我们来计算阶乘 n! = 1 * 2 * 3 * ... * n，用函数 fact(n)表示，可以看出：

fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
所以，fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
"""
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


#汉诺塔
def hannuota(n,a,b,c):  #n个盘子，a,b,c三个柱子
    if n == 1:
       print(a,'-->',c)
       return
    hannuota(n-1, a, c, b)
    print(a, '-->', c)
    hannuota(n-1, b, a, c)


if __name__ == '__main__':
    print(move(0, 0, 50,  math.pi / 6))
    print(quadratic_equation(2,3,0))
    print(fact(20))
    hannuota(4,'A','B','C')


