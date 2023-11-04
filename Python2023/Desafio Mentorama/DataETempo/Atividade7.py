# 7 - Escreva um programa python para subtrair 8 dias da data atual.
# Data atual: 25/01/2021
# Data esperada: 17/01/2021

import time,datetime

dataAtual = datetime.date.today()

sub = datetime.timedelta(days=8)

dataRequerida = dataAtual - sub

print(dataRequerida)