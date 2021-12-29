'''
@author Marcela Estrada
This game is tic tac toe
'''

import sys, pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
import screens as s
import assets as a
import util as u

pygame.init()

scr = pygame.display.set_mode(a.sizes['scr'])

pygame.display.set_caption('Tic Tac Toe')

running = True
state = 0
subState = 0
blinker = 0
mx = 0
my = 0
skins = [a.img['o'],a.img['x']]
player={'skin':skins,'turn':True}
plays = [1,0,1,0,1,1,2,1,2]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if state == 0:
                state += 1
            else:
                mx,my = pygame.mouse.get_pos()
    pygame.Surface.fill(scr,a.colors['indigo'])

    state = s.screens(state,scr,blinker,mx,my,player,plays,subState)
    if blinker == 100:
        blinker = 0
    blinker+=1
    pygame.display.update()

