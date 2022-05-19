def print_items(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_items(10)
# O(n) cresce proporcionalmente ao número de entradas. Quanto maior n, maior o tempo de execução
# para casos de 0(n+n), simplifica-se para apenas n. Esse caso pode ser exemplificado com dois loops independentes
    # utilizam o mesmo n, logo n+n