import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_csv('1-dadosgovbr---2014.csv',sep = ';', encoding='latin-1')

#questão 1:
print(f'Foram registradas {arquivo["Problema"].count()} reclamações')
print('-='*20)

# questão 2:
print(f'O tempo maximo de resposta foi: {arquivo["Tempo Resposta"].max()}')
print(f'O tempo mínimo de resposta foi: {arquivo["Tempo Resposta"].min()}')
print(f'O tempo médio de resposta foi: {(arquivo["Tempo Resposta"].mean()).round(2)}')
print('-='*20)

# questão 3:
print(f'A nota máxima do consumidor foi de: {arquivo["Nota do Consumidor"].max()} ')
print(f'A nota mínima do cosumidor foi de: {arquivo["Nota do Consumidor"].min()}')
print(f'A nota média do consumidor foi de: {(arquivo["Nota do Consumidor"].mean()).round(1)}')
print('-='*20)

# questão 4:
# Podemos correlacionar a nota do consumidor com o tempo de resposta da seguinte forma, se a nota do consumidor for alta
# o tempo de reposta foi rápido e se a nota do consumidor for baixa o tempo de resposta foi alto.

# questão 5:
print(arquivo['UF'])
print(f'A quantidade reclamação do sexo masculino é:',end=' ')
homens = arquivo.loc[arquivo['Sexo'] == 'M']
print(len(homens))
print(f'A quantidade de reclamação do sexo feminino é:',end=' ')
mulheres = arquivo.loc[arquivo['Sexo'] == 'F']
print(len(mulheres))
print('-='*20)

# questão 6:
print('A quantidade de reclamações por estados são:')
print(f'Rio de Janeiro: {len(arquivo.loc[arquivo["UF"] == "RJ"])}')
a = len(arquivo.loc[arquivo["UF"] == "RJ"])

print(f'Espirito Santo: {len(arquivo.loc[arquivo["UF"] == "ES"])}')
b = len(arquivo.loc[arquivo["UF"] == "ES"])

print(f'Maranhão: {len(arquivo.loc[arquivo["UF"] == "MA"])}')
c = len(arquivo.loc[arquivo["UF"] == "MA"])

print(f'Tocantins: {len(arquivo.loc[arquivo["UF"] == "TO"])}')
d = len(arquivo.loc[arquivo["UF"] == "TO"])

print(f'Piaui: {len(arquivo.loc[arquivo["UF"] == "PI"])}')
e = len(arquivo.loc[arquivo["UF"] == "PI"])

print(f'Rio Grande do Norte: {len(arquivo.loc[arquivo["UF"] == "RN"])}')
f = len(arquivo.loc[arquivo["UF"] == "RN"])

print(f'Alagoas: {len(arquivo.loc[arquivo["UF"] == "AL"])}')
g = len(arquivo.loc[arquivo["UF"] == "AL"])

print(f'Pernambuco: {len(arquivo.loc[arquivo["UF"] == "PE"])}')
h = len(arquivo.loc[arquivo["UF"] == "PE"])

print(f'Sergipe: {len(arquivo.loc[arquivo["UF"] == "SE"])}')
i = len(arquivo.loc[arquivo["UF"] == "SE"])

print(f'Paraíba: {len(arquivo.loc[arquivo["UF"] == "PB"])}')
j = len(arquivo.loc[arquivo["UF"] == "PB"])

print(f'Bahia: {len(arquivo.loc[arquivo["UF"] == "BA"])}')
k = len(arquivo.loc[arquivo["UF"] == "BA"])

print(f'Rondonia: {len(arquivo.loc[arquivo["UF"] == "RO"])}')
l = len(arquivo.loc[arquivo["UF"] == "RO"])

print(f'Roraima: {len(arquivo.loc[arquivo["UF"] == "RR"])}')
m = len(arquivo.loc[arquivo["UF"] == "RR"])

print(f'Acre: {len(arquivo.loc[arquivo["UF"] == "AC"])}')
n = len(arquivo.loc[arquivo["UF"] == "AC"])

print(f'Pará: {len(arquivo.loc[arquivo["UF"] == "PA"])}')
o = len(arquivo.loc[arquivo["UF"] == "PA"])

print(f'Amazonas: {len(arquivo.loc[arquivo["UF"] == "AM"])}')
p = len(arquivo.loc[arquivo["UF"] == "AM"])

print(f'Minas Gerais: {len(arquivo.loc[arquivo["UF"] == "MG"])}')
q = len(arquivo.loc[arquivo["UF"] == "MG"])

print(f'São Paulo: {len(arquivo.loc[arquivo["UF"] == "SP"])}')
r = len(arquivo.loc[arquivo["UF"] == "SP"])

print(f'Mato Grosso: {len(arquivo.loc[arquivo["UF"] == "MT"])}')
s = len(arquivo.loc[arquivo["UF"] == "MT"])

print(f'Mato Grosso do sul: {len(arquivo.loc[arquivo["UF"] == "MS"])}')
t = len(arquivo.loc[arquivo["UF"] == "MS"])

print(f'Goiás: {len(arquivo.loc[arquivo["UF"] == "GO"])}')
u = len(arquivo.loc[arquivo["UF"] == "GO"])

print(f'Santa Catarina: {len(arquivo.loc[arquivo["UF"] == "SC"])}')
v = len(arquivo.loc[arquivo["UF"] == "SC"])

print(f'Paraná: {len(arquivo.loc[arquivo["UF"] == "PR"])}')
w = len(arquivo.loc[arquivo["UF"] == "PR"])

print(f'Rio Grande do sul: {len(arquivo.loc[arquivo["UF"] == "RS"])}')
x = len(arquivo.loc[arquivo["UF"] == "RS"])

print(f'Distrito Federal: {len(arquivo.loc[arquivo["UF"] == "DF"])}')
y = len(arquivo.loc[arquivo["UF"] == "DF"])

print(f'Amapá: {len(arquivo.loc[arquivo["UF"] == "AP"])}')
z = len(arquivo.loc[arquivo["UF"] == "AP"])

print(f'Ceará: {len(arquivo.loc[arquivo["UF"] == "CE"])}')
ab = len(arquivo.loc[arquivo["UF"] == "CE"])

print('-='*20)

#questão 7:

print('A porcentagem de reclamações registradas e não respondidas é de:',end=' ')
print(round(len(arquivo.loc[arquivo['Respondida'] == 'N'])/43987,2),'%')
print('-='*20)

# Gráfico:

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = (8,5)



# 5.a
plt.bar('Homens',len(homens))
plt.bar('Mulheres',len(mulheres))
plt.title('Frequência de Reclamações por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Frequência de reclamação')
plt.legend(['27.895','16.092'])
plt.show()


# 5.b
plt.rcParams['figure.figsize'] = (13.5,6.5)
plt.bar('RJ',a)
plt.bar('ES',b)
plt.bar('MA',c)
plt.bar('TO',d)
plt.bar('PI',e)
plt.bar('RN',f)
plt.bar('AL',g)
plt.bar('PE',h)
plt.bar('SE',i)
plt.bar('PB',j)
plt.bar('BA',k)
plt.bar('RO',l)
plt.bar('RR',m)
plt.bar('AC',n)
plt.bar('PA',o)
plt.bar('AM',p)
plt.bar('MG',q)
plt.bar('SP',r)
plt.bar('MT',s)
plt.bar('MS',t)
plt.bar('GO',u)
plt.bar('SC',v)
plt.bar('PR',w)
plt.bar('RS',x)
plt.bar('DF',y)
plt.bar('AP',z)
plt.bar('CE',ab)

plt.title('Frequência de Reclamações por Estado')
plt.xlabel('Estados')
plt.ylabel('Frequência de Reclamações')

plt.legend(['RJ = 4907',
'ES = 1081',
'MA = 1082',
'TO = 46',
'PI = 77',
'RN = 160',
'AL = 104',
'PE = 1626',
'SE = 97',
'PB = 343',
'BA = 2443',
'RO = 119',
'RR = 24',
'AC = 449',
'PA = 211',
'AM = 291',
'MG = 4186',
'SP = 11882',
'MT = 1012',
'MS = 531',
'GO = 886',
'SC = 1458',
'PR = 6140',
'RS = 1941',
'DF = 1805',
'AP = 18',
'CE = 1068'],ncol=3)

plt.show()

# 5.C
cores = ['MidnightBlue','DarkRed']
respondida = len(arquivo.loc[arquivo['Respondida'] == 'S'])
nrespondida = len(arquivo.loc[arquivo['Respondida'] == 'N'])
plt.pie([respondida,nrespondida],autopct=f'%1.1f%%',colors=cores)
plt.title('Frequência de Reclamações Respondidas e não Respondidas')
plt.xlabel('Frequência de Reclamações')
plt.legend(['Respondido','Não-Respondido'],bbox_to_anchor=(0,0.9))

plt.show()