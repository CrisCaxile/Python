# 1- Mostre a data de hoje conforme exemplo: "segunda, 02 de janeiro de 1994"
import datetime
import time

data = time.asctime()
diaData = data[8:10]
diaSemana = data
mes = data[4:7]
separado = data.split(' ')
ano = separado[-1]
print(data)
print(f'{separado[0]},{diaData} de {mes} de {ano}')

# 2- Converter um objeto datetime para date
data1 = datetime.datetime.now()
print(data1.date())

# 3- Converter um objeto datetime para time
data2 = datetime.datetime.now()
print(data2.time())

# 4- Observe que o horário do exercício anterior está com o fuso horário
# incorreto. Converta para horário de Brasília. Observe também que o horário
# de Brasília tem 3 horas de diferença da hora apresentada. Isso vai facilitar a conversão
import time

data3 = time.localtime()

