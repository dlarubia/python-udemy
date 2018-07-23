"""
10) Escreva um algoritmo que encontre o maior dentre 3 números. Para facilitar a resolução do exercício utilize funções.
"""

def retornaMaior(a, b):
    if a > b:
        return a
    else:
        return b

x = input("Digite o primeiro valor: ")
y = input("Digite o segundo valor: ")
z = input("Digite o terceiro valor: ")

print("O maior valor é:", retornaMaior(retornaMaior(x,y),z))