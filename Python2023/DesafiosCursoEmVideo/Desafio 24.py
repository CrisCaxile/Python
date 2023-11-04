#Desafio 24. Crie um programa que leia o nome de uma cidade e diga se
#ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ')
c = cidade.upper()
d = "SANTO" in c[:5]
print('A cidade começa com "SANTO" no nome? ', d)