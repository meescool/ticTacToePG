#write text
import pygame
import assets as a

# clock function for timing
clock  = pygame.time.Clock()

time = 3

def write_text(surf,text,font,color,x,y):
    msg = font.render(text, True , color)
    surf.blit(msg,(x,y))

# def button(scr,color,w,h,x,y,text,font,color2):
#     box = pygame.Rect(x,y,w,h)
#     btn = pygame.draw.rect(scr,color,box, border_top_left_radius = 10)
#     write_text(scr,text,font,color2,x,y)