# Desafio 39 Faça um programa que leia o ano de nascimento de um jovem
# E informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passsou de atrazo

ano = int(input('Digite o ano do seu nascimento: '))

conversao = 2023 - ano

if conversao < 18:
    print('\033[33m Você ainda vai se alistar ao exército futuramente !')
    print('Faltam',18-conversao,'anos !\033[m')
elif conversao > 18:
    print('\033[34m Você já passou do tempo de alistamento.')
    print('Já se passaram',conversao-18,'anos\033[m')
elif conversao == 18:
    print('\033[31m Você está com',conversao,'anos !, está no tempo de alistamento !\033[m')
