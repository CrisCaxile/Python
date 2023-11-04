# Desafio 45 Crie um programa que faça o computador jogar jokenpô com você

from random import choice
print('\033[31m========= BEM VINDO AO JOKENPÔ=============\033[m')
x = ['PEDRA','PAPEL','TESOURA']
a = choice(x)
computador = a
jogador = input('Escolha entre as opções:\n'
                    '- PEDRA\n'
                    '- PAPEL\n'
                    '- TESOURA\n')
if jogador == computador:
    print('EMPATE !!!\n'
          'Você e o computador fizeram a mesma jogada !')
elif jogador == "PEDRA" and computador == 'PAPEL':
    print('O COMPUTADOR VENCEU !!\n'
          'O computador pegou PAPEL.')
elif jogador == "PEDRA" and computador == 'TESOURA':
    print('VOCÊ VENCEU !!\n'
          'O computador pegou TESOURA')
elif jogador == "PAPEL" and computador == 'PEDRA':
    print('VOCÊ VENCEU !!\n'
          'O computador pegou PEDRA')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('VOCÊ PERDEU !!\n'
          'O computador pegou TESOURA')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('VOCÊ GANHOU !!\n'
          'O computador pegou PAPEL')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('VOCÊ GANHOU !! \n'
          'o computador pegou PEDRA')
else:
    print('O nome que você digitou não está nas opções')