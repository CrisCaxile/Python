from datetime import date
print("Bem vindo ao programa ! Espero poder te auxiliar na sua dúdvida.")
Leitor = int(input("Informe um ano ? Coloque 0 para analisar o ano atual:"))
if Leitor == 0:
    Leitor = date.today().year
if Leitor%4 == 0 and Leitor%100 != 0 or Leitor%400 == 0:
    print(f"O ano de {Leitor} é bissexto!")
else:
    print(f"O ano de {Leitor} não é bissexto!")
