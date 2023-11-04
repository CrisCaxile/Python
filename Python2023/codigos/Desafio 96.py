# Desafio 96 Faça um programa que tenha uma função chamada área(), que receba
# um terreno retangular (largura e comprimento) e mostre a área do terreno

print('Controle de Terrenos')
print('-'*20)

def área(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')

largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite o comprimento (m): '))
área(largura,comprimento)