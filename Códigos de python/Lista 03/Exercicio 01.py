# Exercício 01

class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def TrocaCor(self,A):
        print("A cor da bola foi trocada para a cor",A)


    def MostraCor(self):
        print(self.cor)

bola = Bola("azul",270,"plastico")

bola.MostraCor()
bola.TrocaCor("verde")