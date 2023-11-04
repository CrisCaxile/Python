# Desafio 46. Faça um programa que mostre na tela uma contagem regressiva
# Para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1
# segundo entre eles.

from time import sleep
print("\033[31mPrograma de fogos DE ARTIFÍCIO\033[m")
print('CONTAGEM REGRESSIVA...')
for contagem in range(10,-1,-1):
    #sleep(2)
    print('..............')
    print(contagem)
print("\033[34mOS FOGOS ESTÃO ESTOURANDO !!!!!!!!!!!!!!!!\033[m")
