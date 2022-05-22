# desafio2 - somar elementos do array o lado, sem usar um laço: [4,2,1,9,0,3,7,8,6,5]

def soma_array(array, resultado=0, n=0):
    if n <= len(array) - 1:
        resultado += array[n]
        n += 1
        return soma_array(array, resultado, n)
    else:
        return resultado


meu_array = [1, 2, 3]  # 45
print(soma_array(meu_array))
