import random
import math
import json
strtrng = 0
endrng = 100
array = []
for i in range(strtrng, endrng):
    array.append(random.randint(1, 99))
print('начальный массив -', array)
array_p = array
for i in range(endrng-1):
    for j in range(endrng-i-1):
        if array_p[j] > array_p[j+1]:
            array_p[j], array_p[j+1] = array_p[j+1], array_p[j]
print('результат пузырьковой сортировки -', array_p)