import sys, pygame
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
import assets as a
import util as u
import buttons as b
from pygame import rect

def screens(state,scr,bl,mx,my,player,plays,subState):
    if(state==0):
        start_screen(scr,bl)
        return state
    elif(state==1):
        option=main_menu_screen(scr,mx,my,bl)
        if option == 'start' and state == 1:
            state = 2
        if option == 'skins':
            state = 3
        if option == 'help':
            state = 4
        if option == 'quit':
            sys.exit()
        return state
    elif(state==2):
        state, plays, player =game_screen(scr,player,plays,bl,mx,my,state,subState)
        return state
    else:
        return state

def start_screen(scr,bl):
    scr.blit(a.img['title'],(0,0)) 

    # surface,
    x= a.sizes['scr'][0]/2
    y= a.sizes['scr'][1] - 30
    text = 'click to continue'

    if bl >= 50:
        u.write_text(scr,text,a.fonts['sub'],a.colors['white'],x,y)
    

    return

def main_menu_screen(scr,mx,my,bl):
    scr.blit(a.img['bg'],(0,0)) 

    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = a.sizes['scr'][0]/2 - ((a.sizes['scr'][0]/2 - 50)/2)
    y = (a.sizes['scr'][1]/2)- (h*4/2)
  
    colors = [a.colors['white'],a.colors['black'],a.colors['white'],a.colors['pink']]
    
    start = b.Button(colors,x,y,w,h,'start',0,[0,30,30,0])
   
    skins = b.Button(colors,x,y+h,w,h,'skins',0,[0,0,0,0])
   
    help = b.Button(colors,x,skins.y+h,w,h,'help',0,[0,0,0,0])

    quit = b.Button(colors,x,help.y+h,w,h,'quit',0,[30,0,0,30])
    
    btns = [start,skins,help,quit]
    for btn in btns:
        btn.draw(scr)
        btn.hover(scr,bl)
    
    for btn in btns:
        if(btn.click(mx,my))==True:
            return btn.text
    return ""
def game_screen(scr,player,plays,bl,mx,my,state,subState):
    temp = ''
    u.draw_grid(scr,plays,player)
    menu_button = u.draw_menu_btn(scr)
    if menu_button.click(mx,my) == True:
        subState = 1
        temp = u.draw_menu(scr,bl,mx,my)
    else: subState = 0
    if temp == 'restart' and subState == 1:
        plays = [0,0,0,0,0,0,0,0,0]
        state = 2
    if temp == 'quit' and subState == 1:
        sys.exit()
    return state,plays,player
    # make a button and change the substate
    # u.draw_menu(scr,bl)

    return state

    
    # if grid == True:
    #     playerTurn()   
    #     cpuTurn()   
      
            
        




    
