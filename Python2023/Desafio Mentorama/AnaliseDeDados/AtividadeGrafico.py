# 6

# grafico 1.

import pandas as pd
import matplotlib.pyplot as plt

Arquivo = pd.read_csv(R'C:\Users\Cris\Documents\Python\Python2023\Desafio Mentorama\AnaliseDeDados\1-dadosgovbr---2014.csv',sep=';',encoding='latin-1')

'''nota1 = len(Arquivo.loc[Arquivo['Nota do Consumidor'] == 1])
nota2 = len(Arquivo.loc[Arquivo['Nota do Consumidor'] == 2])
nota3 = len(Arquivo.loc[Arquivo['Nota do Consumidor'] == 3])
nota4 = len(Arquivo.loc[Arquivo['Nota do Consumidor'] == 4])
nota5 = len(Arquivo.loc[Arquivo['Nota do Consumidor'] == 5])


plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = (6,5)
cores = ['MidnightBlue','SteelBlue','RoyalBlue','SlateBlue','DodgerBlue']
plt.pie([nota1,nota2,nota3,nota4,nota5],autopct=f'%1.1f%%',startangle=90,colors=cores)
plt.title('Nota do Consumidor')
plt.legend(['Nota 1','Nota 2','Nota 3','Nota 4','Nota 5'],bbox_to_anchor=(0.95,0.2))
plt.figlegend([nota1,nota2,nota3,nota4,nota5],bbox_to_anchor=(0.26,0.31),title='Quantidade Notas')
plt.show()'''

# grafico 2

plt.style.use('dark_background')
RespostaDias = Arquivo['Tempo Resposta']
Maximo = RespostaDias.max()
Minimo = RespostaDias.min()
Media = RespostaDias.mean()
print(Maximo,Minimo,Media)
cores = ['Maroon','Salmon','Coral']
grafico = plt.bar(['Maximo','Minimo','Media'],[Maximo,Minimo,Media],color=['Maroon','Salmon','Coral'])
plt.bar_label(grafico,fmt="%.01f")
plt.title('Tempo de Resposta Empresa')
plt.ylabel('Dias')
plt.show()