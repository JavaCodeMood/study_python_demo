#!/usr/bin/python3
# coding:utf-8

"""
在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。
在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的

Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。
因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict
而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。
迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。

"""

for i in range(1,100):
    if i % 9 ==0:
        print(i, end=" ")



"""
Python中，迭代永远是取出元素本身，而非元素的索引。
使用 enumerate() 函数可以在for中取得索引
使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：

['Adam', 'Lisa', 'Bart', 'Paul']
变成了类似：

[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
因此，迭代的每一个元素实际上是一个tuple：

for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name
如果我们知道每个tuple元素都包含两个元素，for循环又可以进一步简写为：

for index, name in enumerate(L):
    print index, '-', name


索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身。
"""
print("\n\n")
L = ['a','b','c','d','c','e','f','f']
for index,name in enumerate(L):
    print(index,"-",name)


"""
zip()函数可以把两个 list 变成一个 list：

>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
"""
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index1,name1 in enumerate(zip(L,['100','70','90','80'])):
    print(index1,'-',name1)

for index1,name1 in zip(range(1,len(L)+1),L):
    print(index1, '-', name1)



#迭代dict
"""
dict对象本身就是可迭代对象，用 for 循环直接迭代 dict，可以每次拿到dict的一个key。

如果我们希望迭代 dict 对象的value，应该怎么做？

dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v
# 85
# 95
# 59
如果仔细阅读Python的文档，还可以发现，dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.itervalues()
# <dictionary-valueiterator object at 0x106adbb50>
for v in d.itervalues():
    print v
# 85
# 95
# 59
那这两个方法有何不同之处呢？

1. values() 方法实际上把一个 dict 转换成了包含 value 的list。

2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。

3. 打印 itervalues() 发现它返回一个 <dictionary-valueiterator> 对象，这说明在Python中，for 循环可作用的迭代对象远不止 list，tuple，str，unicode，dict等，任何可迭代对象都可以作用于for循环，而内部如何迭代我们通常并不用关心。

如果一个对象说自己可迭代，那我们就直接用 for 循环去迭代它，可见，迭代是一种抽象的数据操作，它不对迭代对象内部的数据有任何要求。
"""
print("\n\n")
d = {'Adam':96,'Lisa':85,'Bart':99}

#计算平均分
sum = 0.0
for score2 in d.values():
    sum = sum + score2
print("平均分：", sum / len(d))

print(d.values())   #values()方法取出字典的所有值
for score in d.values():
    print(score)

#print(d.itervalues())    #itervalues() 是python2中的方法
#for score1 in d.itervalues():
#    print(score1)

"""
items() 方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value：
items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以，
 iteritems() 不占用额外的内存。
"""

print("\n")
print(d.items())  #将dict字典转化为包含tuple的list
sum1 = 0.0
for key,value in d.items():
    print(key, ":", value)
    sum1 = sum1 + value
print("平均分：", sum1 / len(d))