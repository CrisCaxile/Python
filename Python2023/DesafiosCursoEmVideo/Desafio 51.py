# Desafio 51. Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão

inicio = int(input('Informe o primeiro termo da PA:'))
razaoPA = int(input('Agora escolha um número para ser a razão da PA'))
for contagem in range(inicio,inicio+(razaoPA*10),razaoPA):
    print(contagem)