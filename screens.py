import sys, pygame
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
import assets as a
import util as u
import buttons as b
from pygame import rect

def screens(state,scr,bl,timer,coord,player,plays,subState):
    '''
    ' This function has a switch that returns all the possible screens
    ' state - the state to keep track of what screen was last on
    ' scr - the window
    ' bl - this keeps count for when to blink
    ' timer - keeping track of time
    ' coord - coordinates of the mouse click
    ' player - player information 
    ' plays - keeps track of board
    ' substate - used for the state any menu in a screen is in
    '''
    if(state==0):
        start_screen(scr,bl)
        return state, 0, timer, player, plays, coord
    elif(state==1):
        option=main_menu_screen(scr,coord['mx'],coord['my'],bl)
        if option == 'start' and state == 1:
            state = 2
        if option == 'skins':
            state = 3
        if option == 'help':
            state = 4
        if option == 'quit':
            sys.exit()
        return state, 0, timer, player, plays,coord
    elif(state==2):
        state, subState, timer, player, plays, coord =game_screen(scr,player,plays,bl,timer,coord,state,subState)
        return state, subState, timer, player, plays, coord
    else:
        return state, 0, timer, player, plays, coord

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


def game_screen(scr,player,plays,bl,timer,coord,state,subState):
    '''
    ' This function sets up the game screem.
    ' It first draws the grid, using the plays and player 
    ' to decide what to draw.
    ' Then it also draws a menu button. There is a checker to
    ' see if the menu button is being clicked.
    '''
    # stores the menu selection 
    temp = ''
    u.draw_grid(scr,plays,player)
    menu_button = u.draw_menu_btn(scr)
    
    if menu_button.click(coord['mx'],coord['my']) == True:
        temp = u.draw_menu(scr,bl,coord)
        coord['mx2'] =0
        if subState != 2:
            subState = 1
    print(temp)
    print(subState)
    if temp == 'restart':
        plays = [0,0,0,0,0,0,0,0,0]
        state = 2
        subState = 0
        coord['mx'] = 0
        coord['my'] = 0
        temp = ''
        return state, subState, timer, player, plays,coord

        
    if temp == 'quit' and subState == 2:
        sys.exit()
    # if 
    if temp == '':
        x,y = u.get_size(a.img['grid'])
        if x > coord['mx']:
            plays, player = u.play_grid(plays, player, coord['mx'], coord['my'])
            print('clicked on grid')
    return state, subState, timer, player, plays, coord
    # make a button and change the substate
    # u.draw_menu(scr,bl)


    
    # if grid == True:
    #     playerTurn()   
    #     cpuTurn()   
      
            
        




    
