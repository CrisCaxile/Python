# Desafio 28. escreva um programa que faça o computador "pensar"
# Em um número inteiro entre 0 e 5 e peça para o usuário tentar
# Descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice
from time import sleep

lista = [0,1,2,3,4,5]
print('='*40)
print('Bem vindo ao programa de ADIVINHAÇÃO\n ============================================\n Tente descobrir qual o número que o computador pensou...')
jogador = int(input('Entre 0 e 5 escolha um número...'))
computador = choice(lista)
print('Processando...')
sleep(3)
if jogador == computador:
    print('VOCÊ GANHOU !!\n O número que o computador escolheu foi:', computador ,' e o seu número foi:',jogador)
else:
    print('VOCÊ PERDEU !\n O número que o computador escolheu foi:', computador , 'e o seu número foi:', jogador)
