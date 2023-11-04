#Desafio 34. Escreva um programa que pergunte o salário de um funcionário
# E calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00
# Calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Diga qual o valor do seu salário: '))

NovoSalario = 0
if salario > 1250:
    Novosalario = ((salario*10)/100) + salario
if salario <= 1250:
    Novosalario = (salario*15)/100 + salario

print('O valor do seu novo salário é de',round(Novosalario,3),'R$')