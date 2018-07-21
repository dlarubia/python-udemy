"""
7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. Em seguida, imprima os parâmetros recebidos na tela:
"""

print("Digite 'stop' quando quiser parar o algoritmo")

lista = []

continuar = True

while continuar:
    x = input()
    if x == "stop":
        break
    lista.append(x)

print(lista)


"""
Outra ideia
"""
print("Digite 'stop' quando quiser parar o algoritmo")

lista = []

x = input()
while x != "stop":
    lista.append(x)
    x = input()

print(lista)