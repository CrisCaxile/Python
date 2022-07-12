# Exercicio 01, utilização de dois arquivos txt.

Lista_Enderecos = open("Lista De Endereços Ip.txt", "a+")
Lista_Enderecos.close()
Lista_Enderecos = open("Lista De Endereços Ip.txt", "w+")
Lista_Enderecos.write("""200.135.80.9"
"192.168.1.1"
"8.35.67.74"
"257.32.4.5"
"85.345.1.2"
"1.2.3.4"
"9.8.234.5"
"192.168.0.256""")
Lista_Enderecos.close()
Lista_Enderecos = open("Lista de Endereços Ip.txt", "r")
print(Lista_Enderecos.read())
Lista_Enderecos.close()

# Arquivo de saída
Arquivo = open("Relatório Ip.txt", "a+")
Arquivo.close()
Lista_Enderecos = open("Lista de Endereços Ip.txt", "r")
Lista_Enderecos = []
for lista in Lista_Enderecos:
    if lista == Lista_Enderecos.sort():
        Arquivo = open("Relatório Ip.txt", "w+")
        Arquivo.write("[Endereços válidos:]\n", lista)
    elif lista == Lista_Enderecos.sort(reverse = True):
        Arquivo.write("[Endereços inválidos:]\n", lista)
Arquivo.close()
Arquivo = open("Relatório Ip.txt", "r")
print(Arquivo.read())
Arquivo.close()