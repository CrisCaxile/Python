# 4- Escreva um programa para obter uma lista de datas entre duas datas.
# Considere o passo de um dia e reproduza o intervalo das datas entre
# 16/10/87 e 25/10/87

import datetime

Pdata = datetime.date(day=16,month=10,year=1987)
Sdata = datetime.date(day=26,month=10,year=1987)

passo = datetime.timedelta(days=1)

for c in range((Sdata-Pdata).days):
    print(Pdata+c*passo)

