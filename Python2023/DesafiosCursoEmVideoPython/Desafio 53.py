# Desafio 53. Crie um programa que leia uma frase qualquer e diga
# se ela é palindromo, desconsiderando os espaços

Usuario = input('Digite uma frase: ').upper().strip().replace(' ','')
v = ''

for x in Usuario:
    v += x
print('O inverso de',Usuario,'é:\033[31m',v[::-1],end=' ''\033[m\n')

if Usuario == v[::-1]:
    print('\033[34m A palavra é um palíndromo ! \033[m')
else:
    print('\033[31m A palavra digitada não é um palíndromo \033[m')

