#！/usr/bin/python3
# coding:utf-8

def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)
    return

#调用changeme函数
mylist = [10,20,30]
changeme(mylist)
print("函数外取值：",mylist)

#关键字参数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return

printme(str = "你好！")

#关键字参数，不使用指定顺序
def printinfo(name,age):
    "打印任何传入的字符串"
    print("姓名：",name," 年龄：",age)
    return

printinfo(age = 20, name = "霜花似雪")

#使用默认参数
def printMethod(name,age= 20):
    print("姓名：", name, " 年龄：", age)
    return

printMethod(name="花花")

#使用不定长参数
def printA(arg1,*vartuple):
    print(arg1)
    print(vartuple)

printA(10,20,30,40,50)

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def printTuple( msg, *vartuple):
    print(msg)
    for var in vartuple:
        print(var)
    return

printTuple(100)
printTuple(99,98,97)

#加了两个星号 ** 的参数会以字典的形式导入。
def printDict(arg1, **vardict):
    print(arg1)
    print(vardict)

printDict(1,name="zhangsan",age=20,addr="北京")

"""
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
"""
sum = lambda a,b:a+b
print("和为：",sum(10,20))
print("和为：",sum(100,200))

#return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sumone(arg1,arg2):
    total = arg1 + arg2
    print("函数内：",total)
    return total

total= sumone(33,66)
print("函数外：",total)

#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
num = 1
def fun1():
    global num  #需要使用global关键字声明
    print(num)
    num = 100
    print(num)
fun1()
print(num)

#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    mm = 100
    def inner():
        nonlocal mm #使用nonlocal关键字声明
        mm = 10000
        print(mm)
    inner()
    print(mm)
outer()


