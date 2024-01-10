import PyQt6.QtWidgets as pq
import sys

def funcao1():
    label.setText('Botão 1 pressionado!')
    label.adjustSize()

def funcao2():
    label.setText('Botão 2 pressionado!')
    label.adjustSize()

def funcao3():
    valor_lido = le.text()
    label.setText(valor_lido)
    label.adjustSize()

app = pq.QApplication(sys.argv)

janela = pq.QWidget()
janela.resize(800,600)
janela.setWindowTitle('Primeira')


btn = pq.QPushButton('Botao 1',janela)
btn.setGeometry(100,100,150,80)
btn.clicked.connect(funcao1)

btn2 = pq.QPushButton('Botao 2',janela)
btn2.setGeometry(100,300,150,80)
btn2.clicked.connect(funcao2)

btn3 = pq.QPushButton('Botao 3',janela)
btn3.setGeometry(100,500,150,80)
btn3.clicked.connect(funcao3)


label = pq.QLabel('Texto',janela)
label.move(400,100)
label.setStyleSheet('font-size:30px')

le = pq.QLineEdit("",janela)
le.setGeometry(500,300,150,40)

janela.show()

app.exec()