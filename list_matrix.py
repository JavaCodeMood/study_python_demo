#!/usr/bin/python3
#coding:utf-8

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print("matrix=",matrix)

#变换矩阵
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print("transposed=",transposed)

print("----------------")

transposed1 = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed1.append(transposed_row)
print("transposed1=",transposed1)