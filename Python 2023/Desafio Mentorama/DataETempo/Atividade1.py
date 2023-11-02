# 1 - Escreva scripts para mostrar os diversos formatos de tempo conforme se segue:

# a) Impressão da época padrão
import time

print(f'A época padrão é \033[36m:{time.gmtime(0)}\033[m')

# b) Segundos que se passaram desde a época

print(f'Os segundos desde a época padrão são: \033[35m{time.time()}\033[m')

# c) Imprime dados do tempo no momento atual

print(f'Utilizando o asctime temos dados do tempo no momento atual:\n\033[33m {time.asctime()}\033[m')

#d) Cria um objeto time.locatime() e imprime o valor das horas, minutos e segundos

print(f'Utilizando o local time temos: \033[31m{time.localtime()}\033[m')

#e) Imprime se no momento atual estamos em horário de verão ou não

funcao = time.localtime()[-1]
if funcao == 1:
    resposta = 'Sim'
elif funcao == 0:
    resposta = 'Não'
elif funcao == -1:
    resposta = 'Desconhecido'
print(f'Estamos em horário de verão? {resposta}')
