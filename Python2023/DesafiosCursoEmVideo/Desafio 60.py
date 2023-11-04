# Desafio 60 Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1 = 120

print('Desafio do FATORIAL............')
w = 'S'
while w == 'S':
    n = int(input('Digite um número qualquer:'))
    resposta = 1
    while n >= 1:
        print(n,end='')
        print(' x ' if n > 1 else ' = ',end='')
        resposta *= n
        n -= 1


    print(resposta,'\n O fatorial do número',n,'!')
    w = input('Você deseja continuar? [S/N]').upper()
