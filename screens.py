import sys, pygame
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
import assets as a
import util as u
import buttons as b
from pygame import rect

def screens(state,scr,fr,mx,my):
        if(state==0):
            start_screen(scr,fr)
            return state
        elif(state==1):
          
            option = main_menu_screen(scr,mx,my)
            if option == 'start' and state == 1:
                state = 2
            if option == 'skins':
                state = 3
            if option == 'help':
                state = 4
            if option == 'quit':
                sys.exit()
            return state
        else:
            print(state)
            return state

def start_screen(scr,fr):
    scr.blit(a.img['title'],(0,0)) 

    # surface,
    x= a.sizes['scr'][0]/2
    y= a.sizes['scr'][1] - 30
    text = 'click to continue'

    u.write_text(scr,text,a.fonts['sub'],a.colors['white'],x,y)

    return

def main_menu_screen(scr,mx,my):
    scr.blit(a.img['bg'],(0,0)) 

    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = a.sizes['scr'][0]/2 - ((a.sizes['scr'][0]/2 - 50)/2)
    y = (a.sizes['scr'][1]/2)- (h*4/2)
  
    colors = [a.colors['white'],a.colors['black'],a.colors['l-pink']]
    
    start = b.Button(colors,x,y,w,h,'start',0,[0,30,30,0])
   
    skins = b.Button(colors,x,y+h,w,h,'skins',0,[0,0,0,0])
   
    help = b.Button(colors,x,skins.y+h,w,h,'help',0,[0,0,0,0])

    quit = b.Button(colors,x,help.y+h,w,h,'quit',0,[30,0,0,30])
    
    btns = [start,skins,help,quit]
    for btn in btns:
        btn.draw(scr)
        btn.hover(scr)
    
    for btn in btns:
        if(btn.click(mx,my))==True:
            return btn.text
    return " "
                
            
        




    
