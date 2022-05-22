# desafio1 - ordenar o seguinte array de forma crescente e decrescente: [4,2,1,9,0,3,7,8,6,5]

def ordena_array_crescente(meu_array):
    for i in range(len(meu_array) - 1, 0, -1):
        for j in range(i):
            if meu_array[i] < meu_array[j]:
                meu_array[i], meu_array[j] = meu_array[j], meu_array[i]
    return meu_array


def ordena_array_decrescente(meu_array):
    for i in range(len(meu_array) - 1, 0, -1):
        for j in range(i):
            if meu_array[i] > meu_array[j]:
                meu_array[i], meu_array[j] = meu_array[j], meu_array[i]
    return meu_array


print(ordena_array_crescente([4, 2, 1, 9, 0, 3, 7, 8, 6, 5]))
print(ordena_array_decrescente([4, 2, 1, 9, 0, 3, 7, 8, 6, 5]))
