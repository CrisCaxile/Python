#Desafio 12. Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

preco = float(input('Digite o preço do produto: '))
novopreco = preco-((preco*5)/100)
print(cores['vermelho'],"O produto com o desconto de 5% fica:",novopreco, "R$",cores['limpar'])
