# Desafio 40. Crie um programa que leia duas notas de um aluno e calcule
# Sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira nota de um aluno: '))
n2 = float(input('Agora a segunda nota: '))

media = (n1+n2)/2

if media < 5:
    print('\033[31m Sua média foi:',media,'\n Você está em REPROVADO\033[m' )
elif media > 5 and media < 6.9:
    print('\033[33m Sua média foi:',media,'\n Você está em RECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[32m Sua média foi:',media,'\n Você foi APROVADO!\033[m')