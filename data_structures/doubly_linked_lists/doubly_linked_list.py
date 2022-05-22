class Node:
    def __init__(self, value):
        # o construtor do nó é similar ao das linked lists
        # precisamos apenas de um atributo a mais para armazenar a referência do elemento anterior
        self.value = value
        self.next = None
        self.before = None #Ao ser instanciado, ambos(next e before) devem apontar para None


class DoublyLinkedList:
    def __init__(self):
        # O construtor é exatamente o mesmo das linked lists comuns
        self.head = None
        self.tail = None # definimos head e tail para armazenar a referencia do primeiro e ultimo elementos
        self.length = 0 # determinamos que a lista começa vazia
    
    def append(self, value):
        # método para inclusão de nó ao final da lista 0(1)
        # temos dois casos a serem avaliados. Quando  lista está vazia e quando ela já possui elementos
        # primeiro criamos o nó
        new_node = Node(value)
        # verificamos se a lista esta vazia:
        if self.length == 0:
            self.head = new_node # apontamos o head e o tail para o novo nó
            self.tail = new_node
            self.length += 1 # incrementamos o length da lista
            return True
        else:
            temp = self.tail # armazenamos a referência do último elemento
            temp.next = new_node # o último elemento tem seu next apontado para o novo nó
            new_node.before = temp # o novo nó tem a propriedade before setada para o elemento que antes era o último
            self.tail = new_node # o novo nó passa a ser o último da lista
            self.length += 1 # incrementamos o length da lista
            return True
    
    def pop(self):
        # método para remover o último elemento da lista
        # diferente das linked lists comuns. Já que cada elemento tem a referencia do seu antecessor,
            # esse método é O(1), ou seja, tem um numero constante de operações, não necessitando de um laço
        # temos três cenários a serem avaliados. Quando lista está vazia, e quando ela possui apenas um elemento e quando possui dois ou mais
        
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1 # decrementamos o length da lista
            return temp
        else:
            target = self.tail # armazenamos a referência do último elemento
            before = target.before # armazenamos a referencia do elemento anterior ao alvo
            target.before = None # removemos a referencia ao elemento anterior do alvo, a fim de remove-lo da lista
            before.next = None # o elemento que agora é o último passa a ter seu next apontado para none,
                # dessa forma removemos definitivamente o elemento da lista
            self.tail = before # o penúltimo elemento passa a ser o último
            self.length -= 1 # decrementamos o length da lista
            return target
    
    def prepend(self, value):
        # método para inclusão de elemento no inicio da lista
        # temos dois casos a serem considerados. Quando a lista esta vazia, e quando possui nop mínimo um elemento
        # podemos aproveitar o método append em um dos casos
        if self.length == 0:
            return self.append(value)
        else:
            new_node = Node(value) # começamos criando o nó
            temp = self.head # armazenamos a referencia do atual primeiro elemento
            temp.before = new_node # apontamos a propriedade before do elemento que antes era o primeiro para o novo nó
            new_node.next = temp # apontamos o next do novo nó para o elemento que antes era o primeiro
            self.head = new_node # definimos que o elemento agora é o primeiro da lista
            self.length += 1
            return True

    def pop_first(self):
        # remove o primeiro elemento da lista
        # são três os casos que devemos avaliar: lista vazia, lista com um elemento e lista com mais de um elemento
        if self.length ==0: # caso a lista esteja vazia, retornamos None
            return None
        elif self.length ==1:
            return self.pop() # caso a lista tenha apenas um elemento, podemos usar o método pop
        else:
            target = self.head # armazenamos a referencia do primeiro elemento, que é o alvo
            self.head = target.next # definimos que o primeiro elemento será o que antes era o segundo
            target.next = None # removemos do alvo a referencia ao proximo elemento
            self.head.before = None # removemos a referencia ao elemento anterior do elemento que agora é o primeiro elemento
            self.length -= 1 # decrementamos o length da lista
            return target

    def get(self, index):
        # método para buscar um elemento por índice
        # é necessário um laço para navegar até o elemento desejado 0(n)
        # são tres os casos a serem avaliados: caso o index seja 0, caso index seja igual length-1 e caso esteja fora do range da lista
        # esse método, diferente do get das single linked lists, pode ser otimizado, fazendo um loop reverso, dependendo do index passado
        if index < 0 or index >= self.length: # caso o index esteja fora do range da lista retorne None
            return None
        elif index == 0: # caso o index seja zero retorne o primeiro elemento da lista
            return self.head
        elif index == self.length - 1: # caso o index seja igual a length -1 retorne o ultimo elemento
            return self.tail
        else: #caso a lista tenha mais de um elemento
            if index > self.length/2:
                temp = self.head # armazenamos a referencia do primeiro elemento pra iniciar a iteração
                for _ in range(index):#iteramos pela lista até o index desejado
                    temp = temp.next # alteramos a referencia de temp para o seu sucessor a cada iteração
            else:
                temp= self.tail # armazenamos a referencia do ultimo elemento para iniciar uma iteração reversa, de modo a otimizar o laço
                for _ in range(self.length - 1, index, -1):
                    temp = temp.before # alteramos  referencia de temp para o seu antecessor de forma a fazer um laço reverso
            # ao fim do laço o temp contem o elemento de index desejado
            return temp

    def set_value(self, index, value):
        # método para setar o valor do elemento do index passado
        # podemos aproveitar o método get para buscar a referencia do elemento a ser atualizado
        # devemos verificar se o index passado está no range da lista antes de prosseguir
        # devemos verificar se o índice é igual a zero(primeiro elemento) ou igual length -1 (ultimo elemento), para setar o head e tail devidamente
        if index < 0 or index >= self.length: # verificamos se o index está no range da lista
            return False
        else:
            temp = self.get(index) # basta chamar o get para armazenar a referencia do elemento de index passado
            temp.value = value # então alteramos o valor desse elemento
            return True

    def insert(self, index, value):
        # método para inserir um nó na posição desejada
        # Os casos a serem avaliados são: index fora do range, index igual a zero e index maior ou igual a length-1
        # podemos aproveitar o get para buscar a referencia do elemento que encontra-se na posição desejada
        if index < 0 or index > self.length:
            return None
        elif index == 0:
                return self.prepend(value) # podemos aproveitar o método append e prepend para o caso do index referir ao primeiro ou ultimo elemento
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value) # criamos o nó a ser inserido
            temp = self.get(index) # armazenamos a referencia do elemento que ocupa a posição desejada
            new_node.next = temp # definimos que o novo nó é o antecessor do elemento que ocupa o index desejado
            new_node.before = temp.before # alteramos a referencia do before para o elemento que era antecessor do elemento que ocupa a posição desejada
            temp.before = new_node # setamos a propriedade before do elemento que ocupava a posição desejada, concluindo a inserção
            new_node.before.next = new_node # o elemento qe agora se encontra antes do novo nó, tm o next setado para onovo nó
            self.length += 1 # incrementamos o length
            return True
    
    def remove(self, index):
        # remove o elemento do index passado
        # temos três casos a considera:index fora do range, lista vazia, index igual a zero e index igual a self.length-1
        if self.length == 0 or index < 0 or index >= self.length: # caso a lista esteja vazia ou index fora do range
            return None
        elif index == 0: #caso o elemento seja o primeiro da lista
            return self.pop_first()
        elif index == self.length - 1: # caso o elemento seja o ultimo da lista
            return self.pop()
        else:
            target = self.get(index) # armazenamos a referencia do elemento alvo
            before = target.before # armazenamos a referencia do antecessor do alvo
            after = target.next # armazenamos a referencia do sucessor do alvo
            before.next = after # o antecessor do alvo tem seu next apontado para o sucessor do alvo
            after.before = before # o sucessor do alvo tem seu before apontado para o antecessor do alvo
            target.next = None # removemos definitivamente o alvo da lista, removendo suas referencias
            target.before = None
            return target



    def print_list(self):
        # método para exibir a lista
        if self.length == 0: # caso a lista esteja vazia, apenas exibimos os colchetes
            print('[]')
            return None
        elif self.length == 1:
            print(f'[{str(self.head.value)}]') # caso a lista tenha apenas um elemento, retornamos ele sem iterar a lista
        else:
            temp = self.head # armazenamos a referência do  primeiro elemento
            print('[', end='')
            for _ in range(self.length):
                if temp:
                    if temp.next:
                        print(temp.value, end=',')    
                    else:
                        print(temp.value, end="]\n")
                    
                    temp = temp.next


# dll = DoublyLinkedList()

# dll.append(0)
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.append(4)
# dll.append(5)
# dll.pop()
# dll.prepend(10)
# dll.pop_first()
# print(dll.get(2).value)
# dll.set_value(3, 10)
# dll.print_list()
# dll.insert(6, 10)
# dll.print_list()
# dll.remove(4)
# dll.print_list()