# Desafio 41 A confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de
# Acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SêNIOR
# Acima: MASTER

programa = int(input('Digite o ano de nascimento do atleta: '))
conversao = 2023 - programa

if conversao <= 9:
    print('A idade do atleta é:',conversao,'\n Portanto sua categoria é:\033[31m MIRIM \033[m')
elif conversao > 9 and conversao <= 14:
    print('A idade do atleta é:',conversao,'\n Sua categoria é:\033[32m INFANTIL \033[m')
elif conversao > 14 and conversao <= 19:
    print('A idade do atleta é:',conversao,'\n Dessa forma, sua categoria é: \033[33m JUNIOR \033[m')
elif conversao == 20:
    print('A idade do atleta é:',conversao,'\n Assim, sua categoria é:\033[34m SêNIOR \033[m')
elif conversao > 20:
    print('A idade do atleta é:',conversao,'\n Dessa maneira, sua categoria é: \033[35m MASTER \033[m')
