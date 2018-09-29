#!/usr/bin/python3
# coding:utf-8

myList = [100,200,9,52,5,0,1,100]

print("100出现的次数: ",myList.count(100))

#在指定位置插入数据
myList.insert(2,66)
myList.insert(5,1000)
print("myList=",myList)

#添加元素
myList.append(20)
myList.append(15)
print("myList = ",myList)

#返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print("元素9在列表中的位置：",myList.index(9))

#删除某个元素
myList.remove(100)
print("删除100，列表为：",myList)

#倒排列表中的元素
myList.reverse()
print("列表倒排为：",myList)

#对列表的元素进行排序
myList.sort()
print("列表排序为：",myList)

#复制列表
myList1 = myList.copy()
print("myList1=",myList1)

#从列表的指定位置移除元素
myList1.pop(5)
print("移除一个元素后：", myList1)

#移除列表所有项
myList.clear()
print("移除列表元素后：",myList)

#将列表当作堆栈使用 append()进栈，pop()出栈
stack = [3,4,5]
#进栈
stack.append(1)
stack.append(6)
print("stack=",stack)
#出栈
stack.pop()
print("stack=",stack)
stack.pop()
print("stack=",stack)