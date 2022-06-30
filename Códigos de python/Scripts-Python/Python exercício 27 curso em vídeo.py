nome = str(input('Digite seu nome completo: ')).strip().lower()
PN = nome.split()[0]
UN = nome.split()
print(f'Prazer em te conhecer {nome} !!')
print(f'Seu primeiro nome é {PN}')
print(f'Seu ultimo nome é {UN[len(UN)-1]}')
