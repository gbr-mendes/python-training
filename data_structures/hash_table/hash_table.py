class HashTable:
    def __init__(self, size=7): # a hash table armazena os pares em uma lista
        self.data_map = [None] * size # essa é a forma de definir o tamanho específico de uma lista em python
        # o tamanho da lista foi definido com um número primo. Dessa forma, o número de aleatoriedade aumenta, reduzindo o número de colisões
    
    def _hash(self, key):
        # esse método determina o endereço do elemento passado
        # essa função é determinística, ou seja, sempre retornará o mesmo valor para o mesmo input
        my_hash = 0
        for letter in key:# iteramos pelos caracteres da chave aplicando um calculo
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # para essa função ser determinística, utilizamos a função ord na letra para utilizarmos seu código UNICODE
            # Somamos o unicode com o hash atual e multiplicamos por 23 para dar aleatoriedade
            # pegamos o resto da divisão pelo size da hash table, de forma ao endereço ficar sempre no range predefinido
        return my_hash

    def set_pair(self, key, value):
        # esse método atribui um par a um endereço
        address = self._hash(key) # geramos o hash com base na chave
        if self.data_map[address] is None:# verificamos se o endereço está vazio
            self.data_map[address] = [[key, value]] # caso esteja vazio, inserimos uma lista com outra lista interna, que contem a chave e o valor
        else:
            self.data_map[address].append([key, value]) # caso o endereço esteja ocupado, apenas fazemos o append de uma lista com a chave e o valor

    def get(self, key):
        # método para retornar o valor a partir de uma chave
        address = self._hash(key)
        if self.data_map[address] is None:
            return None
        for _, pair in enumerate(self.data_map[address]):
            if key == pair[0]:
                return pair[1]
        return None

    def keys(self):
        keys = []
        for _,storage in enumerate(self.data_map):
            if storage is not None:
                for pair in storage:
                    keys.append(pair[0])
        return keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)

ht = HashTable()
ht.set_pair('nome', 'gabriel')
ht.set_pair('idade', 22)
ht.set_pair('cor', 'branco')

print(ht.keys())
