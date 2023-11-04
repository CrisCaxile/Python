# Desafio 100 Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
# números e vai colocá0los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior

from random import sample
lista = []
def sorteia():
    lista.append(sample(range(0,9),5))
    print(f'Sorteando 5 valores da lista:',end=' ')
    for x in lista:
        for c in x:
            print(c,end=' ')
    print('PRONTO !')

def somaPar():
    soma = 0
    print(f'Somando os valores pares de :',end=' ')
    for x in lista:
        for c in x:
            print(c,end=' ')
    print('temos',end=' ')
    for c in lista:
        for x in c:
            if x % 2 == 0:
                soma += x
    print(soma)
sorteia()
somaPar()
