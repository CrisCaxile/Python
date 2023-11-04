#Desafio 25. Crie um programa que leia o nome de uma pessoa e diga se
# tem "SILVA" no nome.

nome = input("Digite o nome completo: ")
Silva = "SILVA" in nome.upper()
print('O nome que você digitou tem silva? ',Silva)