# 5- Escreva scripts para mostrar os diversos formatos de data e tempo conforme
# se segue:

# a) Data e hora atual
import datetime,time

print(f'A data e hora atual são: {datetime.datetime.now()}')

# b) Ano atual

print(f'O ano atual é: {datetime.datetime.now().year}')

# c) Mês atual

print(f'O mês atual é: {datetime.datetime.now().month}')

# d) Número da semana do ano

print(f'O numero da semana do ano é: {round(time.localtime()[7]/4.2)}')

# e) Dia atual da semana

separacao = time.ctime().split(' ')
print(f'O dia atual da semana é: {separacao[0]}')

# f) dia do ano
separacao1 = time.localtime()
print(f'O dia do ano: {separacao1[-2]}')

#g) dia do mês

print(f'O dia do mês: {separacao1[2]}')

#h) dia da semana

print(f'O dia da semana: {separacao1[6]}')