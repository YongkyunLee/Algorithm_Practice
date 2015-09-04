import random

example = [5, 6, 11, 4, 3, 9, 10, 7, 2, 1, 8]

def choose_pivot(array, lo, hi):
    pivot_num = random.randint(lo, hi) #choosing pivot
    pivot = array[pivot_num]
    #print(pivot)
    return pivot

def partition(array, pivot, lo, hi):
    array.remove(pivot)
    array.insert(lo, pivot) #moving the pivot to the 1st place of the sector
    #print(array)
    i = lo + 1
    for j in range(lo + 1, hi + 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i] #swap
            i += 1
    array[lo], array[i-1] = array[i-1], array[lo] #swap
    #print(array)

def quicksort(array, lo, hi):
    if hi <= lo:
        return array
    pivot = choose_pivot(array, lo, hi)
    partition(array, pivot, lo, hi)
    quicksort(array, lo, array.index(pivot)-1)
    quicksort(array, array.index(pivot)+1, hi)
    #return array
    
quicksort(example, 0, len(example)-1)
print(example)
