#!/usr/bin/python3
# coding:utf-8

"""
L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
如果第一个索引是0，还可以省略
L[:]实际上复制出了一个新list。

切片操作还可以指定第三个参数：

L[::2]
['Adam', 'Bart']
第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。

把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple。
"""

#使用range函数创建一个数列
L = range(1,100)
print(L[0:10])  #前10个数
print(L[2::3])   #3的倍数
print(L[4:51:5])  #不大于50的5的倍数
print(L[-10:])  #最后10个数
print(L[-46::5])  #最后10个5的倍数

"""
Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
"""
print("\n\n")
List = ['a','b','c','d','e','f','g']
print(List[-2:])
print(List[-4:-1])
print(List[-5:-1:2])

"""
字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[-3:]
'EFG'
>>> 'ABCDEFG'[::2]
'ACEG'
"""

def firstCharUpper(s):
    return s[0].upper() + s[1:]

print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))

