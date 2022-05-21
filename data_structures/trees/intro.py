# uma arvore, em essência é uma linked list, no entanto, seus nós possem uma particularidade
# cada nó pode apontar para vários elementos. Mas, o mais comum para estudos básico são nós que apontam para até dois elementos
# nesse caso temos árvores binárias
# nomenclaturas:
    # full tree - cada nó aponta para ou dois elementos, ou nenhum elemento
    # perfect tree -  cada nó de cada camada a arvore é completamente preenchido com filhos e os nós da ultima camada, não apontam para ninguém
    # complete tree - a árvore é totalmente preenchida, da esquerda para direita

# UMA ÁRVORE DE BUSCA BINÁRIA, tem a particularidade de, a partir do nó original, as próximas inserções se dão,
    # com base no valor do seu parent. Por exemplo, o nó inicial tem o valor de 50, caso o nó que venha a ser inserido
    # seja maior que 50, ele é inserido a direita, e caso seja, menor que 50, é inserido a esquerda
    # essa lógica se estende por toda os nós da hierarquia, até que seja possível fazer a inserção em um posição livre

# BIG 0 de árvore de busca binária
# Considerando um nó que possui o left e right apontando para outros nós, temos ao todo uma árvore com 3 nós
# a primeira camada da árvore possuí apenas um nó. Por se tratar de uma árvore binária, podemos, escrever da seguinte forma:
# 1 = 2¹ - 1
# considerando a segunda camada, temos ao todo 3 nós, então podemos escrever da seguinte forma:
# 3 = 2² - 1
# essa lógica se estende. E considerando isso podemos definir o seu big 0
# No melhor dos casos, o big 0 de uma  árvore de busca binária é de 0(log n), pois se aplica o conceito de dividir e conquistar
# no entanto, normalmente avaliamos o big 0 pelo pior caso
# O pior caso, seria que a cada inserção, o valor a ser inserido fosse maior que o valor original.
# nesse cenário, o nó é sempre inserido a direita do seu antecessor, formando uma simples linked list
# e como foi visto, o big0 de uma linked list, para inserção é de 0(n)
    