#Exercício 07
#Letra a
a = int(input("Digite o valor da variável 'a': "))
b = int(input("Digite o valor da variável 'b': "))
c = int(input("Digite o valor da variável 'c: "))
Formula = b**2-4*a*c
Raiz= Formula**(1/2)
if Formula <= 0:
    print("Essa conta não existe resultado")
else:
    print(round(Raiz,2))