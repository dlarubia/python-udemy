"""
20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.
"""

def verificaPalindromo (palavra):
    #[begin : end : step]
    palavraInvertida = palavra[::-1]
    if palavraInvertida == palavra:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

string = input("Digite uma palavra: ")
verificaPalindromo(string)
