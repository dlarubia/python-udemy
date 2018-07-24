"""
18) Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e imprima na telas os números primos contidos nessa lista.
"""

from math import sqrt

#Observação: Com estudos dos números inteiros e criptografia, é possível certificar de que NÃO EXISTEM métodos que garantem a primalidade de um número. Apenas a fatoração!

def verificaPrimos(n):
    listaDePrimos = []
    for i in range (n):
        x = float(input("Digite um número: "))
        raiz = sqrt(x)
        for j in range (int(raiz)):
            if x % j == 0:
                print("O número é primo")
                listaDePrimos.append(x)

    print(listaDePrimos)

n = int(input("Digite o número de valores que deseja inserir: "))

verificaPrimos(n)

# Corrigir o código