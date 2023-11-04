# Desafio 71 Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1

print('$'*50)
print('\033[33m ...........CAIXA ELETRÔNICO............ \033[m')
print('$'*50)


calculo = 0
calculo2 = 0
calculo3 = 0
calculo4 = 0
w = 'S'

while w == 'S':
    valor = int(input('Digite o valor a ser sacado: '))

    if valor % 50 == 0:                   #Divisão do 50 exata, ai o programa acaba.
        calculo = valor // 50
        print(calculo, 'cédulas de 50 R$')
        break

    elif valor % 50 != 0:             #Divisão do 50 sem ser exata, o programa continua.

        if valor // 50:
            calculo = valor // 50
            print(calculo,'cédulas de 50 R$')


        calculo2 = valor % 50    # Calculo para pegar o restante que sobra da divisão do 50.
        calculo21 = calculo2 // 20

        if calculo2 % 20 == 0:                     # Se a divisão do 20 for exata o programa acaba aqui.
            print(calculo21, 'cédulas de 20 R$')
            break

        elif calculo2 % 20 != 0:                  # Se a divisão do 20 não for exata o programa continua.

            print(calculo21, 'cédulas de 20 R$')

            if calculo2 % 10 == 0:                         # Se a divisão do 10 for exata o programa acaba aqui.
                calculo3 = (calculo2 % 20) // 10              # calculo para pegar o valor que sobra do 20 para o 10
                print(abs(calculo3), 'cédulas de 10 R$')
                break

            elif calculo2 % 10 != 0:            # Se a divisão do 10 não for exata o programa continua.

                calculo3 = (calculo2 % 20) // 10         # botar o calculo3 novamente pois o anterior estava dentro de um if
                print(calculo3,'cédulas de 10 R$')

                if calculo3 % 1 == 0:                 # a divisão do 1 o programa acaba aqui
                    calculo4 = (calculo2 % 20) % 10
                    print(abs(calculo4), 'moedas de 1 R$')
                    break




print("-"*50)
print('Serão entregues as seguintes quantidades de cédulas e moedas:')
print('-'*50)

print('\033[31m FIM.............')