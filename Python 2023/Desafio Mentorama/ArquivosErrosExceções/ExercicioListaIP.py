# Faça um programa que leia um arquivo texto contendo uma lista de endereços
# IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos
# e inválidos.

# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
#[Endereços válidos:]
#200.135.80.9
#192.168.1.1
#8.35.67.74
#1.2.3.4
#[Endereços inválidos:]
#257.32.4.5
#85.345.1.2
#9.8.234.5
#192.168.0.256

# Arquivo de entrada
arquivo = open('ListaEndereçosIP.txt', 'w+')
arquivo.write('200.235.80.9\n192.168.1.1\n8.35.67.74\n257.32.4.5\n85.345.1.2\n1.2.3.4\n9.8.234.5\n192.168.0.256')
dicionario = {1:'200.235.80.9',2:'192.168.1.1',3:'8.35.67.74',4:'257.32.4.5',5:'85.345.1.2',6:'1.2.3.4',7:'9.8.234.5',8:'192.168.0.256'}
arquivo.close()

# arquivo de saída
import Função

arquivo = open('ListaEndereçosIP.txt', 'r')
print('\033[33mLISTA DE IPS:\033[m\n')
print(arquivo.read(),'\n')
arquivo.close()

relatorio = open('RelatorioIp.txt', 'w+')
relatorio.write(Função.verificar(dicionario))
relatorio.close()

relatorio = open('RelatorioIp.txt', 'r')
print(relatorio.read())









