"""
8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:
"""

print("A palavra 'stop' encerra o algoritmo.")

dicionario = {}
chave = 0
valor = 0

while valor != "stop":
    valor = input("Digite o valor: ")
    if valor == "stop":
        break
    dicionario[chave] = valor
    #dicionario.update([valor, chave])
    chave += 1

print(dicionario)

