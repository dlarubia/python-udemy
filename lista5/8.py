"""
8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros que estejam associados a uma chave. Em seguida, imprima na tela o nome da chave e o respectivo valor:
"""

print("Digite valores; a palavra 'stop' encerra o algoritmo.")

dicionario = {}
chave = 0
valor = 0

while valor != "stop":
    valor = input()
    dicionario.update(valor)
    chave += 1

print(dicionario)