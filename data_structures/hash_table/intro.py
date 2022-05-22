# Python possui um hash table built in, que são os dicionários
# deforma simplificada, uma hash table funciona da seguinte forma:
    # temos uma função matemática,que receberá um par de chave e valor
    # essa função vai gerar um endereço a partir da chave passada
    # em seguida, vair armazenar a chave e o valor de forma a serem referenciados pelo endereço gerado]
    # quando tentarmos buscar um valor a partir de uma chave, essa função é chamada novamente, a fim de gerar o endereço novamente,
    # dessa forma, sabemos onde o par está armazenado, podendo acessa-lo
#COLISÕES:
    # Ocorrem quando fazemos a inserção de um par chave e valor, em um endereço que já se encontra em uso
    # para que não haja sobrescrita, os pares são armazenados em um array, podendo haver múltiplos pares em um mesmo endereço
    # uma outra maneira de lidar com colisões é, caso o endereço esteja em uso, o par é armazenado no próximo endereço vazio
    