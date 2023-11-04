# Desafio 98 Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

print('~'*30)
print('\033[32m Programa da Função Contador() \033[m')
print('~'*30)

def Contador(i,f,p):
    if p == 0:
        p = 1

    if f < 0:
        p = -p

    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')

    for x in range(i,f+1,p):
        print(x,end=' ')
        sleep(0.3)
    print('FIM!')
    print('-='*20)

print('Contagem de 1 até 10 de 1 em 1')
Contador(1,10,1)

print('Contagem de 10 até 0 de 2 em 2')
print(Contador(10,0,-2))

print('Agora é a sua vez de personalizar a contagem!')
Inicio = int(input('Inicio: '))
Fim = int(input('Fim: '))
Passo = int(input('Passo: '))

Contador(Inicio,Fim,Passo)

