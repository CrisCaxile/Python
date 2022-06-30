# Exercício 01

# Letra A
import statistics
variavel = []
pessoas = []
ListaMulheres = []
PessoasA = []

for x in range(5):
    Nome = input("Digite o nome do cliente: ")
    Sexo = input("Digite o sexo do cliente: ")
    Idade = int(input("Informe a idade do cliente: "))

    variavel.append({
        "Nome": Nome,
        "Sexo": Sexo,
        "Idade": Idade
    })
    pessoas.append(Idade)
    media = round(statistics.mean(pessoas))

for mulheres in variavel:
    if mulheres["Sexo"] == "f" or mulheres["Sexo"] == "F":
        ListaMulheres.append(mulheres.values())

for acima in variavel:
    if acima["Idade"] > media:
        PessoasA.append(acima.values())

print(variavel)
print(f"\033[1;34m Foram cadastradas {len(variavel)} pessoas")


#letra b


print(f"\033[1;36m A média de idade de pessoas é: {media}")

#letra c

print(f"\033[1;31m A lista de mulheres é: {ListaMulheres} ")

#letra d

print(f"\033[1;37m A lista de pessoas com idade acima da média é: {PessoasA}")