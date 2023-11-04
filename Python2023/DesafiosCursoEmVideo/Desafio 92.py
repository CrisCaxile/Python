#Desafio 92 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre -os ( com idade) em um dicionário se por acaso a CTPS for diferente de zero,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
# da idade, com quantos anos a pessoa vai se aposentar,* 35 anos de contribuição.

import datetime
carteiraDeTrabalho = {}

carteiraDeTrabalho['Nome'] = input('Nome: ')
carteiraDeTrabalho['Idade'] = 2023-int(input('Ano de Nascimento: '))
carteiraDeTrabalho['Carteira de Trabalho'] =  int(input('Carteira de Trabalho: '))

if carteiraDeTrabalho['Carteira de Trabalho'] == 0:
    print('-='*20)
    for k,v in carteiraDeTrabalho.items():
        print(f'{k} tem o valor {v}')
else:
    carteiraDeTrabalho['Ano de Contratação'] = int(input('Ano de contratação: '))
    carteiraDeTrabalho['Salário'] = float(input('Salário: '))
    carteiraDeTrabalho['Aposentadoria'] = 35 - (2023 - carteiraDeTrabalho['Ano de Contratação'])

    for k,v in carteiraDeTrabalho.items():
        print(f'{k} tem o valor {v}')
