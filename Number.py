#!/usr/bin/python3
"""
Python 支持三种不同的数值类型：

整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

Python 数字数据类型用于存储数值。

数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
"""

number = 0xFFE  #十六进制数字
number1 = 0o72   #八进制数字
number2 = 3.14   #浮点类型数字
number3 = 32.3j  #复数
numcer4 = 9.332e-36j   #复数
number5 = 100
print(number)
print(int(number2))  #转化为整数
print(float(number5)) #转化为浮点数

