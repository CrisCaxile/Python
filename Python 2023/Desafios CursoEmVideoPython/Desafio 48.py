# Desafio 48. Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de três e que se encontram no intervalo
# de 1 até 500

numerosISoma = 0
nQ = 0
for numero in range(1,500,2):
    if numero % 3 == 0:
        nQ += 1
        numerosISoma += numero
print('\033[35mA soma dos números ímpares são:',numerosISoma,'e a quantidade de números é: \033[m',nQ)
