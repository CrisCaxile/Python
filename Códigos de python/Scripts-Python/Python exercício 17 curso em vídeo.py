from math import hypot
x = float(input('Digite o comprimento do cateto oposto: '))
y = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O valor do comprimento da hypotenusa é : {hypot(x,y):.2f}.')
