import math

sort_list = []

def int_list(file):
    integer_list = []
    text = open(file)
    text_read = text.read()
    text_list = text_read.splitlines()
    for i in range(0, len(text_list)):
        integer_list.insert(i, int(text_list[i]))
    return integer_list

def merge(left_list, right_list):
    i = 0
    j = 0
    add_count = 0
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
            add_count += len(left_list)-i
            continue
    return [merge_list, add_count]

inv_count = 0
input_list = int_list('c:\\IntegerArray.txt')
#print(input_list)
operation_num = math.ceil(math.log2(len(input_list)))
for i in range(0, operation_num+1):
    sort_list.insert(i, [])
for i in range(0, len(input_list)):
    sort_list[0].insert(i, [input_list[i]])

for i in range(0, operation_num):
    mid = len(sort_list[i])/2
    for x in range(0, math.floor(mid)):
        sort_list[i+1].insert(x, merge(sort_list[i][x*2], sort_list[i][x*2+1])[0])
        inv_count += merge(sort_list[i][x*2], sort_list[i][x*2+1])[1]
    if len(sort_list[i])%2 == 1:
        sort_list[i+1].insert(math.ceil(mid)-1, sort_list[i][len(sort_list[i])-1])
#    print(inv_count)

#print(sort_list[operation_num][0])
print(inv_count)
