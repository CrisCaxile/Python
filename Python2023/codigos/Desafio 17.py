#Desafio 17. Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule e mostre
#o comprimento da hipotenusa

from math import hypot
co = float(input('\033[33mInforme o cateto oposto: '))
ca = float(input('\033[36mInforme o cateto adjacente: '))
c = hypot(co,ca)
print('\033[31mO valor da hipotenusa é:', round(c))
