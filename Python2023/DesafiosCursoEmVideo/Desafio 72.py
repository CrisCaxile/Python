# Desafio 72 Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

print('@'*50)
print('\033[33m PROGRAMA DE TUPLAS \033[m')
print('@'*50)

tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

pergunta = input('Escolha um número entre 0 e 20: ')

while pergunta not in "0123456789":
    pergunta1 = input('Tente novamente. Escolha um número entre 0 e 20: ')
    pergunta = pergunta1

if pergunta in '0123456789':
    print('O número por extenso é:', tupla[int(pergunta)])


print('FIM.............')
