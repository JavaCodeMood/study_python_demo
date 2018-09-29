#!/usr/bin/python3
# coding:utf-8

"""
python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
"""

import pickle

#使用pickle模块将数据对象保存到文件中
data1 = {'a':[1,2.0,3,6,10,1100],
         'b':('string',u'Unicode string'),
         'c':None}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open('data.pk1','wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)
output.close()