from PyQt6.QtCore import QSize, Qt, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QSystemTrayIcon, QSlider, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QIcon

import sys
import os.path as path
import threading

import audio
from audio import volumeAtual

'''
     --------------------------------------------------------------------------
     |             this code is jank for now but it WILL get better           |
     --------------------------------------------------------------------------
'''

def banana(b: int):
    return int(b+1)

# melhor usar classe
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toggle = False # controla se ta rodando a funcionalidade de audio
        # por causa de como o pyqt6 roda o exec(), não consigo fazer
        # com q cheque pelo teclado a cada iteração
        # SÓ se eu fizesse uma UI usando outro modulo
        # mas acho que não permitir edição enquanto tá rodando já contorna os problemas

        # configura icone & nome de janela
        self.setWindowIcon(QIcon(path.abspath("../icon.png"))) #placeholder
        self.setWindowTitle("clickclack")

        self.bandeja = QSystemTrayIcon()
        self.bandeja.setIcon(QIcon(path.abspath("../icon.png")))

        # inicializa botao
        self.botao = QPushButton("me clica rs")
        self.botao.setMaximumSize(QSize(100, 100))
        self.desativarbotao = None

        # inicializa outro botao
        self.esconder = QPushButton("esconder")
        self.esconder.setMaximumSize(QSize(100, 100))

        # botao de liga/desliga
        self.rodar = QPushButton("pra sair\né só fechar a janela")
        self.rodar.setMaximumSize(QSize(150, 100))

        # incializa slider
        vol = QSlider(Qt.Orientation.Horizontal)
        vol.setRange(0, 100)
        vol.setSliderPosition(100)

        #    # thread separada para processar o audio:
        #    self.ex = threading.Thread(None, audio.rodarForever, "tocarsom", audios, daemon=True) # threading usa uma LISTA de args
        #    self.ex.start() # só tem como sair dessa thread matando o processo inteiro (botão de X ou sla alt f4)
        #    # pqp sir chloe é mt bom
        #    # TODO deixar esse codigo mais organizadokkkkkkkkkkkkkkkkkkkk

        # arruma o layout
        layout = QVBoxLayout()
        botoescima = QHBoxLayout()
        botoescima.addWidget(self.botao)
        botoescima.addWidget(self.esconder)

        layout.addLayout(botoescima)
        layout.addWidget(self.desativarbotao)
        layout.addWidget(vol)
        layout.addWidget(self.rodar)

        dummy = QWidget()
        dummy.setLayout(layout)
        self.setCentralWidget(dummy)

        # conexoes de interaçao
        self.botao.clicked.connect(self.botaoapertado)
        vol.valueChanged.connect(self.setarVolume)

        self.esconder.clicked.connect(self.bandejaToggle)
        self.bandeja.activated.connect(self.bandejaToggle)


    def botaoapertado(self):
        self.botao.setText("obg \n(audio setado)")
        if len(audios) < 1:
            audios.append(audio.adcaudio())

        #inicializando thread aqui por motivos de gambiarra
        self.ex = threading.Thread(None, audio.rodarForever, "tocarsom", audios, daemon=True)
        self.ex.start()

    def setarVolume(self, v):
        if audios:
            volumeAtual(v/100, audios[0])
            print(v/100)

    def bandejaToggle(self):
        if self.isVisible():
            self.bandeja.setVisible(True)
            self.hide()
            
        else:
            self.show()
            self.bandeja.setVisible(False)
        

if "__main__" == __name__:
    print("hello world!")
    clickclack = QApplication(sys.argv)
    audios = []

    janela = UI()

    # showtime
    janela.show()
    
    #=== LOOP ===
    clickclack.exec()

    del janela, clickclack
    