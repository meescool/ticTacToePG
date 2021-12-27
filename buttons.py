import pygame
import util as u
import assets as a

class Button():
    def __init__(self, colors, x,y,w,h,text):
        print("button")
        self.colors= colors
        self.x=x
        self.y=y
        self.w =w
        self.h = h
        self.text = text

    def draw(self,scr):
        box = pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(scr,self.colors[0],box)
        u.write_text(scr,self.text,a.fonts['btn'],self.colors[1],self.x,self.y)
    
    

   