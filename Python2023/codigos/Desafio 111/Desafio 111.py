# Crie um pacote chamado utilidadesCeV que tenha dois pacotes internos
# chamados moeda e dado. Transfira todas as funções utilizadas nos desafios
# 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando

from utilidadesCeV import moeda as m

pergunta = float(input('Digite um valor: '))
m.resumo(pergunta,45,22)