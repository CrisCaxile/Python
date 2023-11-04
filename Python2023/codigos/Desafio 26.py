#Desafio 26. Faça um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez
#Em que posição ela aparecer a última vez

frase = input("Digite uma frase: ")
print("A quantidade de vezes que aparecer a letra 'A' é:", frase.upper().count('A'))
print('A primeira posição que aparece a letra "A" é:', frase.upper().find("A"))
print('A última posição que aparecer a letra "A" é:', frase.upper().rfind("A"))
