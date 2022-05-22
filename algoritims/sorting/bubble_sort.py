# consiste em ordenar um array iterando por ele e invertendo o sucessor com o seu antecessor, caso o antecessor seja maior que o sucessor
# seguindo essa lógica, o maior valor será jogado para o fim da lista, e ao retomar o processo, o número de iterações necessárias para jogar o segundo maior
#valor para o fim da lista ira ser menor

def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+ 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

array = [4,2,1,9,0,3,7,8,6,5]
bubble_sort(array)