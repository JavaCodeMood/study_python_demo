#python基础语法
#coding:utf8

"""
注意：

1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
"""

#定义变量
a,b,c = 5,8,10
print(a+b+c)

a= 20
b= 3
print(a/b)  #除法  输出浮点数
print(a//b) #除法  输出整数
print(a%b)
print(2**4)  #2的4次方


str = "离愁别绪"
print(type(str))   #查看变量str的类型
print(isinstance(str, int))   #判断变量str是不是int类型的

