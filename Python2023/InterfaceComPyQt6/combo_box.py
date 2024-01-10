import sys
import PyQt6.QtWidgets as pq

def ler_combobox():
    valor = combo.currentText()
    label2.setText(valor)

app = pq.QApplication(sys.argv)

janela = pq.QWidget()
janela.resize(500,500)
janela.setWindowTitle('Combo Box')


botao = pq.QPushButton('MOSTRAR OPÇÃO',janela)
botao.setGeometry(300,90,130,80)
botao.clicked.connect(ler_combobox)

label = pq.QLabel(janela)
label.move(10,200)
label.setText('OPÇÃO SELECIONADA: ')

label2 = pq.QLabel(janela)
label2.move(140,200)
label2.setText('                  ')

combo = pq.QComboBox(janela)
combo.addItem('Selecione uma linguagem de programação')
combo.addItem('Java')
combo.addItem('Python')
combo.addItem('JavaScript')
combo.addItem('Rust')
combo.addItem('C++')
combo.addItem('PHP')
combo.move(10,10)



janela.show()

app.exec()