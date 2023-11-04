# Desafio 102 Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(a,show = False):
    """
    Essa função calcula o fatorial de um valor.
    :parametro a: é o valor que vai inserir o fatorial.
    :parametro b: é opcional, ele vai mostrar ou não o calculo.
    :return: não retorna valores
    """
    f = 1
    if show == False:
        for c in range(a,0,-1):
            f *= c
        print('-='*20)
        print(f)

    else:
        for c in range(a,0,-1):
            print(f'{c} x',end=' ' if c > 1 else f'= {f}')
            f *= c

fatorial(7,show= True)
