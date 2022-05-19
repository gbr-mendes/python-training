# podemos usar construtores similares ao das linked lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # como nas linked lists, cada nó só tem a referencia do elemento seguinte. No caso da pilha, esse elemento está abaixo.


class Stack:
    def __init__(self):
        self.top = None # como as operações só ocorrem em uma ponta nas pilhas, precisamos apenas da referência do elemento que está no topo
        self.length = 0
    
    def push(self, value):
        #Método para incluir um elemento na pilha. Similar as listas.
        # podemos atingir 0(1) escolhendo a ponta certa para se trabalhar, similar aos métodos prepend das linked lists
        new_node = Node(value)
        top = self.top # pegamos a referência do elemento que está no topo
        self.length +=1 # como o elemento sempre será inserido, incrementamos o length de cara para não repetir código

        if not top:
            self.top = new_node
            return True
        new_node.next = top # aqui eu referencio o next como o elemento que estará abaixo do novo nó, para atingir 0(1)
        self.top = new_node
        return True
    
    def pop(self):
        top = self.top # armazenamos o elemento que se encontra no topo da pilha
        if top is None: # caso a pilha esteja vazia retornamos none
            return None
        self.top = top.next # se a pilha não esta vazia, setamos o top para armazenar o elemento que estava abaixo do elemento a ser removido
        self.length -=1
        top.next = None # Removemos definitivamente da lista
        return top
    
    def print_stack(self):
        temp = self.top # armazenamos a referencia do elemento do topo
        if self.length == 0:
            print('[]')
            return
        print('[', end="") # utilizo essa estratégia para imprimir a pilha em forma de lista
        for _ in range(self.length): #iteramos a pilha
            if temp:
                if temp.next:
                    print(temp.value, end=",")
                else:
                    print(str(temp.value) + ']')
                temp = temp.next # alteramos a referência de temp para iterar por toda a pilha


stack = Stack()
# stack.push(0)
# stack.push(1)
# stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.print_stack()