#!/usr/bin/python3
# coding:utf-8

"""
可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：
通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。

"""
d = {
    'Adam': 100,
    'Lisa': 76,
    'Tom': 88,
    'Tour': 79,
    'Toy': 98
}

for x in d:
    print(x)

#判断key是否存储
if 'Piter' in d:
    print("判断Piter是否存在：",d['Piter'])

print("判断key是否存在：", d.get('Tom'))

print("字典：", d)

"""
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。

不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。

由于dict是按 key 查找，所以，在一个dict中，key不能重复。

dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
dict字典是无序的，不能使用dict存储有序集合

dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，
都可以作为 key。但是list是可变的，就不能作为 key。
不可变这个限制仅作用于key，value是否可变无所谓
"""

dict1 = {
    '123': [1,2,3,4,5],   #key是str， value是list
    123: '123',  #key是int，value是str
    ('a','b','c'): True  #key是tuple，并且tuple的每个元素都是不可变对象，value是boolean
}

print(dict1)

"""
dict是可变的，也就是说，我们可以随时往dict中添加新的 key-value。
如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value
"""

dict1['abc'] = "你好"
dict1[999] = '999'

print("dict1= ",dict1)

#使用for循环遍历字典
for key in d:
    print(key + ":", d[key])

