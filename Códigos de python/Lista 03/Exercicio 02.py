# Exercicio 02

class Quadrado:
    def __init__(self,TamanhoDoLado):
        self.TamanhoDoLado = TamanhoDoLado

    def MudarValorDoLado(self,A):
        print("Você mudou o valor do lado do quadrado para ",A)
        self.TamanhoDoLado = A

    def RetornarValorDoLado(self):
        print(self.TamanhoDoLado)

    def CalcularArea(self):
        print(self.TamanhoDoLado**2)

Objeto = Quadrado(4)

Objeto.RetornarValorDoLado()
Objeto.MudarValorDoLado(8)
Objeto.CalcularArea()