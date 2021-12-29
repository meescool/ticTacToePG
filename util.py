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


def get_size(thing):
    w = thing.get_width()
    h = thing.get_height()
    return w,h
def draw_grid(scr):
    # a.img['grid'].set_alpha(0)
    w,h = get_size(a.img['grid'])
    scr.blit(a.img['grid'],((a.sizes['scr'][0] - w)/2,(a.sizes['scr'][0] - h)/2))
    print('this is grid')
