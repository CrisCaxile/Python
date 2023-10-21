# Exercicio 01, utilização de dois arquivos txt.

with open("Lista de Enderecos Ip.txt","w+") as Lista_Enderecos:
    Lista_Enderecos.write("""200.135.80.9"
"192.168.1.1"
"8.35.67.74" 
"257.32.4.5"
"85.345.1.2"
"1.2.3.4"
"9.8.234.5" 
"192.168.0.256""")

with open("Lista de Enderecos Ip.txt","r") as Lista_Enderecos:
    print(Lista_Enderecos.read())


# Transformando o o arquivo de txt Lista de Endereços que é string em lista.

with open("Lista de Enderecos Ip.txt","a+",encoding= "utf-8") as Lista_Enderecos:
    Lista = [Lista_Enderecos]

#Após transformar a string em lista, utilizarei a função sorted() para organizar a lista.

with open("Relatório Ip.txt","w+") as Relatorio:
    for Lista1 in Lista:
        if Lista == sorted(Lista):
            Relatorio.write(f"[Endereços válidos:]\n {Lista1}")
        elif Lista != sorted(Lista):
            Relatorio.write(f"[Endereços inválidos:]\n {Lista1}")

with open("Relatório Ip.txt","r") as Relatorio:
    variavel = Relatorio.read()
    print(variavel)