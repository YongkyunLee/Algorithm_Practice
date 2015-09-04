import random

example = [5, 6, 4, 3, 9, 7, 2, 1, 8]

def partition(array):
    pivot_num = random.randint(0, len(array)-1)
    pivot = array[pivot_num]
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
    #print(pivot)
    #print(array)
    return [left, pivot, right]

def quicksort(array):
    if len(array) == 1:
        return array
    elif len(array) == 0:
        return array
    partition_result = partition(array)
    #print(partition_result)
    return quicksort(partition_result[0])+[partition_result[1]]+quicksort(partition_result[2])
    
print(quicksort(example))            
