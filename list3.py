#!/usr/bin/python3
# coding:utf-8

#生成列表

"""
要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，我们可以用range(1, 11)：
range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""

# for list1 in range(1,10):
#    print(list1, end= " ")
print("list1 = ",[list1 for list1 in range(1,10)])

list2 = []
for x in range(1,11):
    list2.append(x * x)
print("list2 = ", list2)

#写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来，十分有用
list3 = [y*y for y in range(1,11)]
print("list3 = ", list3)

print("list4 = ", [a for a in range(1,60,3)])

#利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([b*(b+1) for b in range(1,100,2)])

print("\n-------------------------")
#for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
#字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}
tds = ['<tr><td>%s</td><td>%s</td></tr>' %(name, score) for name,score in d.items()]
print('<table>')
print('<tr><th>Names</th><th>Score</th></tr>')
print('\n'.join(tds))
print('</table>')

print("\n-------------------------")
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.items()]
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')

print("\n-------------------------")
"""
列表生成式的 for 循环后面还可以加上 if 判断
"""
list5 = [x * x for x in range(1,11) if x % 2 == 0]
print("list5 = ", list5)

#接收一个list，把list中的字符串转化为大写，忽略数字
def toUpper(L):
    return [x.upper() for x in L if isinstance(x, str)]

print(toUpper(['hello','world',100,90,'yellow']))

print("\n-------------------------")
"""
for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。

对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：

>>> [m + n for m in 'ABC' for n in '123']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
"""

L1 = []
for m in 'ABCD':
    for n in '1234':
        L1.append(m + n)

print("'ABCD'与’1234'的组合全排列：", L1)

#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
print ([100 * n1 + 10 * n2 + n3 for n1 in range(1,10) for n2 in range(10) for n3 in range(10) if n1 == n3])