"""
16) Escreva uma função que aceite Strings e calcule a quantidade de letras em mauisculas e minúsculas que a String possui.
"""

def calculaMaiusculas(palavra):
    contador = 0
    for i in range (len(palavra)):
        if palavra[i].isupper():
            contador += 1
    print("Quantidade de letras maiusculas:", contador)

def calculaMinusculas(palavra):
    contador = 0
    for i in range (len(palavra)):
        if palavra[i].islower():
            contador += 1
    print("Quantidade de letras minusculas:", contador)

palavra = input("Digite alguma palavra: ")

calculaMaiusculas(palavra)
calculaMinusculas(palavra)