class Node:
    def __init__(self, value):
        self.value = value
        self.before = None # O elemento da fila sempre aponta para o seu antecessor


class Queue:
    def __init__(self):
        self.first = None # Como a inserção se da em uma ponta e a remoção em outra, precisamo referenciar essas pontas
        self.last = None
        self.length = 0
    
    def enqueue(self, value):
        #método para inclusão de elemento em fila
        # todo elemento que entra na fila passa a ser o último elemento
        # primeiro criamos o nó
        new_node = Node(value)
        self.length += 1 # como o elemento sempre será inserido, de cara eu incremento o length
        last = self.last
        if not last: # verificamos se a fila está vazia
            self.last = new_node
            self.first = new_node # caso esteja vazia, o novo nó será o ultimo e primeiro ao mesmo tempo
            return True

        # caso a fila não esteja vazia
        last = self.last # armazenamos temporariamente o elemento que encontra-se em último
        last.before = new_node # o elemento que era o ultimo passa a er o atributo before, apontando para o novo node que é o último
        self.last = new_node # o novo nó passa a ser o último da fila
        
        return True
    
    def dequeue(self):
        # esse método remove o primeiro elemento da fila
        if self.length == 0: # caso a lista esteja vazia, não prosseguimos
            return None
        if self.length == 1:
            self.first = None
            self.last = None
            return True

        first = self.first # armazenamos a referencia do primeiro elemento
        self.first = first.before # mudamos a referencia do primeiro elemento para o elemento que antes er o segundo
        first.before = None # removemos definitivamente o elemento da fila
        self.length -=1 # decrementamos o length da fila
        return True

    def print_queue(self):
        temp = self.first
        if not temp: # caso a lista esteja vazia, apenas exibimos um array vazio
            print('[]')
            return
        print('[', end="")
        for _ in range(self.length):
            if temp:
                if(temp.before):
                    print(temp.value, end=",")
                else:
                    print(str(temp.value) + ']')
            temp = temp.before


queue = Queue()
# queue.enqueue(0)
queue.enqueue(1)

queue.dequeue()
print(queue.first)
print(queue.last)
queue.print_queue()