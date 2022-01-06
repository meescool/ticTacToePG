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
subState = 0 # might need this
blinker = 0 # need this for blinking effect
timer = 10 # a counter for setting pauses in between button touches

mx = 0 # stores the mouse x position
my = 0 # stores the mouse y position

mx2 = 0
my2 = 0

skins = [a.img['o'],a.img['x']] # store the skins!

player={'skin':skins,'turn':True} # set the players skins and whether it's it's turn
# each index represents a spot on the board
# 0 = empty
# 1 = player
# 2 = cpu
plays = [1,0,1,0,1,1,2,1,2] 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            # when clicking on the intro screen
            if state == 0:
                state += 1
            # when clicking on the submenu in the game screen
            elif state == 2 and subState == 1:
                mx2,my2 = pygame.mouse.get_pos()
                subState = 2
            # when clicking on other screens
            elif state != 0:
                mx,my = pygame.mouse.get_pos()
                
    pygame.Surface.fill(scr,a.colors['indigo'])

    state, subState, timer = s.screens(state,scr,blinker,timer,mx,my,mx2,my2,player,plays,subState)
    if blinker == 100:
        blinker = 0
    blinker+=1
    # u.clock.tick()
    pygame.display.update()

