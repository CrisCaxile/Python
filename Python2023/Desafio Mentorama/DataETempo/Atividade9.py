# 9 - Faça um programa que calcule a diferença em dias entre antes de ontem
# e depois de amanhã

import datetime

hoje = datetime.date.today()

fator = datetime.timedelta(days=2)

antesDeOntem = hoje - fator
depoisDeAmanha = hoje + fator

print(f'A data de hoje é: {hoje}\nAntes de ontem é:{antesDeOntem}\nDepois de amanhã é:{depoisDeAmanha}')