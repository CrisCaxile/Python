#Exercicio 03
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1+n2
print("A soma do primeiro com o segundo número é: ",cores['verde'],soma)