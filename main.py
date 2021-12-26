'''
@author Marcela Estrada
This game is tic tac toe
'''

import sys, pygame
import screens as s
import values as v

pygame.init()

scr = pygame.display.set_mode(v.size['scr'])

pygame.display.set_caption('Tic Tac Toe')

# clock function for timing
clock  = pygame.time.Clock()

time = 10

running = True
state = 0
while running:
    clock.tick(time)
    pygame.Surface.fill(scr,v.colors['indigo'])
    state = s.screens(state,scr)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()

