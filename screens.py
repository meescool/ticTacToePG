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
            coord['mx'] = 0 
            coord['my'] = 0
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
    elif(state==3):
        option = skins_screen(scr, plays, player, coord['mx'], coord['my'], bl)
        if(option == 'return'):
            coord['mx'] = 0
            coord['my'] = 0
            state = 1
        return state, subState, timer, player, plays, coord
    elif(state==4):
        option = help_screen(scr, plays, player, coord['mx'], coord['my'], bl)
        if(option == 'return'):
            coord['mx'] = 0
            coord['my'] = 0
            state = 1
        return state, subState, timer, player, plays, coord
    elif(state==5):
        # get the option to start a new game or return to main menu
        option = score_screen(scr, plays, player, coord['mx'], coord['my'], bl)
        if option == 'new game':
            # need to reset the coordinates and set the state to 2
            coord['mx'] = 0
            coord['my'] = 0
            state = 2
        if option == 'main menu':
            # reseting coordinates so that it doesn't go to another screen
            coord['mx'] = 0
            coord['my'] = 0
            state = 1
        return state, subState, timer, player, plays, coord
        # score_screen(scr, plays, player, coord['mx'], coord['my'], bl)
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


def skins_screen(scr, plays, player, mx, my, bl):
    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = a.sizes['scr'][0]/2 - ((a.sizes['scr'][0]/2 - 50)/2)
    y = (a.sizes['scr'][1])- (h)

    colors = [a.colors['white'],a.colors['black'],a.colors['white'],a.colors['pink']]
    
    goBack = b.Button(colors,x,y,w,h,'return',0,[0,30,30,0])
   
    # surface,
    x= a.sizes['scr'][0]/2
    y= a.sizes['scr'][1] - 30

    text = "this is the screen for choosing skins"

    u.write_text(scr,text,a.fonts['text'],a.colors['white'],x,h)

    btn = goBack
    
    goBack.draw(scr)
    goBack.hover(scr,bl)
    if(goBack.click(mx,my))==True:
            return btn.text
    return ""


def help_screen(scr, plays, player, mx, my, bl):
    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = a.sizes['scr'][0]/2 - ((a.sizes['scr'][0]/2 - 50)/2)
    y = (a.sizes['scr'][1]) - (h)

    colors = [a.colors['white'],a.colors['black'],a.colors['white'],a.colors['pink']]
    
    goBack = b.Button(colors,x,y,w,h,'return',0,[0,30,30,0])
   
    # surface,
    x= a.sizes['scr'][0]/2
    y= a.sizes['scr'][1] - 30

    text = "these are instructions"

    u.write_text(scr,text,a.fonts['text'],a.colors['white'],x,h)

    btn = goBack
    
    goBack.draw(scr)
    goBack.hover(scr,bl)
    if(goBack.click(mx,my))==True:
            return btn.text
    return ""


def score_screen(scr, plays, player, mx, my, bl):
    w = a.sizes['scr'][0]/2 - 50
    h = 60
    x = a.sizes['scr'][0]/2 - ((a.sizes['scr'][0]/2 - 50)/2)
    y = (a.sizes['scr'][1]/2)- (h/2)

    colors = [a.colors['white'],a.colors['black'],a.colors['white'],a.colors['pink']]
    
    newgame = b.Button(colors,x,y,w,h,'new game',0,[0,30,30,0])
   
    mainMenu = b.Button(colors,x,y+h,w,h,'main menu',0,[30,0,0,30])

    # surface,
    x= a.sizes['scr'][0]/2
    y= a.sizes['scr'][1] - 30
    if(player['status'] == 0):
        text = 'It\'s a draw!'
    if(player['status'] == 1):
        text = 'You won!'
    if(player['status'] == 2):
        text = 'You lost!'


    if bl >= 3:
        u.write_text(scr,text,a.fonts['score'],a.colors['white'],x,h)

    btns = [newgame, mainMenu]
    # print(bl)
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
        if subState != -1:
            subState = 1
    # print(temp)
    # print(subState)
    if temp == 'restart':
        plays = [0,0,0,0,0,0,0,0,0]
        state = 2
        subState = 0
        coord['mx'] = 0
        coord['my'] = 0
        temp = ''
        return state, subState, timer, player, plays,coord

        
    if temp == 'quit' and subState == -1:
        sys.exit()

    # if(u.check_winner(plays, 1)== True):
    #     player['turn'] = True
    #     player['status'] = 1
    #     plays = [0,0,0,0,0,0,0,0,0]
    #     state = 5

    # if(u.check_winner(plays, 2)== True):
    #     player['turn'] = False
    #     player['status'] = 2
    #     plays = [0,0,0,0,0,0,0,0,0]
    #     state = 5

    # playsSet = set(plays)
    # if 0 not in playsSet:
    #     player['turn'] = True
    #     player['status'] = 0
    #     plays = [0,0,0,0,0,0,0,0,0]
    #     state = 5

    if temp == '':
        w,h = u.get_size(a.img['grid'])
        padx = (a.sizes['scr'][0] - w)/2
        pady = (a.sizes['scr'][0] - h)/2
        # print(coord['my'] , " is < ", h + pady)
        # player checks that mouse coordinates are in the grid, taking into account the padding of the window
        if (coord['mx'] > padx and coord['mx'] < w+padx) and (coord['my'] > pady and coord['my'] < h + pady):
            plays, player, coord['mx'], coord['my'], state, timer = u.play_grid(plays, player, coord['mx'], coord['my'], state, timer)
        # cpu checks that if it's cpu turn
        elif (player['turn'] == False and (coord['mx'] == 0 and coord['my'] == 0)):
            plays, player, coord['mx'], coord['my'], state, timer = u.play_grid(plays, player, coord['mx'], coord['my'], state, timer)

        return state, subState, timer, player, plays, coord
    return state, subState, timer, player, plays, coord
    # make a button and change the substate
    # u.draw_menu(scr,bl)


    
    # if grid == True:
    #     playerTurn()   
    #     cpuTurn()   
      
            
        




    
