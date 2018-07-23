"""
14) Escreva uma função que calcule o fatorial de um número (um inteiro não negativo). Envie o valor do número que será calcula como argumento da função.
"""

def calculaFatorial(n):
    if n != 1:
        return calculaFatorial(n-1)*n
    else:
        return 1

x = int(input("Digite um valor: "))
print(calculaFatorial(x))