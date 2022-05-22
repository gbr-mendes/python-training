# nesse algorítimo, armazenamos o índice do menor elemento, e caso encontremos um elemento menor que ele, fazemos um swap

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        if min_index != i:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]
    return my_list

array = [4,2,1,9,0,3,7,8,6,5]
print(selection_sort(array))