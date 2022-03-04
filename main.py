'''
@author Marcela Estrada
This game is tic tac toe with a GUI
'''

import sys, pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
import screens as s
import assets as a
import util as u

pygame.init()

scr = pygame.display.set_mode(a.sizes['scr'])

pygame.display.set_caption('Tic Tac Toe')

myIcon= a.img['grid']
pygame.display.set_icon(myIcon)

running = True


state = 0
subState = 0 # might need this
blinker = 0 # need this for blinking effect
timer = 10 # a counter for setting pauses in between button touches

coord ={
    'mx':0,
    'my':0,
    'mx2':0,
    'my2':0
}
mx = 0 # stores the mouse x position
my = 0 # stores the mouse y position

mx2 = 0
my2 = 0

skins = [a.img['o'],a.img['x']] # store the skins!

player={'skin':skins,'turn':True, 'status':0} # set the players skins and whether it's it's turn
# each index represents a spot on the board
# 0 = empty
# 1 = player
# 2 = cpu
plays = [0,0,0,0,0,0,0,0,0] 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            # when clicking on the intro screen
            if state == 0:
                state += 1
            # when clicking on the submenu in the game screen
            elif state == 2 and subState == 1:
                coord['mx2'],coord['my2'] = pygame.mouse.get_pos()
                subState = -1
            # when clicking on other screens
            elif state != 0:
                coord['mx'],coord['my']= pygame.mouse.get_pos()
                
    pygame.Surface.fill(scr,a.colors['indigo'])

    state, subState, timer, player, plays,coord = s.screens(state,scr,blinker,timer,coord,player,plays,subState)
    if blinker == 100:
        blinker = 0
    blinker+=1
    # u.clock.tick()
    pygame.display.update()

