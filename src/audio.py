import pygame
#import time
import os.path as path
from keyboard import read_event

#from PyQt6.QtCore import QObject, QThread # HEHE
pygame.mixer.init()
import threading

print(pygame.mixer.get_init())
# esse arquivo parece inutil agora,
# mas com mais audios isso vai funcionar pra encapsulamento

def adcaudio(caminho = "../media/wilhelmscream.mp3"):
    som = pygame.mixer.Sound(path.abspath(caminho))
    som.play()
    print(pygame.mixer.get_busy())
    
    return som
    
def tocaraudio(som: pygame.mixer.Sound):
    som.play()
    print(som.get_volume())

def volumeAtual(v: int, som: pygame.mixer.Sound):
    som.set_volume(v)


def rodarForever(som: pygame.mixer.Sound):
    while True:
        if read_event().event_type == 'down':
            tocaraudio(som)

        jaexiste=False
        for a in threading.enumerate():
            if a.name == "tocarsom":
                if jaexiste: break 
                else: jaexiste=True 


'''TODO: queria fazer isso sem depender do modulo de keyboard, porem isso significaria
fazer codigo especifico pra cada sistema operacional
até tenho alguma ideia de como usar hooks de windows, mas de resto?
nem ideia mermao'''