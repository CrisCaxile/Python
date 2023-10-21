# Desafio 104 Crie um programa que tenha a função leiaInt(), que vai
# funcionar de forma semelhante à função input() do Python, só que fazendo
# a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

def leiaInt(numero):

    n = input(numero)
    while n.isdigit() == False:
        print('\033[31m ERRO! Digite um número inteiro válido. \033[m')
        n = input(numero)
    return n

n = leiaInt('Digite um valor: ')
print(f'Você digitou o número {n}')
