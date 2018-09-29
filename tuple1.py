#!/usr/bin/python3

#python元组

tuple1 = ("red","blue","yellow",1,2,3)
tuple2 = (1,2,3,4,5,6)
print("tuple1[0]=", tuple1[0])
print("tuple2[2:]=",tuple2[2:])
print("tuple2[2:5]=", tuple2[2:5])

#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tuple3 = tuple1 + tuple2
print("拼接后的元组：",tuple3)

#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tuple2
print("删除后的元组：",tuple2)

#统计元组的元素个数
print("元组1元素个数：",len(tuple1))
print("元组2元素个数：",len(tuple2))

#判断某个元素是否在元组中
if ("red" in tuple1):
    print("red元组在tuple1中")
else:
    print("red元素不在tuple1中")




