import matplotlib.pyplot as plt
import pandas
'''print(plt.style.available)
plt.style.use('seaborn-v0_8-dark-palette')
plt.rcParams['figure.figsize'] = (8,6)


x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
a = [22,33,44,55]
b = [1,2,3,4]
plt.pie(a,shadow=True,autopct=f'%1.1f%%',startangle=90,explode=(0.1,0,0,0),labels=['Calças','Sapatos','Camisas','Meias'])
plt.savefig('nome_da_imagem.png')
plt.title('Produtos')
plt.figlegend(a)
plt.show()'''

Data1 = {
    'x':[1,2,3,4,5,6,7,8,9,10],
}

Data2 = {
    'y':[11,12,13,14,15,16,17,18,19,20]
}

df1 = pandas.DataFrame(Data1,columns=['x'])
df2 = pandas.DataFrame(Data2,columns=['y'])

plt.rcParams['figure.figsize']=(9,6)
plt.plot(df1,marker='o',color='r')
plt.plot(df2,marker='o',color='b')
for numero in range(1,3):
    plt.legend(f'xy{numero}')
plt.title('Exemplo')
plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.savefig('DataFrame.png')
plt.show()