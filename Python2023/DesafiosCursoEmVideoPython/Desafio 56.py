# Desafio 56 Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas
# No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

IdadeS = 0
IdadeM = 0
Qmulher = 0
AbaixoIdade = 0
dicionario = {}
HomemV = {'idade': 0}
idades = []
escolher = int(input('Digite quantas pessoas vocês quer: '))

for c in range(0,escolher):
    nome = input('Digite o nome de uma pessoa: ')

    idade = int(input('Agora a idade: '))
    IdadeS += idade
    if idade < 20:
        AbaixoIdade += 1

    sexo = input('E o sexo dessa pessoa: ')
    dicionario = {'Nome':nome,'idade':idade,'sexo':sexo}

    if dicionario['sexo'] == 'feminino' and dicionario['idade'] < 20:
        Qmulher += 1

    if dicionario['sexo'] == 'masculino' and dicionario['idade'] > HomemV['idade']:
        HomemV['Nome'] = dicionario['Nome']
    IdadeM = IdadeS / escolher

print('\033[34m A média de idade das pessoas é:',IdadeM,'\033[m')
print('\033[35m No grupo tem:',Qmulher,' mulheres abaixo dos 20 anos\033[m')
print('\033[31m No grupo o nome do homem mais velho é:',HomemV['Nome'])