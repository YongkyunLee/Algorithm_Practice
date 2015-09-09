import random
import math

def adj_list(file): #converting the given text file into a list
    temp = []
    adj_list = []
    text = open(file)
    lines = text.readlines() #import lines in txt as string
    for i in range(0, len(lines)): #converting string into lists of integers
        adj_list.append(lines[i].split())
        for j in range(0, len(adj_list[i])):
            adj_list[i][j] = int(adj_list[i][j])
    return adj_list
    
def choose_edge(array): #choosing edge to contract
    vertex_1 = random.randint(0, len(array)-1) #choosing a vertex to be contracted
    vertex_1_val = array[vertex_1][0]
    vertex_2_num = random.randint(1, len(array[vertex_1])-1) #choosing a vertex linked to vertex_1
    vertex_2_val = array[vertex_1][vertex_2_num] #value of vertex 2
    for i in range(0, len(array)): #location of vertex 2 in the adjacency list
        if array[i][0] == vertex_2_val:
            num = i
    vertex_2 = num
    vertex = [vertex_1, vertex_2, vertex_1_val, vertex_2_val]
    return vertex 

def solve(array):
    if len(array) == 2:
        #print(array)
        num = len(array[0])-1
        return num
    vertex = choose_edge(array)
    #print(vertex)
    array[vertex[0]].extend(array[vertex[1]]) #contracting two chosen vertices
    array.remove(array[vertex[1]])
    #print(array)
    for j in range(0, len(array)): #merging two contracted vertices to one vertex
        i = 0
        test_contract = True
        while test_contract:
            i += 1
            if array[j][i] == vertex[3]:
                array[j].remove(vertex[3])
                array[j].insert(i, vertex[2])
            if i == len(array[j])-1:
                test_contract = False
    test_selfloop = True
    #print(array)
    k = 1
    if vertex[0] > vertex[1]: #setting the right vertex for selfloop erase
        vertex[0] -= 1
    while test_selfloop: #erasing self-loops of contracted vertex
        if array[vertex[0]][k] == vertex[2]:
            array[vertex[0]].pop(k) #remove module erases the first item spotted ==> to be fixed!!!!
        else:
            k += 1
        if k == len(array[vertex[0]]):
            test_selfloop = False
    return solve(array)
    #print(array)
    

input_list = 'c:\\Users\\Yongkyun\\Desktop\\python practice\\algorithm\\kargerMinCut.txt'
#input_list = 'c:\\Users\\Yongkyun\\Desktop\\python practice\\algorithm\\practice.txt'
#print(adjency_list)
trial = adj_list(input_list)
iteration_num = len(trial)
min_cut = solve(trial)
for i in range(0, int(iteration_num/10)):
    adjency_list = adj_list(input_list)
    cut = solve(adjency_list)
    if cut < min_cut:
        min_cut = cut
    #print(cut)

print(min_cut)
