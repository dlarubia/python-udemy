"""
18) Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e imprima na telas os números primos contidos nessa lista.

* Alteração: Ao invés de fazer a função pedida no exercício, implementei o Crivo de Erastóstenes
"""

from math import sqrt

#Observação: Com estudos dos números inteiros e criptografia, é possível certificar de que NÃO EXISTEM métodos que garantem a primalidade de um número. Apenas a fatoração!

#Observação 2: Esse algoritmo é uma tentativa de implementação do Crivo de Eratóstenes

def crivoErastostenes(n):
    #Inicialmente, determina-se o maior número a ser checado. Ele corresponde à raiz quadrada do valor limite, arredondado para baixo. No caso, a raiz de n, arredondada para baixo, é sqrt(n). Isso retorna um float, portanto truncamos utilizando o cast.
    raiz = sqrt(n)
    raiz = int(raiz)
    #Crie uma lista de todos os números inteiros de 2 até o valor limite: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, e 30, ... n
    listaDePrimos = list(range(2, n + 1))
    print("Lista inicial ->", listaDePrimos)
    #Encontre o primeiro número da lista. Ele é um número primo, 2.
    #Remova da lista todos os múltiplos de 2 até n
    #O próximo número da lista é primo. Repita o procedimento.
    #Refazer o processo até chegar ao valor que é raiz arredondada (para baixo) do número.

    #Verificarei do 2 até a raiz (soma-se 1 porque a função range para em n-1)
    for i in range (2, raiz + 1):
        #Minha lista[0] = 2, lista[2] = 4 (primeiro número não primo)
        #Irei parar em n-1, porque a lista começa no 2 e não no 0
        for j in range (i, n-1):
            #Verifico se o número (i) divide o número da lista lista[j] e removo-o caso sim.
            if listaDePrimos[j] % i == 0:
                listaDePrimos[j] = 0
    #Minha lista agora só possui números primos e zeros no lugar dos que não são primos
    print("Lista com zeros ->", listaDePrimos)
    #Para remover os zeros, faço um while e em seguida imprimo a lista contendo apenas os primos
    while 0 in listaDePrimos:
        listaDePrimos.remove(0)
    print("Lista de primos ->", listaDePrimos)

x = int(input("Digite um valor: "))
crivoErastostenes(x)


"""
Observação: Acredito que seja possível fazer muitas melhorias no código, entretanto ainda não tenho conhecimento desejável das funções que trabalham com listas em python
"""
