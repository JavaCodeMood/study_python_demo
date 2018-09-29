#python列表类型
"""
加号 + 是列表连接运算符，星号 * 是重复操作
与Python字符串不一样的是，列表中的元素是可以改变的
List内置了有很多方法，例如append()、pop()等等

注意：

1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。
"""

list = ['a','b','c','d',1,2,3,4,5,3.14,0.618]
list1 = ['天国虽热闹',"没了你","万杯觥筹",'只不过',"是提醒寂寞"]
print(list)   #输出完整的列表
print(list1)
print(list[0])  #输出列表的第一个元素
print(list[1:5])  #输出列表的第2个元素到5个元素、
print(list[3:])  #输出列表第4个元素后的所有元素
print(list1 * 2)  #输出2次列表
print(list + list1)  #连接两个列表

print("-----------------------")
list2 = [1,2,3,4,5,6]
print(list2)
list2[0] = 6
list2[3] = 1
print(list2)

list2.append(100)  #向列表中添加元素
list2.append(3.12425)
print(list2)
list2.pop(1)  #删除列表中下标为1的元素，列表下标从0开始
print(list2)
list2.pop(-1)  #删除列表中最后一个元素
print(list2)

print("----------------")
exchange_threads = []
print(exchange_threads)
exchange_threads.append("你好")
print(exchange_threads)