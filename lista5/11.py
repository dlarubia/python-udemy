"""
11) Escreva um função que some todos os números contidos numa lista.
Lista: (1, 2, 3, 4, 5)
Soma: 15
"""

lista = [1, 2, 3, 4, 5]
somatorio = 0

for i in range (len(lista)):
    somatorio += lista[i]

print(somatorio)