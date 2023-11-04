#Desafio 19. Um profesor quer sortear um dos seus quatro alunos para
#apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
#e escrevendo o nome do escolhido

from random import choice
p1 = input('Digite o nome do primeiro aluno: ')
p2 = input('Agora o segundo: ')
p3 = input('O terceiro: ')
p4 = input('E o último: ')

nomes = [p1,p2,p3,p4]
print('\033[34mO escolhido foi', choice(nomes))