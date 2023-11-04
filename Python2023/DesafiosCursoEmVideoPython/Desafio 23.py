#Desafio 23. Faça um programa que leia um número de 0 a 9999 e mostre
#na tela cada um dos digitos separados.
#ex : digite um número:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1

numero = int(input('Digite um número de 0 a 9999: '))
u = numero % 10
print('Unidade:',u)
d = numero // 10 % 10
print('Dezena:',d)
c = numero // 100 % 10
print('Centena:',c)
m = numero // 1000
print('Milhar:',m)
