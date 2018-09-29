#!/usr/bin/python3
# coding:utf-8

"""
input()方法：内置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回

open() 将会返回一个 file 对象
f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
f.read()  读取文件内容
f.read(size)  读取一定数量size的内容
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
f.readlines() 将返回该文件中包含的所有行。 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
from_what 值为默认为0，即文件开头。

 f.close() 来关闭文件并释放系统的资源

"""
def readfile(filename):
    #打开一个文件
    f = open("D:/lhfcode/Python/"+filename+".txt", "r")
    #str = f.read()
    #print("str =", str)

    str1 = f.read(-10)
    print("str1 =", str1)

    str2 = f.readline()
    print("str2 =", str2)

    str3 = f.readlines()
    print("str3 =", str3)

    filestr = f.tell()
    print("filestr = " , filestr)

    #迭代文件，读取每一行
    for line in f:
        print(line, end=' ')

    firstStr = f.seek(5)
    print("firstStr = ", firstStr)


    #关闭打开的文件
    f.close()

if __name__=='__main__':
    filename = input("请输入要读取的文件名：")
    readfile(filename)
    print("文件名：", filename)