#  Linked lists, diferente de listas comuns, não possuem indices
# Diferente das listas comuns que são espaços contíguos na memória, linked lists são espalhadas
# Em linked lists, temos uma variável chamada head, que aponta para o primeiro elemento da lista,
# e temos outra variável chamada tail, que aponta para o último elemento
# Cada elemento aponta para o próximo, formando uma cadeia, e o último elemento aponta para none
#___________________________________________________________________
#Big 0 de linked lists
# Para o método append, para incluir um elemento ao final da lista, temos 0(1)

# Para o método pop, diferentemente de listas comuns, temos que fazer o set da variável tail
# a qual tem que apontar para o elemento que antes era o penúltimo. E, como cada elemento sabe qual é o seu sucessor,
# mas não qual é o seu antecessor, devemos iterar a lista e encontrar o elemento que seu next aponta para None, e então setar
#tail para esse elemento ou seja, temos O(n), pois as iterações aumentam proporcionalmente a n

#Para o método de inserir um elemento ao inicio da lista, temos 0(1), Pois temos apenas que setar a variável head para esse elemento
# e setar como next desse elemento o que antes era o primeiro
# Para remover o primeiro elemento, também temos 0(1), pois podemos setar a variável head para o next do primeiro elemento

# Para inserir um elemento no meio da lista, primeiro temos que achar o elemento na posição desejada
# Dessa forma, temos que iterar pela lista, logo, temos 0(n). O mesmo ocorre com a remoção
