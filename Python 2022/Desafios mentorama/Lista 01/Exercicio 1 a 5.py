#Lista 02
nome = str(input("Digite seu nome completo: "))
print(nome)
print("="*50)
#Exercício 02
a = 2
b = 5
print((5*a)*(3*b))
print("="*50)
#Exercício 03
a = 2
b = 5
c = 5
print(a+b+c)
print("="*50)
#Exercício 04
Programa = str(input("Informe o nome de qual cálculo que deseja realizar +  -  *  /: "))
x = int(input("Agora insira um número: "))
y = int(input("Insira o segundo número: "))
Soma = x + y
Subtração = x - y
Multiplicação = x * y
Divisão = x / y
if Programa == "+":
    print(Soma)
elif Programa == "-":
    print(Subtração)
elif Programa == "*":
    print(Multiplicação)
elif Programa == "/":
    print(Divisão)
print("="*50)
#Exercício 05

#Letra a
w = 0
while w <= 10:
    print(w)
    w += 1

#Letra b

for n in range(0,11):
    print(n)
    
