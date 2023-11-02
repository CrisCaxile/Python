# 8- Escreva um programa Python para calcular o número de dias entre
# dois datetimes. A diferença entre os dias dever ser igual a 10

import datetime

dia1 = datetime.date.today()
fator = datetime.timedelta(days=10)
dia2= dia1-fator

print(dia2)