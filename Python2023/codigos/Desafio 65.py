# Desafio 65 Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores e qual foi o maior
# e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores

print('~~~~~~~~~~~~Programa Final~~~~~~~~~~~~')

pergunta = 'S'
soma = 0
quantidade = 0
menorV = 999
maiorV = 0


while pergunta == 'S':
    valores = int(input('Informe um número inteiro: '))
    soma += valores
    quantidade += 1
    pergunta = input('Você deseja continuar a informar valores? [S/N]').upper()
    if valores > maiorV:
        maiorV = valores
    if valores < menorV:
        menorV = valores

print('A média dos valores são:',round(soma/quantidade,2))
print('O maior valor lido é:',maiorV,' e o menor valor lido é:',menorV)
print('FIM..............')