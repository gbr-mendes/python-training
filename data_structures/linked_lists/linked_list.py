from itertools import count
# Métodos a serem desenvolvidos:
# append, prepend, pop, pop_first, insert, get, remove, set, reverse

# Cada nó de uma linked list faz referencia apenas ao seu sucessor e ao seu valor
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# A linked list faz referencia a duas variáveis  head e tail
class LinkedList:
    def __init__(self):
        # Ao inicializar uma linked list, seto suas variáveis como none, para criar uma lista vazia
        self.head = None
        self.tail = None
        # É interessante setar uma variável para a instancia da lista, que armazenará seu tamanho.
        self.length = 0 # como a lista inicia vazia, ela começa com zero
    
    def append(self, value):
        # Como esse método sempre fará a inclusão do valor passado na lista, de cara incremento length para evitar repetição
        self.length += 1
        # Para incluir um elemento ao final da linked list, basta que a variável tail aponte para esse elemento
        # Além disso, o elemento que antes era o último, tenha o seu next setado para o novo elemento
        new_node = Node(value)# antes de tudo, criamos o novo nó
        # devemos fazer uma validação para ver se a lista está vazia
        if not self.head: #Caso o atributo head aponte para none, a lista é vazia
            # Com a lista vazia, tanto head, quanto tail tem que apontar para o novo nó
            self.head = new_node
            self.tail = new_node
            return True
        
        # Com uma lista não vazia
        temp = self.tail#armazenamos a referencia do último elemento a uma variável temporária
        temp.next = new_node # O elemento que antes era o último, deixa de apontar para none e passa a apontar para o novo nó
        self.tail = new_node # O atributo tail passa a apontar para o último elemento
        return True

    def prepend(self, value):
        # Como esse método sempre fará a inclusão do valor passado na lista, de cara incremento length para evitar repetição
        self.length += 1
        # O método prepend  segue a mesma lógica de inclusão ao final, mas trabalhando com as referências do inicia da lista
        # Primeiro verificamos se a lista está vazia
        if not self.head:
            # Para evitar repetição, posso utilizar o próprio método append
            return self.append(value)
        
        # Caso a lista não esteja vazia, basta alterar a referência do head para o novo nó, e setar o next do novo nó para o elemento que er o primeiro
        new_node = Node(value) # Primeiro criamos o novo nó
        temp = self.head # armazeno a referência do primeiro elemento
        new_node.next = temp # seto o next do novo nó para o elemento que era o primeiro
        self.head=new_node # defino que o elemento criado passa a ser o primeiro da lista
        return True

    def pop(self):
        # O método pop remove o ultimo elemento da lista, mas como em uma linked list os elemento não fazem referencia ao seu anterior,
        # ele é mais complexo que os métodos de inserção, de forma que toda a lista tem que ser iterada
        # primeiro se verifica se a lista está vazia
        if not self.head:
            return None #É interessante retornar none nesse caso, pois o pop retorna o elemento removido,e o contrário disso seria retornar none
        
         # Como esse método sempre fará a remoção do ultimo elemento, de cara decremento length para evitar repetição
        self.length -= 1
        temp = self.head # Para iniciar o laço, armazeno a referência do primeiro elemento

        for _ in range(self.length - 1):# Precisamos pegar a referencia do último elemento, por isso não iteramos até o último, e sim até o penúltimo
            temp = temp.next # a cada iteração o temp muda até que chegue o penúltimo elemento
        # com o penúltimo elemento, basta alterar o elemento next dele para none e pontar o tail para esse elemento
        self.tail = temp
        temp.next = None
        return temp

    def pop_first(self):
        # Esse método remove o primeiro elemento da lista. Como cada elemento faz referencia ao seu sucessor, é mais simples o que o pop comum
        # Primeiro verificamos se a lista esta vazia, caso esteja retornamos none
        if not self.head:
            return None
        # Como esse método sempre fará a remoção do primeiro elemento, de cara decremento length para evitar repetição
        self.length -= 1
        temp = self.head # armazenamos a referencia do primeiro elemento na variável temp
        self.head = temp.next # o atributo head passa a apontar para o elemento que vem depois de temp
        temp.next = None # Removemos de vez o elemento que era o primeiro da lista. Como esse elemento agora não aponta para ninguém, o garbage collector atua na sua remoção da memória
        return temp

    def insert(self, index, value):
        # esse método insere um nó em qualquer posição da lista. Por conta disso, é preciso iterar a lista para encontrar o elemento anterior ao índice definido
        #Devemos fazer uma validação do índice  para verificar se ele não está fora do range da lista
        if index < 0 or index >= self.length:
            return False
        # Podemos aproveitar os métodos append e prepend para caso o índice passado seja zero ou igual ao length da lista
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        self.length +=1 # aqui, incrementamos o length da lista visto que a inserção será realizada
        new_node = Node(value) # criamos o node a ser inserido
        # aqui podemos usar o get para pegar o elemento que se encontra no índice desejado
        temp = self.get(index - 1) # temos a referencia do elemento que o sucessor do elemento que ocupa a posição desejada
        new_node.next = temp.next # alteramos a referencia ao next do novo node para o que antes era o next do elemento que será seu antecessor
        temp.next = new_node #o novo ó passa a ser o next do elemento que ocupava sua posição. Dessa forma, o elemento é inserido no índice
        return True

    def get(self, index):
        # esse método retorna o elemento no índice passado, portanto, devemos iterar a lista até o elemento desejado
        # devemos verificar se o index não está fora do range da lista
        if index < 0 or index >= self.length:
            return None

        # Verificamos se o elemento desejado é o primeiro da lista, caso seja, retornamos o head
        if index == 0:
            return self.head
        # Verificamos se o elemento desejado é o último da lista, caso seja, retornamos tail, assim, ganhamos eficiência, pois evitamos um laço desnecessário
        if index == self.length - 1:
            return self.tail
        # em casos do index ser um elemento no meio da lista, devemo iterar a lista
        temp = self.head # armazenamos a referencia do primeiro elemento
        for _ in range(index):# usamos index - 1 para navegar até o elemento desejado
            temp = temp.next # Alteramos a referência de temp a cada iteração para o seu sucessor. Assim, no último laço, teremos o elemento desejado
        
        return temp
    
    def remove(self, index):
        # esse método remove o elemento no índice desejado
        # portanto, precisamos iterar a lista até o antecessor do índice desejado
        # podemos aproveitar o pop e o pop first para caso o índice se refira ao primeiro ou ultimo elemento
        # antes de tudo, verificamos se o índice está no range da lista
        if index < 0 or index >= self.length:
            return None
        
        # depois aproveitamos os métodos mencionados
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        # se o elemento estiver em outras posições precisamos fazer a iteração, mas podemos usar o get
        temp = self.get(index-1) # passamos index - 1 para pegar o antecessor do elemento a ser removido
        target = temp.next # armazenamos a referencia do elemento a ser removido
        temp.next = target.next # alteramos a referencia do elemento que apontava para o alvo, para que ele aponte para o sucessor do alvo
        target.next = None # removemos de vez o alvo da lista
        return target

    def set(self, index, value):
        # atualiza o valor do elemento encontrado no índice passado
        # por ter que encontrar o elemento com base no índice, precisamos de um laço, mas podemos aproveitar o get
        #primeiro verificamos se o índice passado está no range
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index) # armazenamos a referencia do elemento em temp
        temp.value = value # setamos o valor do elemento com o novo valor
        return True
    
    def reverse(self):
        # esse método inverte a ordem da lista. É bastante complexo, pelo fato de que cada nó possuir referencia apenas para o seu sucessor
        # para atingir esse objetivo de forma performática, devemos usar algumas variáveis a mais
        before = None # definimos uma variável que vai armazenar os antecessores do nó que está na iteração
        temp = self.head # uma variável para armazenar o o nó do momento da iteração. Para inicio, temos o head da lista
        after = temp.next #uma variável para armazenar o proximo elemento do nó que está em iteração
        # para inverter a lista precisamos inverter o apontamento dos nós para os seus antecessores
        # HEAD 0 -> 1 -> 2 -> 3 -> 4 -> TAIL 5 -> None, essa lista invertida fica como a seguinte:
        # None <- TAIL 1 <- 2 <- 3 <- 4 <- HEAD 5
        # para tanto, primeiramente invetemos o head e o tail
        self.head, self.tail = self.tail, self.head

        #depois iteramos a lista para mudar as referencias das variáveis
        for _ in range(self.length-1):
            before = temp
            temp = after
            after = after.next
            temp.next = before

    def print_list(self):
        # Para exibir os resultados de uma linked list temos que iterar toda a lista, desde seu primeiro elemento
        # podemos fazer isso aproveitando a variável length
        node = self.head # armazenamos o primeiro elemento da lista na variável node
        print('[', end="") # Utilizo essa estratégia para exibir a lista no formato de exibição de listas comuns do python
        for _ in range(self.length):
            if node.next:
                print(node.value, end=",")
            else:
                print(node.value, end="")
                break
            node = node.next
        print(']')
        
ll = LinkedList()
ll.append(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print_list()
ll.pop()
ll.print_list()
ll.pop_first()
ll.print_list()
ll.remove(2)
ll.print_list()
