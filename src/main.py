from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStatusBar
from PyQt6.QtGui import QIcon, QKeyEvent
import sys

import audio

def banana(b: int):
    return int(b+1)

# melhor usar classe
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # configura icone & nome de janela
        self.setWindowIcon(QIcon("icon.png")) #placeholder
        self.setWindowTitle("five night at fred")
        
        # inicializa botao
        self.botao = QPushButton("me clica rs")
        self.botao.setMaximumSize(QSize(100, 100))

        # arruma o layout
        self.setCentralWidget(self.botao)
        
        # conexoes de interaçao
        self.botao.clicked.connect(self.botaoapertado)     
        
        
    def botaoapertado(self):
        self.botao.setText("obg")

    # TODO: colocar isso pra rodar em um icone de bandeja, pra gui ser so pra configuraçoes
    def keyPressEvent(self, evento: QKeyEvent):
        if evento.key() == 90: #se a tecla apertava for z:
            print("z")
            self.surpresa = QStatusBar()
            self.setMenuWidget(self.surpresa)
                
        audio.adcaudio()
        
        
if "__main__" == __name__:
    print("hello world!")
    clickclack = QApplication(sys.argv)
    
    janela = UI()
    
    # showtime
    janela.show()
    
    #=== LOOP ===
    clickclack.exec()
    
    del janela, clickclack
    