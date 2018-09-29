#!/usr/bin/python3

#python字典

dict = {}  #空字典
dict1 = {"name":"liuhefei","age":20,"sex":"男","address":"shenzhen"}
#获取字典的值
print(dict1["name"],"->",dict1["age"],"->",dict1["sex"])
#print(dict1["phone"])  #不存在的键，将会报错

dict1["age"] = 22   #更新age
dict1["phone"] = "18295514401"  #添加新元素
print("打印字典：",str(dict1))   #打印字典

del dict1["name"]   #删除字典元素
print("打印字典：",str(dict1))

print("字典元素个数：",len(dict1))
print("字典类型：",type(dict1))

#复制字典
dict2 = dict1.copy()
print("dict2=",str(dict2))

#返回指定键的值
print("键phone对应的值：",dict1.get("phone"))

#判断某个键是否存在字典中
if ("name" in dict1):
    print("键name存在字典dict1中")
else:
    print("键name不存在字典dict1中")

#以列表返回可遍历的元组数组
print("遍历：",dict1.items())

#返回一个迭代器，可以使用list来转换为列表
print("字典键：",dict1.keys())

#为字典的某个键设置默认值
dict1.setdefault("height","170")
print(str(dict1))

#返回一个迭代器，可以使用list来转化为列表
print("字典值：",dict1.values())

#删除字典给定键所对应的值、
dict1.pop("height")
print("删除height键之后：",str(dict1))

#随机返回并删除字典中的一对键和值(一般删除末尾对)。
dict1.popitem()
print("随机返回并删除字典中的一个键值对：",str(dict1))

dict1.clear()    #清空字典
print("字典清空后：",str(dict1))

del dict   #删除字典
print("dict",str(dict))
