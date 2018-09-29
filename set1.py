# !/usr/bin/python3

#python集合set
"""
集合（set）是一个无序不重复元素的序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }
"""

#创建一个set集合
set1 = {"orange","banana","pear","apple"}
print(set1)  #打印set集合

#创建一个空set集合
set2 = set()

#判断某个元素是否在集合set中
if ("orange" in set1):
    print("orange元素在集合set1中")
else:
    print("orange元素不在集合set1中")

a = set("abcdeffjfhf")
b = set("kjsahhasracasva")
c = set()

c = a - b  #集合差集
print(c)

c = a | b  #集合并集
print(c)

c = a & b  #集合交集
print(c)

c = a ^ b  #集合补集，a,b中不同时存在的元素
print(c)

#c = a + b  #集合不能拼接，报错
print(c)

#给集合添加元素
set1.add("dog")
set1.add("cat")
print(set1)

#给集合添加元素，参数可以是列表，元组，字典等
set1.update([1,2,3])  #列表参数
set1.update((100,200,300))  #元组参数
set1.update({"name":"liuhefei"})
print("最新集合：",set1)

#set.remove(x)移除集合中的x元素,如果元素不存在，则会发生错误。
set1.remove("name")
print(set1)

#set.discard(x)移除集合中的x元素，且如果元素不存在，不会发生错误
set1.discard(1)
print(set1)

#set.pop()  随机删除一个集合元素
set1.pop()
print("随机删除一个集合元素：",set1)

#len(set)  计算集合元素个数
print("集合元素个数：",len(set1))

#set.clear()清空集合
set1.clear()
print("清空集合后：",set1)