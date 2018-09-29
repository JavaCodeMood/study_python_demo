#python字典类型
"""
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

注意：

1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。

"""

dict = {}  #创建一个空字典
dict['one'] = "万杯觥筹不过是提醒寂寞"
dict['two'] = "没了你"
dict[1] = "天国虽热闹"
dict[2] = "但我不愿久留"
print(dict)  #输出字典
print(dict['one'])  #输出键为one的值
print(dict['two'])  #输出键为two的值

userdict = {'name':"liuhefei",'age':18,'sex':"男"}
print(userdict)
print(userdict.keys())   #输出字典的所有键
print(userdict.values()) #输出字典的所有值

