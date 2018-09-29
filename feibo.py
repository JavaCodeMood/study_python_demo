#!/usr/bin/python3

#斐波那契数列 1 1 2 3 5
#f(i) = f(i-1) + f(i-2)

a,b = 0, 1
while b < 20:
    print(b)
    a, b = b, a+b

print("----------------------")
x,y = 0,1
while y < 100:
    #关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    print(y, end=',')
    x,y = y, x+y