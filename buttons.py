import pygame
import util as u
import assets as a

class Button():
    def __init__(self, colors, x,y,w,h,text,width,corners):
        self.colors= colors
        self.x=x
        self.y=y
        self.w =w
        self.h = h
        self.text = text
        self.box = pygame.Rect(self.x,self.y,self.w,self.h)
        self.width = width
        self.corners = corners

    def draw(self,scr):
        pygame.draw.rect(scr,self.colors[0],self.box,self.width,self.corners[0],self.corners[1],self.corners[2],self.corners[3])
        u.write_text(scr,self.text,a.fonts['btn'],self.colors[1],self.x+(self.w/2),self.y+(self.h/2))

    def hover(self,scr):
        x,y = pygame.mouse.get_pos()
        if x >= self.x and x <= self.x +self.w and y >= self.y and y <= self.y + self.h:
            pygame.draw.rect(scr,self.colors[2],self.box,self.width,self.corners[0],self.corners[1],self.corners[2],self.corners[3])
            u.write_text(scr,self.text,a.fonts['btn'],self.colors[1],self.x+(self.w/2),self.y+(self.h/2))

    def click(self,x,y): 
        if x >= self.x and x <= self.x +self.w and y >= self.y and y <= self.y + self.h: 
            return True    
    
    

   