#Desafio 18. Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin,cos,tan

a = float(input('Informe o valor de um ângulo: '))
print('\033[35mO valor do seu seno é', round(sin(a)),'o cosceno é',round(cos(a)),' e sua tangente é',round(tan(a)))
