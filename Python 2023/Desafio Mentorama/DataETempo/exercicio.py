import time

print(f'O método construtor inicial é gmtime(0) com parametro "0", porém o gmtime() é igual ao localtime() :{time.gmtime(0)}')
print(f'Os segundos desde a época é: {time.time()}')
print(f'O tempo local completo: {time.ctime()}')
print(f'O tempo local completo também,pois, o ctime é igual ao asctime: {time.asctime()}')
print(f'O método construtor do gmtime através da data atual: {time.localtime()}')
print(f'O dia de hoje pelo sistema é: {time.localtime()[2]} e o mês {time.localtime()[1]}')
print(f'O ano atual pelo sistema é: {time.localtime()[0]}')
print(f'A hora atual do sistema é: {time.localtime()[3]}:{time.localtime()[4]}:{time.localtime()[5]}')
print(f'A hora do sistema é: {time.ctime()[11:20]}')
print(f'O dia do sistema é: {time.gmtime()[2]}')
print(f"A função strftime() utiliza dois argumentos o primeiro %y ou %M,m,h,d,s para definir o year ou mouth ou day e o segundo é o locatime():{time.strftime('%Y',time.localtime())}")

tempoI = time.time()
lista = [1,5,7,6]
for c in lista:
    print(c)
tempoF = time.time()
print(f'O tempo gasto foi de {tempoF-tempoI} segundos')

#n,m = map(int,input().split())
#for c,d in zip(range(0,2),(range(13,14))):
   # print(c,d)

import datetime as d

data = d.datetime.now()
print(d.datetime.now().hour)
print(d.date.today().month)