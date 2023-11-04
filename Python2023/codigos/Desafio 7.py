#desafio 07. Desenvolva um programa que leia as duas notas de um aluno
#calcule e mostre sua média

cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Agora digite a segunda nota: "))
print(cores['cinza'],'A média das notas é:',(n1+n2)/2,cores['limpar'])
