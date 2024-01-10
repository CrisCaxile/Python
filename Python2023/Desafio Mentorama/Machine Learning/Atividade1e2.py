from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Importar a base de dados
mnist = fetch_openml('mnist_784', version=1, parser='auto')

# Dividir a base de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    mnist.data, mnist.target, test_size=0.80, random_state=42
)

# Definir o modelo de classificação
clf = KNeighborsClassifier()

# Treinar o modelo
clf.fit(X_train, y_train)

# Avaliar o modelo
y_pred = clf.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Matriz de confusão:")
print(confusion_matrix(y_test, y_pred))

# O modelo teve uma boa performance porque a acuracia foi alta
# as dificuldade são no entendimentos do contexto geral para a crianção do modelo
# esse assunto é bem complexo e é dificil de entendimento