#!/usr/bin/python3

list = [1,2,3,4,5,6,7,8,1,1,1]
list1 = [1,2,3,1.1,1.2,1.3,"何以解忧",'离愁别绪','月如钩']
list2 = [["red","blue","yellow","green"],["dog","cat","tiger"]]  #定义一个嵌套列表

print(list)   #打印列表
print(list1)
print(list2)

print(len(list1))  #获取列表长度
print(len(list2))

print("list的最大值：",max(list))
print("list的最小值：",min(list))

list.append(100)    #向列表中添加元素
list1.append("花飞尽")

del list1[2]   #删除列表元素
print(list1)

list1[4] = "断桥残雪"  #修改列表的元素
list1[5] = "感时花溅泪"
print(list1)

count = list.count(1)  #统计元素1在列表中出现的次数
print("元素1在列表list中出现的次数：",count)

list3 = ["小明","小花"]

#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list4 = list1.extend(list3)
print(list4)

#从列表中找出某个值第一个匹配项的索引位置
index = list.index(7)
print("index=",index)

#将一个列表对象插入到列表中
list2.insert(2,["fish","pig"])
print("list2 = ",list2)

print("list1反转：",list1.reverse())

list.pop(1)   #删除列表的元素
list.pop(3)
print("删除元素后的列表list：",list)

#对列表进行排序
list.sort()
print("排序后的列表list:",list)

#复制列表
list5 = list2.copy()
print("list5=",list5)

#清空列表
list1.clear()
print("清空列表：",list1)

#拼接列表
list6 = list2 + list3 + list3
print("list6=",list6)

