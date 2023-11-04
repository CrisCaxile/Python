# Desafio 32. Faça um programa que leia um ano qualquer
# e mostre se ele é BISSEXTO

Ano = int(input('Informe um ano: '))

if Ano % 4 == 0 and Ano % 100 != 0:
    print('O ano que você digitou:', Ano, 'é um ano bissexto')

elif Ano % 400 == 0:
    print('O ano que você digitou:', Ano, 'é um ano bissexto')

else:
    print('O ano não é bissexto!!')
