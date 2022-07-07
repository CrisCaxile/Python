#Exercicio 08

class BombaCombustivel:
    def __init__(self,TipoCombustivel,ValorLitro,QuantidadeCombustivel):
        self.TipoCombustivel = TipoCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeCombustivel = QuantidadeCombustivel
        self.Valor1 = 0

    def AbastecerPorValor(self,D):
        self.Valor1 = D / Valor
        print("Você optou abastecer por valor, você abasteceu ",D,"R$, e deu ",self.Valor1," litros")



    def AbastecerPorLitro(self,E):
        self.ValorLitro = E * Valor
        print("Você desejou abastecer por litro, você abasteceu ",E,"litros, e deu ",self.ValorLitro," R$")



    def AlterarValor(self,C):
        self.Valor1 = C



    def AlterarCombustivel(self,B):
        self.TipoCombustivel = B
        print(self.TipoCombustivel)


    def AlterarQuantidadeCombustivel(self,A):
        self.QuantidadeCombustivel = A
        print(self.QuantidadeCombustivel)

print("\033[1;34mBEM VINDO ao sistema de abastecido do combustível !")
Tipo = input("Olá, você deseja abastecer pelo DIESEL,GASOLINA ou ETANOL? ").strip().upper()

if Tipo == "DIESEL":
    Valor = 7.59
elif Tipo == "GASOLINA":
    Valor = 6.89
elif Tipo == "ETANOL":
    Valor = 5.89

Funcao = input("\033[1;31mPrefere abaster por Litro ou por Valor? ").capitalize()
if Funcao == "Litro":
    QuantLitro = float(input("Qual a quantidade de Litro que deseja colocar? "))
    QuantCombustivel = QuantLitro
    Objeto1 = BombaCombustivel(Tipo, Valor, QuantCombustivel)
    Objeto1.AlterarCombustivel(Tipo)
    Objeto1.AlterarQuantidadeCombustivel(QuantCombustivel)
    Objeto1.AbastecerPorLitro(QuantLitro)

else:
    QuantValor = float(input("Quanto em R$ deseja abastecer? "))
    QuantCombustivel = QuantValor
    Objeto1 = BombaCombustivel(Tipo, Valor, QuantCombustivel)
    Objeto1.AlterarCombustivel(Tipo)
    Objeto1.AlterarQuantidadeCombustivel(QuantCombustivel)
    Objeto1.AbastecerPorValor(QuantValor)
print("\033[1;35mVocê tem na sua bomba de combustível",Objeto1.QuantidadeCombustivel,"litros")


