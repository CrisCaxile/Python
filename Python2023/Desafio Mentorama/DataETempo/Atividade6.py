# 6- Escreva um programa Python capaz de converter uma string em data e hora.
# String de exemplo: 01 de janeiro de 2021 13h53
# Resultado esperado: 2021-01-01 13:53:00

import datetime
import time

string = '2021-01-01-13-53-00'

conversao = datetime.datetime.strptime(string,'%Y-%m-%d-%H-%M-%S')
print(conversao)
