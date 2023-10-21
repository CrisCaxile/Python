#Exercicio 07

class TV:
    def __init__(self,NumeroCanal):
        self.NumeroCanal = NumeroCanal
        self.Volume = 0


    def canal(self):
        if self.NumeroCanal < 0 or self.NumeroCanal > 100:
            print("Este canal não existe ou não está disponivel")
        else:
            print("O numero do canal atual é:")
            print(self.NumeroCanal)

    def AumentarVolume(self):
        self.Volume = Volume1
        if self.Volume > 100:
            print("O volume está no máximo !")
        else:
            self.Volume += P1
            print("Você aumentou o volume !")
            print("O volume está em ",self.Volume)

    def Volumee(self):
        self.Volume = Volume1
        print("O volume atual é :",self.Volume)

    def DiminuirVolume(self):
        self.Volume = Volume1
        if self.Volume < 0:
            print("O volume está em 0")
        else:
            self.Volume -= P2
            print("Você diminuiu o volume !")
            print("O volume está em ",self.Volume)
while True:

    NumeroDoCanal = float(input("Digite o numero do canal: "))
    Usuario = TV(NumeroDoCanal)
    Volume1 = float(input("Digite o valor do volume que deseja: "))
    Pergunta = input("Deseja continuar? S/N ")
    if Pergunta == "N":
        Usuario.Volumee()
        Usuario.canal()
        break
    Volume = input("Você deseja aumentar ou diminuir o volume? AUMENTAR/DIMINUIR ")
    if Volume == "AUMENTAR":
        P1 = float(input("Você deseja aumentar em quanto o volume? "))
        Usuario.AumentarVolume()
    else:
        P2 = float(input("Você desejar diminuir em quanto o volume?"))
        Usuario.DiminuirVolume()





