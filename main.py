'''
@author Marcela Estrada
This game is tic tac toe
'''

import sys, pygame
from pygame.constants import MOUSEBUTTONDOWN
import screens as s
import assets as a
import util as u

pygame.init()

scr = pygame.display.set_mode(a.sizes['scr'])

pygame.display.set_caption('Tic Tac Toe')

running = True
state = 0
while running:

    pygame.Surface.fill(scr,a.colors['indigo'])

    state = s.screens(state,scr)
    print(state , 'this is a state')
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if state == 0:
                state += 1

    pygame.display.update()

