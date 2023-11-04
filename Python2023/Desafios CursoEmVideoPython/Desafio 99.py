# Desafio 99 Faça um programa que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior

from time import sleep

def maior(*valor):

    MaiorValor = 0
    print('Analisando os valores passados...')
    sleep(2)

    for c in valor:
        print(c,end=' ')
        if c > MaiorValor:
            MaiorValor = c


    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {MaiorValor}.')
    print('-='*20)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
