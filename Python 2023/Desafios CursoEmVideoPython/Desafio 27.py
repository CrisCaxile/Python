#Desafio 27. Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = input("Digite o nome completo de uma pessoa: ")
separacaoNome = nome.split()
print("primeiro nome é:", separacaoNome[0])
print('O último nome é:', separacaoNome[-1])