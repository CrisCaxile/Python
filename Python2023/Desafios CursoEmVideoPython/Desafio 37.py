# Desafio 37. Escreva um programa que leia um número inteiro qualquer
# E peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

leitor = int(input('Digite um número inteiro qualquer: '))

Escolha = int(input('Agora digite qual a base de conversão que você deseja.\n\033[34m'
                    '1 para binário\n'
                    '2 para octal\n'
                    '3 para hexadecimal: \033[m'))

if Escolha == 1:
    print('\033[33mO número convertido para BINÁRIO é igual a:',bin(leitor)[2:],'\033[m')
elif Escolha == 2 :
    print('\033[35m O número convertido para OCTAL é igual a:',oct(leitor)[2:],'\033[m')
elif Escolha == 3 :
    print('\033[36m O número convertido para hexadecimal é igual a:',hex(leitor)[2:],'\033[m')
else:
    print('\033[31m O número digitado não está nas opções.\033[m')
