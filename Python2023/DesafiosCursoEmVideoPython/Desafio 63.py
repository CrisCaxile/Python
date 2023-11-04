# Desafio 63. Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os n primeiros elementos de uma sequência de fibonacci
# ex: 0-1-1-2-3-5-8

print('SEQUÊNCIA DE FIBONACCI...........')

pergunta = int(input('Digite quantos elementos você deseja? '))
v1 = 0
v2 = 1
contador = 3

if pergunta == 1:
    print(0)

elif pergunta == 2:
    print(v1,v2,end=' ')

elif pergunta == 0:
    print('Não existem números')

if pergunta >= 3:
    print(v1,v2,end=' ')

    while pergunta >= contador:
        v3 = v1 + v2
        print(v3,end=' ')
        v1 = v2
        v2 = v3
        contador += 1

print('FIM.......')
