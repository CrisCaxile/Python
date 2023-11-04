#Desafio 14. Converta a temperatura de Celsius para Fahrenheit
cores = {'limpar':'\033[m',
         'azul':'\033[36m',
         'vermelho':'\033[31m',
         'cinza':'\033[37m'}

C = float(input('Digite a temperatura em Celsius: '))
F = ((C*9)+160)/5
print(cores['cinza'],'A temperatura em Celsius é', C,'e em Fahrenheit é', F,cores['limpar'])
