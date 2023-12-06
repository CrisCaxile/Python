import pandas

arrayU = pandas.Series([1,2,3,4,5,6],index=['alfa','b','c','d','e','f'])
print(arrayU)

Data = {
    'País':['Brasil','Argentina','Portugal'],
    'Capital':['Brasilia','Buenos Aires','Lisboa'],
    'População':[214.3,45.81,10.33]
}

DataFrame = pandas.DataFrame(Data,index=['a','b','c'],columns=['País','Capital','População'])
print(DataFrame)
print(DataFrame.count())
print(DataFrame.head())
print(DataFrame.columns)
print(DataFrame.shape)
print(DataFrame.describe())
print(DataFrame.index)
DataFrame['Nova Coluna'] = 23
print(DataFrame)
DataFrame.drop('Nova Coluna',axis=1)
print(DataFrame)
DataFrame.columns = ['ColunaA','ColunaB','ColunaC','ColunaD']
print(DataFrame)
print(DataFrame.rename({'ColunaD':'DI'},axis='columns'))
print(arrayU.drop('alfa'))
print(DataFrame.loc[['a'],['ColunaA']])
print(DataFrame.loc[['b'],['ColunaC']])
print(DataFrame.drop('ColunaB',axis='columns'))
print(DataFrame.max())
help(DataFrame.sort_values)
print(DataFrame.sort_values(by=['ColunaA'],ascending=False))