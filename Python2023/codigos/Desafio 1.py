#exercício 01 Python
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

nome = input("Qual seu nome?")
print("Seja bem vindo",cores['vermelho'],nome,cores['limpar'],)