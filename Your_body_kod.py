# -*- coding: utf-8 -*-
import pygame
import sys
import pickle
from pygame.locals import *
pygame.init()
# okna i funkcje
def start():
    okno.blit(okno_start, (0,0))

#główny program

with open("savegame", "rb") as f:
    save = pickle.load(f)
main = foo[0]
strona = foo[1]
okno_start = pygame.image.load('main.png')
okno_start = pygame.transform.scale(okno_start, main)
okno = pygame.display.set_mode(main, DOUBLEBUF)
pygame.display.set_caption('Your body')
fps = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save = [main,strona]
            with open("savegame", "wb") as f:
                pickle.dump(save, f)
            pygame.quit()
            sys.exit()
    fps.tick(60)
    start()
    pygame.display.update()

