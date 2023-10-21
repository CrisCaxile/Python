# Exercicio 05
# Inserir um elemento no início de um dicionário ordenado

print("Dicionário Ordenado Original")

DicionarioOrdenado = [("Color1","Red"),("Color2","Green"),("Color3","Blue")]
print(DicionarioOrdenado)
print(type(DicionarioOrdenado))

print("Dicionário Ordenado Atualizado")
DicionarioOrdenado.insert(0,("Color4","Orange"))
DicionarioOrdenado = dict(DicionarioOrdenado)
print(DicionarioOrdenado)
print(type(DicionarioOrdenado))
