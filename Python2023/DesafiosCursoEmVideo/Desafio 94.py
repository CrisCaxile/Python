# Exercicio 94 Crie um programa que leia nome,sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média


dicionarioMaior = {}
lista = []
somatorioIdade = 0
while True:
    dicionarioMaior['Nome'] = input('Digite o nome da pessoa: ')
    dicionarioMaior['Sexo'] = input('Digite o sexo [M/F]: ')
    dicionarioMaior['Idade'] = int(input('Digite a idade: '))

    somatorioIdade += dicionarioMaior['Idade']

    lista.append(dicionarioMaior.copy())

    pergunta = input('Você deseja continuar? [S/N]: ')
    if pergunta.upper() == 'N':
        break

print('=-'*20)
print('Foram cadastradas:',len(lista),'pessoas')
print('A média de idade do grupo é de:',round(somatorioIdade/len(lista),2),'anos')
print('A lista com mulheres são: ',end=' ')

for d in lista:
    for k,v in d.items():
        if v == 'F' or v == 'f':
            print(d['Nome'],end=' ')
print(end='\n')
print('A lista com pessoas acima da média são: ')

for d in lista:
    for k,v in d.items():
        if d['Idade'] > round(somatorioIdade/len(lista)):
            print(f'{k} = {v};',end=' ')
            if d['Idade'] == v:
                print(end='\n')
