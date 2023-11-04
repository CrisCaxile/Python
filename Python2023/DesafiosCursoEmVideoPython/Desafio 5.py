cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

# desafio 05. Faça um programa que leia um número
# inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))
print(cores['azul'],'O seu antecessor é',n-1,'e o seu sucessor é',n+1,cores['limpar'])