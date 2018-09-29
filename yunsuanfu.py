#!/usr/bin/python3

a = 21
b = 10
c = 0

if (a == b):
    print("a等于b")
else :
    print("a不等于b")

if (a != b):
    print('a不等于b')
else :
    print('a等于b')

if (a < b):
    print('a小于b')
else :
    print('a大于等于b')

if (a > b):
    print('a大于b')
else :
    print('a小于等于b')

print("---------------")
a = 2  #修改变量的值
b = 9
if (a > b):
    print('a大于b')
else :
    print('a小于等于b')

print("-----------------------")
x = 100
y = 8
z = 0

z = x + y
print("z=",z)
z += x  #z=z + x
print("z1=",z)
y **= 2 #y=y**2 y的2次方
print("y=",y)
x //= 9  #x=x//9
print("x=",x)

print("--------------------")
'''
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101
^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111
'''
a1 = 60  #60 = 0011 1100
b1 = 13  #13 = 0000 1101
c1 = 0

c1 = a1 & b1 #12 = 0000 1100
print("1-> c1=",c1)

c1 = a1 | b1 #61 = 0011 1101
print("2-> c1=",c1)

c1 = a1 ^ b1 #49= 0011 0001
print("3-> c1=",c1)

c1 = ~a1 #-61 = 1100 0011
print("4-> c1=",c1)

c1 = a1 << 2 #左移2位相当于乘以2的2次方 240 = 1111 0000
print("5-> c1=",c1)

c1 = a1 >> 2 #右移2位相当于除以2的2次方 15 = 0000 1111
print("6-> c1=",c1)

print("--------------")
"""
Python逻辑运算符
Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:

运算符	逻辑表达式	描述	实例
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

"""
a2 = 10
b2 = 20
if(a2 and b2):
    print("1->变量a2和b2")
else:
    print("1-> 变量a2和b2有一个不为true")

if ( a2 or b2 ):
   print ("2 - 变量 a2 和 b2 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a2 和 b2 都不为 true")

if not( a2 and b2 ):
   print ("3 - 变量 a2 和 b2 都为 false，或其中一个变量为 false")
else:
   print ("3 - 变量 a2 和 b2 都为 true")

print("------------------")
"""
Python成员运算符
除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。

运算符	描述	实例
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
"""

a3 = 3
b3 = 9
list = [1,2,3,4,5,6,7,8,10]
if(a3 in list):
    print("元素a3在列表list中")
else:
    print("元素a3不在列表list中")

if(b3 not in list):
    print("元素b3不在列表list中")
else:
    print("元素b3在列表list中")


print("-------------------------------")
"""
Python身份运算符
身份运算符用于比较两个对象的存储单元

运算符	描述	实例
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
注： id() 函数用于获取对象内存地址。
"""

a4 = 10
b4 = 10
if(a4 is b4):
    print("1->a4和b4引用自一个对象")
else:
    print("1->a4和b4来自不同的对象")

if(a4 is not b4):
    print("2->a4和b4来自不同的对象")
else:
    print("2->a4和b4来自同一个对象")

if (id(a4) == id(b4)):
    print("a4和b4有相同的标识，来自同一个对象")
else:
    print("a4和b4有不同的标识，来自不同对象")