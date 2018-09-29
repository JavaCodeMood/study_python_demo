#!/usr/bin/python3
#coding:utf-8

def fib(n): #定义到n的斐波那契数列
    a,b = 0,1
    while b<n:
        print(b, end = ' ')
        a,b = b, a+b
    print()

def fib2(n):  #返回到n的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a,b = b,a+b
    return result


if __name__ == '__main__':
    #fib(100)
    print("-----------")
    print(fib2(1000))