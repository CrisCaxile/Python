#Exercicio 04

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        print("Você envelheceu mais um ano !")

    def engordar(self):
        print("Você engordou, seu corpo está tendo um superávit de calorias.")

    def emagrecer(self):
        print("Você emagreceu,seu corpo está tendo um déficit de calorias.")

    def crescer(self,A):
        if self.idade < 21:
            B = A*0.05
            self.altura = B + self.altura
            print("Você cresceu mais 0.5 cm de altura.")
        else:
            print("Você ja passou dos 21 anos, não irá mais aumentar de altura !")

pessoa1 = Pessoa("Lauro",18,64.0,1.73)
pessoa1.crescer(2)
print(pessoa1.altura)