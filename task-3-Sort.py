import random
import math
import json

strtrng = 0
endrng = 100
array = []

for i in range(strtrng, endrng):
    array.append(random.randint(1, 99))
print('начальный массив -', array)

array_bubble = array

def bubblesort(x):
    for i in range(endrng-1):
        for j in range(endrng-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]            
    return x

print('результат пузырьковой сортировки -', bubblesort(array_bubble))

array_quick = array

def quicksort(x):
   if len(x) <= 1:
       return x
   else:
       q = random.choice(x)
   l_x = [n for n in x if n < q]
   e_x = [q] * x.count(q)
   b_x = [n for n in x if n > q]
   return quicksort(l_x) + e_x + quicksort(b_x)

print('результат быстрой сортировки', quicksort(array_quick))

array_choise = array

def choise_sort(x):
    n = len(x)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if x[j] < x[m]:
                m = j
        x[i], x[m] = x[m], x[i]
    return x

print(choise_sort(array_choise))