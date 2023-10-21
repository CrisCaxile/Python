#Exercício 06
#Letra a
print('\033[2;31mOs números pares são:\033[2;39m')
w = 2
Soma = 0
while w <= 10:
    print(w)
    w += 2
    Soma = Soma + w
print(f"\033[2;34mA soma dos números pares são : {Soma}")

print('\033[2;31mOs números ímpares são:\033[2;39m')
l = 1
Soma = 0
while l <= 9:
    print(l)
    l += 2
    Soma = l + Soma
print(f"\033[2;34mA soma dos números ímpares são: {Soma}")