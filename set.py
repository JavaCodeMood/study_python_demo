#python set集合
"""
集合（set）是一个无序不重复元素的序列。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

color = {'red','blue','yellow','green','black','pink','red','blue','white'}
print(color)  #输出集合，重复的元素会被删除

#成员测试
if 'yellow' in color :
    print("yellow在集合color中")
else :
    print("yellow不在集合中")

#set可以进行集合运算
a = set('abcdefabfes')   #使用set函数创建两个集合
b = set('afgdfsbcddsldjkhgasjh')

print(a)   #输出集合元素
print(b)

print(a - b)  #a和b的差集
print(a | b)  #a和b的并集
print(a & b)  #a和b的交集
print(a ^ b)  #a和b中不同时存在的元素
print("集合不能拼接：",a + b)  #集合不能拼接