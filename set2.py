#!/usr/bin/python3
# coding:utf-8

"""
创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
s = set(['A', 'B', 'C'])
set集合是无序的，set集合不能包含重复的元素
访问 set中的某个元素实际上就是判断一个元素是否在set中。
"""

s = set(['A','B','C','D','E','F','A','B'])
print("set集合：", s)
print('set集合长度：', len(s))
#判断某个元素是否在有序集合中
print('B' in s)
print('G' in s)

"""
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。

set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。

最后，set存储的元素也是没有顺序的。
"""

weekdays = set(['MON','TUE','WED','THU','FRI','SAT','SUN'])
weekday = str(input("请输入星期号：\n"))
if weekday in weekdays:
    print("今天是：", weekday)
else:
    print("错误的输入")

#遍历 set 和遍历 list 类似，都可以通过 for 循环实现。
for day in weekdays:
    print(day)

score = set([('Adam', 95),('Lisa',85),('Bart',59)])
for x in score:
    print(x[0] + ":", x[1])

"""
set存储的是一组不重复的无序元素

更新set主要做两件事：
一是把新的元素添加到set中，二是把已有元素从set中删除。
"""

num = set([1,2,3,4])
num.add(5)   #添加元素
num.add(6)
num.add(7)
num.add(6)
num.add(7)
print(num)

num.remove(1)  #删除元素
num.remove(4)
#num.remove(100)  #删除的元素不存在，报错
print(num)

s1 = set(['Adam','Lisa','Paul'])   #set集合
L1 = ['Adam', 'Tom', 'Pite', 'Boy', 'Lisa']  #列表
for name in L1:
    if name in s1:   #判断元素name是否在set集合中，在就删除，不在就添加
        s1.remove(name)
    else:
        s1.add(name)
print("s1 = ", s1)
print("L1 = ", L1)