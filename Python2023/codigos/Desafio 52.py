# Desafio 52. Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo
print('-'*30)
print('\033[34mPROGRAMA VERIFICADOR DE NÚMEROS PRIMOS\033[m')
print('='*30)

nUsuario = int(input('Digite um número inteiro qualquer: '))
nPrimo = 0
lista = [2,3,5,7,11]
for c in lista:
    if nUsuario in lista:
        nPrimo = 1
    elif nUsuario % c != 0:
        nPrimo = 1
    elif nUsuario == 1:
        nPrimo = 0
    else:
        nPrimo = 0
        break

if nPrimo == 1:
    print('O número',nUsuario,'é primo !')
else:
    print('O número',nUsuario,'não é primo')

