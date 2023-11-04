# Desafio 64. Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condiçao de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles desconsiderando o flag


print('\033[31m DIGITE "999" SE DESEJAR PARAR O PROGRAMA !!!\033[m')
w = 0
soma = 0
contagem = 0
while w != 999:
    w = int(input('Digite o valor de um número inteiro: '))

    if w != 999:
        soma += w
        contagem += 1

print('A soma dos valores são:',soma)
print('A quantidade de números digitados foi:',contagem)
print('FIM......')

