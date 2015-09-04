import random

example = [3, 5, 6, 2, 1, 4]

def int_list(file):
    integer_list = []
    text = open(file)
    text_read = text.read()
    text_list = text_read.splitlines()
    for i in range(0, len(text_list)):
        integer_list.insert(i, int(text_list[i]))
    return integer_list

class Quicksort:
    def __init__(self):
        self.count = 0

    def partition(self, array):
        pivot = array[len(array)-1]
        self.count += len(array)-1
        array.remove(pivot)
        array.insert(0, pivot)
        i = 1
        for j in range(1, len(array)):
            if array[j] < pivot:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
                i += 1
        array.remove(pivot)
        array.insert(i-1, pivot)
        left = []
        right = []
        for i in range(0, array.index(pivot)):
            left.insert(i, array[i])
        for j in range(0, len(array)-array.index(pivot)-1):
            right.insert(j, array[array.index(pivot)+1+j])

        return [left, right]

    def qsort(self, array):
        if len(array) == 0:
            return array
        elif len(array) == 1:
            return array
        partition_result = self.partition(array)
        self.qsort(partition_result[0])
        self.qsort(partition_result[1])

input_list = int_list("c:\\Users\\Yongkyun\\Desktop\\python practice\\algorithm\\QuickSort.txt")
comp = Quicksort()
comp.qsort(input_list)
print(comp.count)
