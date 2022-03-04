#write text
import random
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

def get_skin(index):
    options = [a.img['o'],a.img['x']]
    if(index % 2 == 0):
        skins = [options[index], options[index+1]]
    else:
        skins = [options[index], options[index-1]]
    return skins

def check_winner(plays, sym):
    '''
    ' This function checks for the winner. I decided to use a hashing algorithm to check for the winners
    ' Basically it goes through the list of plots on the grid and checks if there is a 1 or 2, depending
    ' on where the function was called, and adds one to a list that keeps track of the rows and columns
    ' kind of like in a matrix.
    ' !! important !! currently does not check for diagonals
    '''
    row = [0,0,0]
    col = [0,0,0]
    dia = [0,0]
    i = 0
    j = 0
    k = 0
    # sort out each of the plays into it's respective row, column or diagonal
    for play in plays:
        # print(play)
        if(play == sym):
            col[i] += 1
            row[j] += 1
            if(k%4 == 0):
                dia[0]+=1
                print('left diagonal \\')
            if(k%2 == 0 and k >= 2 and k <=6 ):
                dia[1]+=1
                print('right diagonal /')

        i+=1
        if(i == 3):
            j+=1
            i=0
        k+=1

    # check if any of the rows, columns or diagonals has 3 in a row
    if ((row[0] == 3 or row[1] == 3 or row[2] == 3) or (col[0] == 3 or col[1] == 3 or col[2] == 3) or dia[0] == 3 or dia[1] == 3):
        return True

    return False


def get_rand(limit):
    rand = random.randrange(0,limit)
    return rand

def play_grid(plays, player, mx, my, state, time):
    # print('put play on game')
    '''
    ' if player = true
    ' check where the user clicks
    ' check if the box is free
    ' update the plays list
    ' set player to false
    ' if false, use timer to simulate the computer thinking
    ' once timer is reached then place the play of the computer 
    ' set player to true
    '''
    w,h = get_size(a.img['grid'])
    padx = (a.sizes['scr'][0] - w)/2
    pady = (a.sizes['scr'][0] - h)/2
    x = w/3
    y = h/3
    i = 0
    j = 0
    k = 0
    if(player['turn'] == True):
        for play in plays:
            if(player['turn'] == True):                            
                if ((mx > (x*i) + padx and mx < ((x * i) + x) + padx) and (my > (y*j) + pady and my < ((y * j) + y) + pady) and play == 0):
                    # print("This is the value of col 1 ", (y*j) + pady)
                    # print("This is the value of end col 1  ", ((y * j) + y) + pady)
                    # print("This is the value of my mouse y ", my)
                    # print('player played their turn on spot ', k)
                    plays[k] = 1
                    player['turn'] = False
                    mx = 0
                    my = 0
            i+=1    
            if(i == 3):
                i = 0
                j += 1             
            k+=1
                    # need to check where the user clicked and then reset the mx and my coordinates
        # need to check if there is a winner
        if(check_winner(plays, 1)== True):
            player['turn'] = True
            player['status'] = 1
            plays = [0,0,0,0,0,0,0,0,0]
            state = 5
            return plays, player, mx, my, state, time
    else:
        time+=1
        if(time >= 300):
            play = get_rand(8)
            limiter = 0
            while(True):
                # print("CPU turn to play is playing spot ", play)
                if(plays[play] == 0):
                    mx = 0
                    my = 0
                    time = 0
                    plays[play] = 2
                    player['turn'] = True
                    break
                else:
                    play = get_rand(9)
                if (limiter == 9):
                    break
                limiter+=1

            if(check_winner(plays, 2)== True):
                player['turn'] = False
                player['status'] = 2
                plays = [0,0,0,0,0,0,0,0,0]
                state = 5
                return plays, player, mx, my, state, time

            playsSet = set(plays)
            if 0 not in playsSet:
                player['turn'] = True
                player['status'] = 0
                plays = [0,0,0,0,0,0,0,0,0]
                state = 5
                return plays, player, mx, my, state, time

        
        #player['turn'] = True
        # need to add a random function for choosing the pc move
        # need to add a timing function to simulate time
        # need to check if there is a winner
    return plays, player, mx, my, state, time


def draw_grid(scr, plays,player):
    '''
    ' This function is for drawing the grid and for placing the marks 
    '''
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
        if play == 1:
            scr.blit(player['skin'][0],(x,y))
        if play == 2:
            scr.blit(player['skin'][1],(x,y))
        x += w/3+20
        i+=1
        
       
def draw_menu_btn(scr):
    '''
    function for drawing the button
    ''' 
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
    '''
    ' Function for drawing the main menu
    '''
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
