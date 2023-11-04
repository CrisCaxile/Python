#Desafio 13. Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

s = float(input("Digite o salário do funcionário: "))
novosalario = s+((s*15)/100)
print(cores['azul'],'Seu novo salário com 15% de aumento será de:',novosalario, "R$",cores['limpar'])
