#Desafio 15. Escreva um programa que pergunte a quant de km percorrido
#por um carro alugado e a quant de dias pelos quais ele foi alugado
#calcule o preço a pagar sabendo que o carro custa 60 por dia
# e 0.15 por km rodado.

cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

qkm = float(input('Digite a quantidade de km percorrido: '))
qd = int(input('Agora informe a quantidade de dias que foi alugado: '))
p = (qd*60)+(0.15*qkm)
print(cores['azul'],'O preço a pagar é de:', p,' R$',cores['limpar'])