#desafio 09. Faça um programa que leia um número inteiro qualquer
#e mostre na tela a sua tabuada
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

p = int(input('Digite um valor: '))
print(cores['vermelho'],'A tabuada do número',p,'é: ')
print('='*20)
print('='*20)
print('1 x',p,'=',p*1)
print('2 x',p,'=',p*2)
print('3 x',p,'=',p*3)
print('4 x',p,'=',p*4)
print('5 x',p,'=',p*5)
print('6 x',p,'=',p*6)
print('7 x',p,'=',p*7)
print('8 x',p,'=',p*8)
print('9 x',p,'=',p*9,cores['limpar'])
