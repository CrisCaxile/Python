# Desafio 74 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla

print('='*50)
print('\033[31m ...LISTAGEM MAIOR E MENORES VALORES TUPLA... \033[m')
print('='*50)

from random import choices

tupla1 = (0,1,2,3,4,5,6,7,8,9)
tupla2 = ()

tupla2 = choices(tupla1,k=5)

Organizar = sorted(tupla2)
Maior = Organizar[-1]
Menor = Organizar[0]

print('A lista com os números gerados foram: ',end='')
for n in tupla2:
    print(n,'',end='')
print('')
print('O maior valor foi:',Maior,'e o menor valor foi:',Menor)
print('FIM.........')
