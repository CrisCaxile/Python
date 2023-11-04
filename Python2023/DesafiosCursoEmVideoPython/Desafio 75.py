# Desafio 75 Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

print('~'*50)
print('\033[32m Programa DE ANALISE DE TUPLAS..... \033[m')
print('~'*50)

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o teceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))


tupla = (valor1),(valor2),(valor3),(valor4)

PosicaoDo3 = 0


if '3' in str(valor1):
    PosicaoDo3 = 1
elif '3' in str(valor2):
    PosicaoDo3 = 2
elif '3' in str(valor3):
    PosicaoDo3 = 3
elif '3' in str(valor4):
    PosicaoDo3 = 4
else:
    PosicaoDo3 = 'O valor 3 não foi digitado'


print('Você digitou os valores:',tupla)
print('A quantidade de vezes que apareceram o número 9 foi de:',tupla.count(9),'vezes')
print('A posição que foi digitado o primeiro número 3 foi:',PosicaoDo3)
print('Os números pares foram:',end='')

for c in tupla:
    if c % 2 == 0:
        print(c,'',end='')
print('')
print('FIM......')
