#Exercicio 09

listaencadeada = "A1E5T7W8G"

def numeros():
    for x in listaencadeada:
        if x in "[1],[2],[3],[4],[5],[6],[7],[8],[9],[0]":
            print(x)

def letras():
    for x in listaencadeada:
        if x not in "[1],[2],[3],[4],[5],[6],[7],[8],[9],[0]":
            print(x)

letras(),numeros()
