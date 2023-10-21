# Desafio 106 Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
# A palavra 'FIM', o programa se encerrará.
# OBS: Use cores.

def helpCris(parametro):
    if parametro.capitalize() == 'Fim':
        pass
    else:
        print('\033[44m-=' * 20)
        print(f'Acessando o manual do comando "{parametro}"')
        print('-=' * 20)

        print('\033[7;40m')
        return help(parametro)

while True:
    print('\033[0;42m-='*20)
    print(f'{"SISTEMA DE AJUDA PyHELP":>30}')
    print('-=' * 20)

    pergunta = input('\033[mFunção ou Biblioteca: ')
    helpCris(pergunta)

    if pergunta.upper() == 'FIM':
        print('\033[0;41m-='*5)
        print('ATÉ LOGO!')
        print('-='*5)
        break