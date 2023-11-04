#desafio 08. Escreva um programa que leia um valor em metros
#e o exiba convertido em centímetros e milímetros
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

p = float(input("Digite um valor em metros: "))
print(cores['vermelho'],'O valor convertido em centímetros é:',round(p*100),"\nO valor em milímetros é:",round(p*1000),cores['limpar'])
