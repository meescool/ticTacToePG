import sys, pygame
import assets as a
import util as u
import buttons as b
from pygame import rect

def screens(state,scr):
        if(state==0):
            start_screen(scr)
            return state
        elif(state==1):
            main_menu_screen(scr)
            return state
        else:
            print('no state')
            return state

def start_screen(scr):
    scr.blit(a.img['title'],(0,0)) 

    # surface,
    w = a.sizes['scr'][0]/3+50
    h = a.sizes['scr'][1]/3+50
    x= w/2+50
    y= h/2+50
    text = 'click to continue'

    u.write_text(scr,text,a.fonts['sub'],a.colors['white'],x,y)

    u.clock.tick(1) 

    return
    # btn_txt = 'click to continue'
    # colors = [a.colors['pink'],a.colors['white'],a.colors['l-pink']]
    # btn = b.Button(colors,x,y,w,h,btn_txt)
   
    #btn.draw(scr)

def main_menu_screen(scr):
    print('main menu')

    
