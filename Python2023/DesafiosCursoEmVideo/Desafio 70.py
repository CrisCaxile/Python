# Desafio 70 Crie um programa que leia o nome e o preço de vários produtos
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

print('-'*50)
print('\033[36m CAIXA DE SUPERMERCADO \033[m')
print('-\033[m'*50)

soma = 0
produtoMaisde1000 = 0
produtoMaisBarato = 999
NomeProdutoMaisBarato = ''

while True:

    nome = input('Digite o nome do produto: ')
    while nome.isalpha() is not True:
        nome = input('Digite o nome do produto: ')


    preco = input('Digite o preço do produto: ')
    while preco.isnumeric() is not True or int(preco) <= 0:
        preco = input('Digite o preço do produto: ')

    soma += int(preco)

    if int(preco) > 1000:
        produtoMaisde1000 += 1

    if int(preco) < produtoMaisBarato:
        produtoMaisBarato = int(preco)
        NomeProdutoMaisBarato = nome

    pergunta = input('Você deseja continuar? [S] ou [N]: ').upper()
    if pergunta == 'N':
        break


print('\033[31m ......FIM....... \033[m')
print('O total de gasto na compra foi de',soma,'R$')
print(produtoMaisde1000,'produtos são mais de 1000 R$')
print('O nome do produto mais barato é:',NomeProdutoMaisBarato)
