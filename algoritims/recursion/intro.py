# é uma função que chama a ela mesma, até que não chame mais
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))