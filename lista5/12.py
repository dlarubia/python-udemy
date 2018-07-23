"""
12) Escreva uma função que multiplique todos os números de uma lista.
Lista: (1, 2, 3, 4, 5)
Multiplicação: 120
"""

lista = [1, 2, 3, 4, 5]
somatorio = 1

for i in range (len(lista)):
    somatorio *= lista[i]

print(somatorio)