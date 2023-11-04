# Desafio 80 Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

verificadorSimbolo = 0
usuario = 'S'
valor = []
while usuario == 'S':

    valor = input('Digite um valor: ')

    w = 0
    while w < len(valor):
        while valor[w] not in '0123456789':
            print('ERRO')
            valor = input('Digite um valor: ')
        w +=1

    usuario = input('Você deseja continuar? [S] ou [N]: ').upper()

    while usuario.upper() not in 'SN':
        print('ERRO ! DIGITE NOVAMENTE')
        usuario = input('Você deseja continuar? [S] ou [N]: ').upper()
