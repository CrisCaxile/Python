import math
a = int(input("Digite o valor da variável 'a': "))
b = int(input("Digite o valor da variável 'b': "))
c = int(input("Digite o valor da variável 'c': "))
Formula = b**2-4*a*c
Raiz = math.sqrt(Formula)
if Formula <= 0:
    print("Não existe resultado para a conta")
else:
    print(math.ceil(Raiz))