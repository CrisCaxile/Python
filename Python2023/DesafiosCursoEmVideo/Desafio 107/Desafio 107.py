# Crie um módulo chamado moeda.py que tenha funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use
# algumas dessas funções

import moeda as m

pergunta = float(input('Digite um valor: '))
print(f'O dobro de {pergunta} é: {m.dobro(pergunta)}')
print(f'A metade de {pergunta} é : {m.metade(pergunta)}')
print(f'aumentando 10% de {pergunta} é: {m.aumentar(pergunta,10)}')
print(f'diminuindo 10% de {pergunta} é: {m.diminuir(pergunta,10)}')

