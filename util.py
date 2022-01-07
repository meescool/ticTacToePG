#write text
import pygame
from pygame import color
import assets as a
import buttons as b

# clock function for timing
clock  = pygame.time.Clock()

time = 3

def write_text(surf,text,font,color,x,y):
    msg = font.render(text, True , color)
    w,h = get_size(msg)
    surf.blit(msg,(x-(w/2),y-(h/2)))


def get_size(thing):
    w = thing.get_width()
    h = thing.get_height()
    return w,h

def check_input(mx,my):
    print('check input')

def draw_grid(scr, plays,player):
    pygame.Surface.fill(scr,a.colors['indigo'])
    # a.img['grid'].set_alpha(0)
    w,h = get_size(a.img['grid'])
    # place the grid
    grid = scr.blit(a.img['grid'],((a.sizes['scr'][0] - w)/2,(a.sizes['scr'][0] - h)/2))
    x = (a.sizes['scr'][0] - w)/2
    y = ((a.sizes['scr'][0] - h)/2)+20

    i = 0
    for play in plays:
        # adjusting how to display figures
        if i%3 == 0 and i != 0:
            x = (a.sizes['scr'][0] - w)/2
            if i == 6:
                y += h/3-10
            else:
                y += h/3+20
        if play != 0:
            scr.blit(player['skin'][0],(x,y))
        x += w/3+20
        i+=1
        
        
def draw_menu_btn(scr):
    colors = [a.colors['white'],a.colors['black'],a.colors['black'],a.colors['white']]
    w = 100
    h = 60
    x = 20
    y = a.sizes['scr'][0] - (h + 20)
    text = 'menu'
    btn = b.Button(colors,x,y,w,h,text,0,[10,10,10,10])
    btn.draw(scr)
    btn.hover(scr,0)
    return btn


def draw_menu(scr,bl,coord):
    area = pygame.Rect(0,a.sizes['scr'][0]/2,(a.sizes['scr'][0]/3)*(2),a.sizes['scr'][0]/2)
    bg = pygame.draw.rect(scr,a.colors['white'],area,0,0,0,50,0,0)
    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = (bg.width - w)/2
    y = bg.height
  
    colors = [a.colors['white'],a.colors['black'],a.colors['pink'],a.colors['white']]
    
    restart = b.Button(colors,x,y,w,h,'restart',0,[0,30,30,0])
   
    help = b.Button(colors,x,restart.y+h,w,h,'help',0,[0,0,0,0])
   
    changeSkin = b.Button(colors,x,help.y+h,w,h,'change skin',0,[0,0,0,0])

    quit = b.Button(colors,x,changeSkin.y+h,w,h,'quit',0,[30,0,0,30])
    
    btns = [restart,changeSkin,help,quit]
    for btn in btns:
        btn.draw(scr)
        btn.hover(scr,bl)
    
    for btn in btns:
        if(btn.click(coord['mx2'],coord['my2']))==True:
            return btn.text
    return 1

def timer(timer):
    timer-=1
    return timer
