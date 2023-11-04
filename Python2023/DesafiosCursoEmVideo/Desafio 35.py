# Desafio 35. Desenvolva um programa que leia o comprimento de três retas
# E diga ao usuário se elas podem ou não formar um triângulo

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3= float(input('Agora informe o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1 :
    print('Com o valor das três comprimentos, PODE SIM SE FORMAR UM TRIÂNGULO!!')

else:
     print('NÃO PODE SE FORMAR UM TRIÂNGULO...')