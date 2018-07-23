"""
13) Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. Não utilize a função interna do Python que faz inverção, crie o algoritmo que faça a inversão.
Lista: "1234abcd"
Saída: "dcba4321"
"""

lista = [1,2,3,4,"a","b","c","d"]
listaReversa = []

for i in range (1, len(lista) + 1):
    print(lista[-i])
    listaReversa.append(lista[-i])

print("Lista:", lista)
print("Lista reversa:", listaReversa)

