# Desafio 31. Desenvolva um programa que pergunte a distância
# De uma viagem em KM. Calcule o preço da passagem, cobrando
# R$ 0,50 por Km para viagens de até 200Km e R$0,45 para
# Viagens mais longas

Distancia = float(input('Digite a distância em Km da viagem: '))

if Distancia <= 200:
    Preço1 = round(Distancia * 0.50,3)
    print('O preço da viagem vai ficar no valor de:',Preço1,'R$')
else:
    Preço2 = round(Distancia * 0.45,3)
    print('O preço da viagem vai ficar no valor de:',Preço2,'R$')
