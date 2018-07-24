"""
4) Escreva um algoritmo contendo uma função que necessite de três argumentos. Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, imprima a média aritmética:
"""

def ordemCrescente(a, b, c):
    lista = [a, b, c]
    lista.sort()
    print(lista)
    print("Média aritmética = " , (a+b+c)/3)

ordemCrescente(3,1,7)
