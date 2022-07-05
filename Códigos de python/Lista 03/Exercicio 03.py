#Exercicio 03

class Retangulo:
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura

    def MudarValorDosLados(self,A,B):
        print("Você mudou o valor do comprimento para:",A," e o valor da largura para:",B)
        self.comprimento = A
        self.largura = B

    def RetornarValorDosLados(self):
        print("O retangulo tem ",self.comprimento," de comprimento e ",self.largura," de largura" )

    def CalcularArea(self):
        CalculoAreaInterna = float(comprimento - 0.40) * (largura - 0.40)
        Acrescimo = (CalculoAreaInterna * 10) / 100
        CalculoComAcrescimo = CalculoAreaInterna + Acrescimo
        QuantCaixaPiso = CalculoComAcrescimo / 1.5
        print(round(QuantCaixaPiso))

        # os 0,40 cm que subtraí foi da expessura das paredes, para saber a parte interna dos cômodos
        # Nesse exercicio utilizei um piso de porcelanato que possui 1,5m².

    def CalcularPerimetro(self):
        CalcRodape = (comprimento * 2 + largura + (largura - 0.80)) * 0.10
        QuantRodape = CalcRodape / 1.5
        print(round(QuantRodape))

        # considerei no calculo do rodapé - o perimetro e 0,80cm de largura para a porta.
        # e a multiplicação * 10cm de acrescimo de segurança do perímetro.

comprimento = float(input("Digite a medida do comprimento do local: "))
largura = float(input("Digite a medida da largura do local: "))

objeto = Retangulo(comprimento,largura)

print("A quantidade de piso para o local é de  caixas de 1,50 cm²")
objeto.CalcularArea()
print("A quantidade de rodapé para o local é de caixas de 1,50 cm²")
objeto.CalcularPerimetro()


