#Exercicio 07 letra c
#Parte das variáveis a=1 b=-5 e c=6

a = 1
b = -5
c = 6
Formula = b**2-4*a*c
Raiz = Formula**(1/2)
if Formula <= 0:
    print('Não existe resolução para esta conta')
else:
    print(f"O resultado para a 1ª questão é: {Raiz}")

#Parte das variáveis a=1 b=0 e c=-9

a = 1
b = 0
c= -9
Formula = b**2-4*a*c
Raiz = Formula**(1/2)
if Formula <=0:
    print('Não existe resolução para esta conta')
else:
    print(f'O resultado para a 2ª questão é: {Raiz}')

#Parte das variáveis a=5 b=-45 e c=0

a = 5
b = -45
c = 0
Formula = b**2-4*a*c
Raiz = Formula**(1/2)
if Formula <= 0:
    print("Esta conta não tem resolução")
else:
    print(f'O resultado para a 3ª questão é: {Raiz}')

#Parte das variáveis a=1 b=-1 e c=-12

a = 1
b = -1
c = -12
Formula = b**2-4*a*c
Raiz = Formula**(1/2)
if Formula <= 0:
    print('Esta conta não tem resolução')
else:
    print(f"O resultado para a 4ª questão é: {Raiz}")

#Parte das variáveis a=1 b=-6 e c=10

a = 1
b = -6
c = 10
Formula = b**2-4*a*c
Raiz = Formula**(1/2)
if Formula <= 0:
    print('Esta conta não existe resolução')
else:
    print(f"O resultado para a 5 questão é : {Raiz}")
print("="*50)
#Exercicio 08

a = int(input("Digite o valor da variável 'a': "))
b = int(input("Digite o valor da variável 'b': "))
c = int(input("Digite o valor da variável 'c': "))
Formula = b**2 - 4 * a * c
Raiz = Formula ** (1/2)
x1 = (-b + Raiz)/ 2 * a
x2 = (-b - Raiz) / 2 * a
if Formula <= 0:
    print("Esta conta não tem resolução")
else:
    print(f'A primeira raiz da equação foi {round(x1,2)} e a segunda raiz foi {round(x2,2)}')
