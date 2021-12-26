import sys, pygame
from pygame import rect
title = pygame.image.load('images/title.png')

def screens(state,scr):
        if(state==0):
            start_screen(scr)
            return 0
        else:
            print('no state')

def start_screen(scr):
    scr.blit(title,(0,0))
    # start_button = pygame.draw.rect(scr,white,)
    
