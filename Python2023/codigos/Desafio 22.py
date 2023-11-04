#Desafio 22. Crie um programa que leia o nome completo
#de uma pessoa e mostre:

#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
# Quantas letras ao todoo (sem considerar espaços).
#Quantas letras tem o primeiro nome

Pessoa = "Cristovão José Da Silva Caxilé"
print(Pessoa.upper())
print(Pessoa.lower())
print(len(Pessoa.replace(' ','')))
p1 = Pessoa.split()
print(len(p1[0]))