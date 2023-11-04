# Desafio 33. Faça um programa que leia três números e mostre qual
# é o maior e qual é o menor

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Agora digite o segundo número: '))
numero3 = float(input('Informe o terceiro: '))

numeroMaior = 0
numeroMenor = 0

if numero1 > numero2 and numero1 > numero3:
    numeroMaior = numero1
elif numero2 > numero1 and numero2 > numero3:
    numeroMaior = numero2
elif numero3 > numero1 and numero3 > numero2:
    numeroMaior = numero3

print('O maior número foi:', numeroMaior)

if numero1 < numero2 and numero1 < numero3:
    numeroMenor = numero1
elif numero2 < numero1 and numero2 < numero3:
    numeroMenor = numero2
elif numero3 < numero1 and numero3 < numero2:
    numeroMenor = numero3

print('e o menor número foi:',numeroMenor)
