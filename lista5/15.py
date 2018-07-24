"""
15) Escreva uma função que verifique se um número está num intervalo determinado.
"""
def verificaIntervalo (inicio, fim, n):
    if inicio < fim:
        if ((n >= inicio) and (n <= fim)):
            print("O valor está dentro do intervalo1")
        else:
            print("O valor não pertence ao intervalo1")
    elif fim < inicio:
        if n >= fim and n <= inicio:
            print("O valor está dentro do intervalo2")
        else:
            print("O valor não pertence ao intervalo2")
    else:
        print("Não há intervalo")

#Completar

a = int(input("Digite o início do intervalo: " ))
b = int(input("Digite o fim do intervalo: "))
c = int(input("Digite um número para verificar se pertence ao intervalo: "))

verificaIntervalo(a, b, c)
