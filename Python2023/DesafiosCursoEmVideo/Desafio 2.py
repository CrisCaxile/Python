#Exercicio 02 Python
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

dia = input("Qual o dia de seu nascimento? ")
mes = input("Qual o mês do seu nascimento? ")
ano = input("Qual o ano do seu nascimento? ")

print("A sua data de nascimento é ",cores['azul'],dia,"/",mes,"/",ano,cores['limpar'],)
