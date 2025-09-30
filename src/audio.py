import pygame
import time
pygame.mixer.init()

print(pygame.mixer.get_init())

def adcaudio():
    som = pygame.mixer.Sound("media/click3.mp3")
    som.play()
    print(pygame.mixer.get_busy())
    
    return som
    
def tocaraudio(som: pygame.mixer.Sound):
    som.play()
    print(som.get_volume())
