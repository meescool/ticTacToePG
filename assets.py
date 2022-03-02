import pygame

pygame.font.init()

colors={
    'indigo': [54,46,101],
    'pink': [255,115,115],
    'l-pink': [255,150,115],
    'white': [255,255,255],
    'black': [0,0,0]
}

sizes={
    'scr':[500,500]
}

fonts={
    'btn': pygame.font.SysFont('Corbel',30),
    'sub': pygame.font.SysFont('Corbel',30),
    'score': pygame.font.SysFont('Corbel',60),
    'text': pygame.font.SysFont('Corbel',25),

}

img={
    'title':pygame.image.load('images/title.png'),
    'bg':pygame.image.load('images/bg.png'),
    'grid':pygame.image.load('images/grid.png'),
    'o':pygame.image.load('images/o.png'),
    'x':pygame.image.load('images/x.png')

}

# buttons = {
#     screen,color_light,[width/2,height/2,140,40]
# }
