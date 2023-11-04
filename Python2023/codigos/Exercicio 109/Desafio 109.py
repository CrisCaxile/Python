# Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
# pela função moeda(), desenvolvida no desafio 108

import moeda as m

pergunta = float(input('Digite um valor: '))
print(f'O dobro de {m.moeda(pergunta)} é: {m.dobro(pergunta,True)}')
print(f'A metade de {m.moeda(pergunta)} é : {m.metade(pergunta,True)}')
print(f'aumentando 10% de {m.moeda(pergunta)} é: {m.aumentar(pergunta,10,True)}')
print(f'diminuindo 10% de {m.moeda(pergunta)} é: {m.diminuir(pergunta,10,True)}')

