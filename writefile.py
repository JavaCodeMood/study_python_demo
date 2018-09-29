#!/usr/bin/python3
# coding:utf-8

#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。

def newfile(filename):
    #打开一个文件
    f = open("D:/lhfcode/Python/"+filename+".txt", "w")
    num = f.write("人间虽热闹，没有了你，万杯觥筹只不过是提醒寂寞")
    print("字符数：", num)

    #关闭打开的文件、
    f.close()

if __name__=='__main__':
    filename = input("请输入文件名：")
    newfile(filename)
    print("文件名：", filename)