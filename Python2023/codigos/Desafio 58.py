# Desafio 58. Melhore o jogo do Desafio 28. Onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar
# até acertar, mostrando no final quantos palpites foram necessários
# para vencer

print('='*40)
print('Bem vindo ao programa de ADIVINHAÇÃO\n ============================================\n Tente descobrir qual o número que o computador pensou...')
from random import choice
from time import sleep

jogador = 2
computador = 3
contagem = 0
while jogador != computador:
    lista = [0,1,2,3,4,5,6,7,8,9,10]
    jogador = int(input('Entre 0 e 10 escolha um número...'))
    computador = choice(lista)
    print('Processando...')
    sleep(3)
    if jogador == computador:
        print('VOCÊ GANHOU !!\n O número que o computador escolheu foi:', computador ,' e o seu número foi:',jogador)
        contagem += 1
    else:
        print('VOCÊ PERDEU !\n O número que o computador escolheu foi:', computador , 'e o seu número foi:', jogador)
        contagem += 1
print('Foram necessários:',contagem,'jogadas para vencer o computador !')
