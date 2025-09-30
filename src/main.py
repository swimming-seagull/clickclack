from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QStatusBar, QSystemTrayIcon, QMenu,
                             QWidget, QHBoxLayout)
from PyQt6.QtGui import QIcon, QKeyEvent, QAction
import sys

import audio

def banana(b: int):
    return int(b+1)

# janela principal
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
        layout = QHBoxLayout()
        layout.addWidget(self.botao)
        layout.addWidget(QPushButton("dummy"))
        
        self.setLayout(layout)
        
        # conexoes de interaçao
        self.botao.clicked.connect(self.botaoapertado)     
        
    def botaoapertado(self):
        self.botao.setText("obg")

    def keyPressEvent(self, evento: QKeyEvent):
        audio.adcaudio()
        if evento.key() == 90: #se a tecla apertava for z:
            print("z")
            self.surpresa = QStatusBar()
            self.setMenuWidget(self.surpresa)


if "__main__" == __name__:
    clickclack = QApplication(sys.argv)
    clickclack.setQuitOnLastWindowClosed(False)
    
    
    # icone de bandeja pra rodar no fundo
    bandeja = QSystemTrayIcon()
    bandeja.setIcon(QIcon("icon.png"))
    bandeja.setVisible(True)

    menu = QMenu()
    bandeja.setContextMenu(menu)
    #bandeja.activated(menu.)
    # TODO: acertar o menu pra so dawr 1 clique pra abrir
    menuconfig = QAction("Abrir configurações...")
    menu.addAction(menuconfig)
    
    menusair = QAction("sair")
    menu.addAction(menusair)
    
    
    # showtime
    janela = UI()
    janela.show()
    menuconfig.triggered.connect(janela.show)
    menusair.triggered.connect(clickclack.quit)
    
    #=== LOOP ===
    clickclack.exec()
    
    
    del janela, clickclack
    