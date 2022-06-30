print("Bem vindo ao programa PY, irei te ajudar a mostrar quais são os maiores e menores valores.")
man = 0
men = 999
for x in range (3):
    Jogador = float(input("Digite um número: "))

    if Jogador > man:
        man = Jogador
    if Jogador < men:
        men = Jogador

print(f"O menor número é {men} e o maior número é {man}")
