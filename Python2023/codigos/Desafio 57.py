# Desafio 57. Faça um programa que leia o sexo de uma pessoa, mas só
# aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto

w = 'S'
while w == 'S':
    pergunta = input('Digite o sexo da pessoa: [M/F]').upper()

    while pergunta not in 'MF':
        pergunta = input('O valor digitado está errado.\n Digite novamente [M/F]').upper()

    w = input('Se você quiser parar digite: [N]\n Se quiser continuar digite: [S]')

print('FIM.......')