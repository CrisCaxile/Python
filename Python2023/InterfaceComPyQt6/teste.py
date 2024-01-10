import sys
import PyQt6.QtWidgets as pq
import matplotlib.pyplot as plt

def F_Botao():
    botao.deleteLater()
    print('mensagem')
    mensagem.setText('Mensagem 1')
    mensagem.adjustSize()

def grafico():
    plt.rcParams['figure.figsize']=(4,2)
    plt.plot([1,2,3])
    plt.show()

app = pq.QApplication(sys.argv)

janela = pq.QWidget()
janela.setStyleSheet('background-color:black')
janela.resize(700,500)
janela.setWindowTitle('Assistant')

botao = pq.QPushButton('BOTAO 1',janela)
botao.setGeometry(300,200,100,60)
botao.setStyleSheet('color:white;background-color:darkgreen')
botao.clicked.connect(F_Botao)

mensagemTitulo = pq.QLabel(janela)
mensagemTitulo.setText('INICIO')
mensagemTitulo.setStyleSheet('color:white;font-size:35px')
mensagemTitulo.move(300,60)

mensagem = pq.QLabel(janela)
mensagem.move(300,170)
mensagem.setStyleSheet('color:white;font-size:20px')

mensagemCris = pq.QLabel(janela)
mensagemCris.move(650,470)
mensagemCris.setText('By Cris')
mensagemCris.setStyleSheet('color:white')

opcoes = pq.QComboBox(janela)
opcoes.setStyleSheet('background-color:white')
opcoes.move(10,10)
opcoes.addItem('Selecione Um Item')
opcoes.addItem('Verificar Gráfico')

# NAO TO CONSEGUINDO CONECTAR O VERIFICAR GRAFICO NA FUNCAO GRAFICO
if opcoes.setItemData(1) == 'Verificar Gráfico':
    opcoes.currentIndexChanged.connect(grafico)

janela.show()
app.exec()