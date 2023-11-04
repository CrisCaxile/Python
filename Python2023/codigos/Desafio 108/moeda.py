# Desafio 108 Crie um modulo chamada moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().

def aumentar(argumento,aumento):
    return argumento + (argumento * aumento)/100

def diminuir(argumento,diminui):
    return argumento - (argumento * diminui)/100

def dobro(argumento):
    return argumento * 2

def metade(argumento):
    return argumento/2

def moeda(valor):
    if valor % 2 == 0:
        return f'R${valor:.0f}.00'
    else:
        return f'R${valor:.2f}'

