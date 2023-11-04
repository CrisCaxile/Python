# Desafio 43 Desenvolva uma lógica que leia o peso e a altura de uma
# Pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela
# Abaixo:
# Abaixo de 18.5:Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Agora informe a sua altura: '))

IMC = peso/(altura**2)

if IMC < 18.5:
    print('O seu IMC está abaixo de 18.5. \n \033[31m Portanto, você está abaixo do peso.\033[m')
elif IMC >= 18.5 and IMC < 24.99:
    print('O seu IMC está entre 18.5 e 24.99. \n \033[32m Dessa maneira, você está no peso ideal.\033[m')
elif IMC >= 25 and IMC < 29.99:
    print('O seu IMC está entre 25 e 29.99. \n \033[33m Assim, você está com sobrepeso.\033[m')
elif IMC >= 30 and IMC < 39.99:
    print('O seu IMC está entre 30 e 39.99. \n \033[34m Portanto, você está com Obesidade.\033[m')
else:
    print('O seu IMC está acima de 40. \n \033[35m Nesse sentido, você está com obesidade mórbida.\033[m')
