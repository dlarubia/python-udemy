"""
21) Escreva uma função que tenha definida uma função em seu escopo. Invoque a função aninhada, retorne algum valor, imprima esse valor na tela e finalize a aplicação.
"""

def funcaoExterna (string):
    print("Sua string é:", string)

    def funcaoInterna (string):
        stringReversa = string[::-1]
        print("Sua string invertida é:", stringReversa)

    funcaoInterna(string)

funcaoExterna(input("Digite alguma palavra: "))