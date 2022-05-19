def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)
# 0(n^2) nesse caso, percebe-se um crescimento do tempo em forma de parabola. o número de interações será n*n
# Por isso, sempre que possível, deve-se evitar usar um laço dentro de outro. No exemplo acima, ocorrem 100
    # iterações, logo 10*10. Mesmo que sejam mais laços encadeados. sempre será simplificado como n^2