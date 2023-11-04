#Desafio 10. Crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dólares ela pode comprar.

cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

c = float(input('Quantos reais você tem disponivel na carteira? '))
print(cores['azul'],"Com",c,"R$ disponível em carteira você pode comprar\n",round(c/3.27),"de dólares",cores['limpar'])
