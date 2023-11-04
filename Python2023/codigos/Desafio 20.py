#Desafio 20. O mesmo professor do desafio anterior quer sortear a ordem
#de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
#dos quatro alunos e mostre a ordem sorteada

from random import shuffle

shuffle(nomes)
print('\033[37mA ordem de apresentação é', nomes)