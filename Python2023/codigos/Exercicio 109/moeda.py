# Desafio 108 Crie um modulo chamada moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade().

def aumentar(argumento,aumento,moeda):
    if moeda == False:
        return argumento + (argumento * aumento)/100
    else:
        if argumento % 2 == 0:
            return f'R${(argumento + (argumento * aumento)/100):.0f}.00'
        else:
            return f'R${(argumento + (argumento * aumento)/100):.2f}'

def diminuir(argumento,diminui,moeda):
    if moeda == False:
        return argumento - (argumento * diminui)/100
    else:
        if argumento % 2 == 0:
            return f'R${(argumento - (argumento * diminui)/100):.0f}.00'
        else:
            return f'R${(argumento - (argumento * diminui)/100):.2f}'

def dobro(argumento,moeda):
    if moeda == False:
        return argumento * 2
    else:
        if argumento % 2 == 0:
            return f'R${(argumento * 2):.0f}.00'
        else:
            return f'R${argumento * 2:.2f}'

def metade(argumento,moeda):
    if moeda == False:
        return argumento/2
    else:
        if argumento % 2 == 0:
            return f'R${(argumento/2):.0f}.00'
        else:
            return f'R${(argumento/2):.2f}'

def moeda(valor):
    if valor % 2 == 0:
        return f'R${valor:.0f}.00'
    else:
        return f'R${valor:.2f}'

