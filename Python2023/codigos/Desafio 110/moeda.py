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

def moeda(argumento):
    if argumento % 2 == 0:
        return f'R${argumento:.0f}.00'
    else:
        return f'R${argumento:.2f}'

def resumo(argumento,aumento,desconto):
        espaço = ' '*10
        print('='*40)
        print(f'{"RESUMO DO VALOR":>27}')
        print('='*40)
        print(f'O Preço analisado:{espaço}{moeda(argumento)}')
        print(f'Dobro do preço:{espaço}{dobro(argumento,True)}')
        print(f'Metade do preço:{espaço}{metade(argumento,True)}')
        print(f'Aumento de {aumento}%:{espaço}{aumentar(argumento,aumento,True)}')
        print(f'Redução de {desconto}%:{espaço}{diminuir(argumento,desconto,True)}')
        print('='*40)