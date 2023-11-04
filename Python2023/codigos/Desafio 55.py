# Desafio 55. Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

MApeso = 0
MEpeso = 100
for c in range(0,5):
    peso = float(input('Informe o peso de cinco pessoas: '))
    if peso > MApeso:
        MApeso = peso
    elif peso < MEpeso:
        MEpeso = peso
print('\033[33m O maior peso foi:',MApeso,'e o menor peso é:',MEpeso,'\033[m')
