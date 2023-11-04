# Desafio 59 Crie um programa que leia dois valores e mostre um menu
# na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Agora informe o segundo valor: '))

w = 0
while w != 5:
    print('[1] : Somar')
    print('[2] : Multiplicar')
    print('[3] : maior')
    print('[4] : novos números')
    print('[5] : sair do programa')
    w = int(input('\033[34m Escolha uma operação acima:\033[m'))
    if w == 1:
        print('\033[33m A soma dos números',n1,'+',n2,'é igual a:',n1+n2,'\033[m')
    elif w == 2:
        print('\033[35m A multiplicação dos números',n1,'*',n2,'é igual a:',round(n1*n2,2),'\033[m')
    elif w == 3:
        maiorN = 0
        if n1 > n2:
            maiorN = n1
            print('\033[36m O número maior entre', n1, 'e', n2, 'é o número',n1,'\033[m')
        elif n2 > n1:
            maiorN = n2
            print('\033[36m O número maior entre', n1, 'e', n2, 'é o número:',n2,'\033[m')
        else:
            print('\033[31m Os dois números são iguais \033[m')
    elif w == 4:
        n1 = float(input('\033[37m Digite um novo número para o N1:'))
        n2 = float(input('Agora um novo número para o N2:\033[m'))
