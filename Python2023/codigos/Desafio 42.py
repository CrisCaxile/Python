# Desafio 42 Refaça o desafio 035 dos triângulos, acrescentando o recurso
# De mostra que tipo de triângulo será formado:
# Equilátero:todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3= float(input('Agora informe o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1 :
    print('Com o valor das três comprimentos, PODE SIM SE FORMAR UM TRIÂNGULO!!')
    if reta1 == reta2 and reta2 == reta3:
        print('\033[32m O TRIÂNGULO A SER FORMADO SERÁ O EQUILÁTERO!!\n Pois tem todos os lados iguais \033[m')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('\033[33m O TRIÂNGULO A SER FORMADO SERÁ O ISÓSCELES !!\n Pois tem dois lados iguais \033[m')
    elif reta1 != reta2 and reta2 != reta3:
        print('\033[31m O TRIÂNGULO A SER FORMADO SERÁ O ESCALENO ! \n Pois tem todos os lados diferentes \033[m ')
else:
     print('NÃO PODE SE FORMAR UM TRIÂNGULO...')