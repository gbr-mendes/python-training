class Node:
    def __init__(self, value): # os nós da árvore de busca binária possuem dois atributos, left e right, além do valor
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None # para desenvolvermos a árvore, precisamos manter apenas a referência de sua raiz
    
    def insert(self, value):
        # método para inserção de valores
        new_node = Node(value) # primeiro criamos o nó a ser inserido
        if self.root is None: # caso a raiz esteja vazia, basta apontar a raiz para o novo nó
            self.root = new_node
            return True
        else:# caso contrário, precisamos iterar pelos nós seguindo alguns critérios
            temp = self.root # armazenamos a referencia da raiz para iniciar a iteração
            while temp: # iniciamos o laço com a referência da raiz
                if new_node.value == temp.value: # caso o valor do novo nó já esteja presente na arvore, não fazemos a inserção e quebramos o laço
                    return False
                elif new_node.value > temp.value: # caso o valor do novo nó seja maior do que o nó do momento da iteração, entramos a direita
                    if temp.right: #  caso a direita do nó do momento da iteração esteja ocupada por outro nó, alteramos a referencia de temp para passar para a próxima iteração
                        temp = temp.right
                    else: # caso a direita esteja livre, fazemos a inserção
                        temp.right = new_node
                        return True
                else: # caso o valor do novo nó seja menor do que o valor do nó do momento da iteração, entramos a esquerda
                    if temp.left: # caso a esquerda do nó do momento da iteração esteja ocupada, alteramos a referencia de temp para continuarmos a iteração
                        temp = temp.left
                    else:# caso a esquerda do nó do momento da iteração esteja livre, fazemos a inserção do novo nó
                        temp.left = new_node
                        return True

    def contains(self, value):
        # método para verificação da existência de dado valor
        # primeiro verificamos se a árvore está vazia, caso esteja, retornamos false
        if self.root is None:
            return False
        elif self.root.value == value: # verificamos se o valor desejado é igual ao primeiro elemento
            return True
        else:
            # caso contrário, iniciamos a comparação do valor, sempre olhando para esquerda ou direita
            # essa é uma das vantagens da árvore de busca binária, pois não temos que iterar todo os seus valores para encontrar algo específico
            temp = self.root # armazenamos referência da raiz, para iniciar o laço
            while temp:
                if temp.value < value: # caso o valor a ser buscado seja menor que o valor de temp na iteração atual, entramos a direita
                    if temp.right is None: # caso a direita de temp no momento da iteração no momento do laço esteja vazia, o valor desejado não existe
                        return False
                    else:
                        if temp.right.value == value:
                            return True
                        else:
                            temp = temp.right # caso o valor não seja encontrado alteramos temp, para continuar a iteração
                else:
                    # caso o valor buscado seja menor que o valor de temp no momento da iteração, entramos a esquerda
                    if temp.left is None:
                        return False# caso a esquerda de temp esteja vazia, o valor não existe
                    else:
                        if temp.left.value == value:
                            return True # caso o valor de left seja o valor desejado, retornamos true
                        else:
                            temp = temp.left # caso contrário, alteramos a referencia de temp para continuarmos a iteração
    
    def minimum_value(self, value=None):
        # método para retornar o menor valor da árvore a partir de um valor especifico
        # para alcançar esse objetivo, basta navegar sempre pela esquerda do nó do momento da iteração
        if self.root is None:
            return None # caso a árvore esteja vazia, retornamos none
        
        if value is None:
            value = self.root.value # caso value não seja passado, iniciamos a partir da raiz
        
        if not self.contains(value):
            # caso o valor passado não esteja presente na árvore, retornamos None
            return None
        temp = self.root #armazenamos a referencia da raiz da árvore para começar a iteração
        while temp.value != value: #alteramos a referencia de temp até encontrar o valor base para a busca do menor valor
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        # ao final dessa primeira iteração, temp aponta para o valor passado como referencia
        # a partir daqui basta buscar o menor valor
        while temp.left:
            temp = temp.left # sempre entramos a esquerda, ao final, teremos o menor valor
        return temp.value

        

bst = BinarySearchTree()

bst.insert(50)
bst.insert(47)
bst.insert(52)
bst.insert(54)
bst.insert(51)
bst.insert(43)
bst.insert(49)

print(bst.minimum_value(50))