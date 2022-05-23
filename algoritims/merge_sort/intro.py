# a ideia por trás do merge sort consiste em separar uma lista dividindo ao meio até que cada elemento corresponda a uma lista
# por exemplo, a lista [1,5,6,8,4,3] se tornaria [1], [5], [6], [8], [4], [3]
# em seguida, fazemos a ordenação em pares

# Para isso, precisamos de uma helper function chamada merge
# essa função pega duas listas e itera por elas fazendo a comparação entre seus items e armazenando eu uma nova lista os maiores
# assim que uma das listas estiver vazia, os elementos da segunda são comparados e inseridos na lista em ordem

from operator import le


def merge(list1, list2):
    combined = []
    i = 0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined

# print(merge([1,2,7,8], [3,4,5,6]))

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([3,1,4,2]))