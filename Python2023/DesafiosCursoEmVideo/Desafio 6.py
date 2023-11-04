# desafio 06. Crie um algoritmo que leia um número e mostre
#o seu dobro, triplo e raiz quadrada
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

a = float(input("Digite um número: "))
print(cores['vermelho'],"O dobro de",a ,"é",a*2 ,"o seu triplo é",a*3 ,"o sua raiz quadrada é",round(a**(1/2)),cores['limpar'])
