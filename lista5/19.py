"""
19) Escreva uma função que imprima somente os números pares
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Saída: [2, 4, 6, 8]
"""

def imprimePares(lista):
    listaPares = []
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            listaPares.append(lista[i])
    print(listaPares)

enes = []
argumentos = int(input("Quantos argumentos deseja inserir?: "))
for i in range (argumentos):
    enes.append(int(input("Valor %i: " %i)))

imprimePares(enes)