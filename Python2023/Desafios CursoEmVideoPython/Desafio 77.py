# Desafio 77 Crie um programa que tenha uma tupla com várias palavra
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra
# Quais são as suas vogais.

tupla = ('amar','projetar','fazer','ensolarado','agua','computador')

print(tupla[1])
tuplaVazia = str()

for contagem in range(0,6):
    for x in tupla[contagem]:
        if x in 'aeiou':
            tuplaVazia += x


tupla1 = tuplaVazia[0:2]
tupla2 = tuplaVazia[2:5]
tupla3 = tuplaVazia[5:7]
tupla4 = tuplaVazia[7:12]
tupla5 = tuplaVazia[12:15]
tupla6 = tuplaVazia[15:19]

tuplaConjunto = ((tupla1),(tupla2),(tupla3),(tupla4),(tupla5),(tupla6))

for x in range(0,6):
    print('Na palavra',tupla[x],'temos',tuplaConjunto[x])
