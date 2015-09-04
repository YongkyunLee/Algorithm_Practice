import random
import math

example = [3, 5, 9, 8, 6, 2, 7, 1, 10, 4]

def int_list(file):
    integer_list = []
    text = open(file)
    text_read = text.read()
    text_list = text_read.splitlines()
    for i in range(0, len(text_list)):
        integer_list.insert(i, int(text_list[i]))
    return integer_list

def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

class Quicksort:
    def __init__(self):
        self.count = 0

    def choose_pivot(self, array, lo, hi):
        #pivot_num = lo #choosing the first element as pivot
        #pivot_num = hi #choosing the final element as pivot
        if (hi - lo)%2 == 1: #choosing the "median-of-three" as pivot
            mid = int(lo + (hi-lo-1)/2)
            pivot = median(array[lo], array[mid], array[hi])
        else:
            mid = int(lo + (hi-lo)/2)
            pivot = median(array[lo], array[mid], array[hi])
        #print(pivot)
        pivot_num = array.index(pivot)
        return pivot_num

    def partition(self, array, pivot_num, lo, hi):
        self.count += hi - lo
        pivot = array[pivot_num]
        array[lo], array[pivot_num] = array[pivot_num], array[lo]
        i = lo + 1
        for j in range(lo + 1, hi + 1):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[lo], array[i-1] = array[i-1], array[lo] #swap
        
    def qsort(self, array, lo, hi):
        if hi <= lo:
            return array
        pivot_num = self.choose_pivot(array, lo, hi)
        pivot = array[pivot_num]
        self.partition(array, pivot_num, lo, hi)
        self.qsort(array, lo, array.index(pivot)-1)
        self.qsort(array, array.index(pivot)+1, hi)

#input_list = example
input_list = int_list("c:\\Users\\Yongkyun\\Desktop\\python practice\\algorithm\\QuickSort.txt")
comp = Quicksort()
comp.qsort(input_list, 0, len(input_list)-1)
print(comp.count)
