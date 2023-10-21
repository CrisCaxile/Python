#Desafio 21. Faça um programa em Python que abra e reproduza o
#áudio de um arquivo MP3

import pygame

pygame.mixer.init()
pygame.mixer.music.load("SnapInsta.io - ILLENIUM - Take You Down __ Good Things Fall Apart (Nurko & William Black Remix) (64 kbps).mp3")

while True:
    comando = input("\033[34mDigite 1 se quiser que a música pause, 2 para dar play e 3 para sair: ")
    if comando == "1":
        pygame.mixer.music.pause()
    elif comando == "2":
        pygame.mixer.music.play()
    elif comando == "3":
        pygame.mixer.music.stop()
        break