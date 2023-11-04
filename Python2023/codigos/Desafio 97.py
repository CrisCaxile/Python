# Desafio 97 Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptavel
# ex: escreva('Olá,mundo !')
# saída:
# ------------
# Olá, Mundo!
# ------------

def Escreva(argumento):
    print('~'*(len(argumento)+2))
    print(argumento)
    print('~'*(len(argumento)+2))

print('\033[34m~'*28)
print('\033[m Programa da Função Escreva()')
print('\033[34m~'*28,'\033[m')

pergunta = input('Digite uma frase para colocar na função: ')
Escreva(pergunta)
