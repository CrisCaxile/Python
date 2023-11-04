# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

import moeda as m

pergunta = float(input('Digite um valor: '))
print(f'O dobro de {m.moeda(pergunta)} é: {m.moeda(m.dobro(pergunta))}')
print(f'A metade de {m.moeda(pergunta)} é : {m.moeda(m.metade(pergunta))}')
print(f'aumentando 10% de {m.moeda(pergunta)} é: {m.moeda(m.aumentar(pergunta,10))}')
print(f'diminuindo 10% de {m.moeda(pergunta)} é: {m.moeda(m.diminuir(pergunta,10))}')

