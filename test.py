#-*- coding: utf-8 -*-
array = [1,2,3,6,5,4]
for i in range(len(array)):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array
