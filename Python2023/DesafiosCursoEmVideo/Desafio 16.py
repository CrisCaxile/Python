#Desafio 16. Crie um programa que leia um número real qualquer pelo
# teclado e mostre na tela a sua porção inteira

n = float(input('Digite um número qualquer: '))
print('\033[32mO número', n,' tem a parte inteira',round(n),'\033[m')