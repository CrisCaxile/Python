print('='*50)
print("Bem vindo !")
print('='*50)
Funcionario = float(input("Digite o valor do seu salário: "))
if Funcionario > 1250:
    print(f"O seu novo salário é {Funcionario + (Funcionario * 10/100)} R$")
else:
    print(f"O seu novo salário é {Funcionario + (Funcionario * 15/100)} R$")
