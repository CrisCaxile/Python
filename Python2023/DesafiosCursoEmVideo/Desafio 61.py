# Desafio 61. Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while

inicio = int(input('Informe o primeiro termo da PA:'))
razaoPA = int(input('Agora escolha um número para ser a razão da PA'))
for contagem in range(inicio,inicio+(razaoPA*10),razaoPA):
    print(contagem)

calculo = inicio+(razaoPA*10)
while inicio < calculo:
    print(inicio)
    inicio += razaoPA
