#Desafio 11. Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua área e a quantidade de tinta necessária para
#pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura dela: '))
area = l*a
print(cores['cinza'],'A área da parede é',area,"M\ne a quatidade de tinta para pintá-la é:",round(area/2)," litros",cores['limpar'])
