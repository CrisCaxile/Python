# Desafio 68 Faça um programa que jogue par ou ímpar com o computador.
# o jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo

vitorias = 0
while True:
    from random import choice
    usuario = int(input('Escolha um número par ou ímpar: '))
    computador = [0, 1]
    if choice(computador) == 0 and usuario % 2 == 0:
        vitorias += 1
        print('\033[36m O computador selecionou um número PAR \n VOCÊ VENCEU!!!! PARABENS!!! \033[m')
    elif choice(computador) == 1 and usuario % 2 != 0:
        vitorias += 1
        print('\033[35m O computador selecionou um número ÍMPAR \n VOCÊ GANHOU !!! \033[m')
    else:
        print('\033[31m VOCÊ PERDEU ! \033[m')
        break

if vitorias == 0:
    print('\033[31m Você não ganhou nenhuma partida ! \033[m')
print('O número total de vitórias foi:',vitorias)

