#write text
import pygame
import assets as a

# clock function for timing
clock  = pygame.time.Clock()

time = 3

def write_text(surf,text,font,color,x,y):
    msg = font.render(text, True , color)
    w = msg.get_width()
    h = msg.get_height()
    surf.blit(msg,(x-(w/2),y-(h/2)))
