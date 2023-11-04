#Desafio 29. Escreva um programa que leia a velocidade
# De um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# Dizendo que ele foi multador. A multa vai custar R$7,00
# Por cada Km acima do limite.

Velocidade = float(input('Informe a velocidade do carro: '))

if Velocidade > 80:
    Multa = round((Velocidade - 80) * 7,3)
    print('VOCÊ FOI MULTADO !! \n Terá de pagar: ',Multa,'R$ de Multa.')

else:
    print('VOCÊ NÃO FOI MULTADO ! PARABÉNS !!')