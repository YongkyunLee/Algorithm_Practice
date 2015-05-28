import math

input_list = [1, 8, 5, 3, 9, 10, 7, 6, 2, 4]
sort_list = []
operation_num = math.floor(math.log2(len(input_list))+1)
#print(operation_num)
for i in range(0, operation_num):
    sort_list.insert(i, [])
#print(sort_list)
for i in range(0, len(input_list)):
    sort_list[0].insert(i, [input_list[i]])
#print(sort_list)
    
def merge(left_list, right_list):
    i = 0
    j = 0
    merge_list = []
    for k in range(0, len(left_list)+len(right_list)):
        if i == len(left_list):
            merge_list.insert(k, right_list[j])
            j += 1
            continue
        if j == len(right_list):
            merge_list.insert(k, left_list[i])
            i += 1
            continue
        if left_list[i] < right_list[j] and i < len(left_list) and j < len(right_list):
            merge_list.insert(k, left_list[i])
            i += 1
            continue
        if left_list[i] > right_list[j] and i < len(left_list) and j < len(right_list):
            merge_list.insert(k, right_list[j])
            j += 1
            continue
    return merge_list

for i in range(0, operation_num):
    for x in range(0, math.floor(len(sort_list[i])/2)):
        sort_list[i+1].insert(x, merge(sort_list[i][x*2], sort_list[i][x*2+1]))
    
print(sort_list[operation_num-1])
