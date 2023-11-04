# Desafio 88 Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

print('=-'*20)
print(f'{"JOGO MEGA SENA":>25}')
print('=-'*20)

from random import sample
from time import sleep

pergunta = int(input('Quanto jogos você deseja sortear? '))
print('=-'*20)
lista = list()


for contagem in range(0,pergunta):
    jogos = sample(range(1,61),6)

    for c in jogos:
        if jogos.count(c) > 1:
            jogos.pop(c)
            sample(range(1,61),1)

    lista.append(jogos)


print(f'=-=-= GERANDO OS {pergunta} JOGOS =-=-=')

for c,v in enumerate(lista):
    sleep(1)
    print(f'Jogo {c+1}: {lista[c]}')

print('FIM.............')

from random import sample
lista = [1,3,4,5,4]

for p,v in enumerate(lista):
    if lista.count(v) > 1:
        lista.pop(v)
        a = sample(range(1, 61), 1)
        while a in lista :
            for x in range(0,10):
                a = sample(range(1,61),1)
                print('a')

print(lista)
