#!/usr/bin/python3
#coding:utf-8

#for循环
list = ["Java","c","c++","python","html","css","javaScript","jquery","go"]
for i in list:
    print(i,end = ",")
    #print(i)

print()
# for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
for x in list:
    if x == "Java":
        print("1-》一处编译到处运行")
        break
    print("循环数据：",x)
else:
    print("没有循环数据")


for m in list:
    if m == "Java":
        print("2-》一处编译到处运行")
    if m == "python":
        print("人生苦短，我用python")
else:
    print("list列表")