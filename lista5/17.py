"""
17) Escreva uma função que receba como argumento uma lista que poderá ter valores duplicados e retorne uma nova lista sem que haja valores iguais.
Lista: [1,2,3,3,3,3,4,5]
Retorno: [1, 2, 3, 4, 5]
"""

def eliminaRepeticao(lista):
    novaLista = []
    for i in range (len(lista)):
        if lista[i] in novaLista:
            continue
        else:
            novaLista.append(lista[i])

    print(novaLista)

lista = list(input("Digite valores para compor uma lista: "))
eliminaRepeticao(lista)