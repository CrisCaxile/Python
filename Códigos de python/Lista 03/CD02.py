# Exercicio 01

Lista = []
c = 1
def ParOuImpar(valor):
    Par = []
    Impar = []
    for x in valor:
        if x % 2 == 0:
           Par.append(x)
        else:
           Impar.append(x)
    print("Os valores pares e impares consecutivos são: ")
    return Par,Impar



try:
    while c <= 5:
        Valores = int(input("Digite 5 numeros: "))
        Lista.append(Valores)
        c = c + 1

    Verificar = ParOuImpar(Lista)
    print(Verificar)
except Exception as erro:
    print("O tipo de erro foi :",erro.__class__)


