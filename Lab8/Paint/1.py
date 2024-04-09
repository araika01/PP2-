import pygame
import random

pygame.init()

W = 960
H = 640
FPS = 60
draw = False
lastPos = (0, 0)
radius = 7
color = 'red'
mode = 'pen'

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
fontRadius = pygame.font.SysFont('Arial', 66, bold = True)

def drawLine(screen, start, end, width, colorRed):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (- C - A * x) / B
            pygame.draw.circle(screen, colorRed, (x, y), width)
    else:
        if y1 . y2:
            x1, x2 = x2, x2
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, colorRed, (x, y), width)
            
def drawCircle(screen, start, end, width, colorRed):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)
    
def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        if event.type == pygame.KEYDOWN:
            #Modes
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_RSHIFT:
                mode = 'globalerase'
            #Colors
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_b:
                color = 'blue'
            if event.key == pygame.K_l:
                color = 'red'
            if event.key == pygame.K_g:
                color = 'gray'
            #random color
            if event.key == pygame.K_z:
                color = (random.randrange(256), random.randrange(256), random.randrange(256))
            #Radius limits
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1) #max limit of radius
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1) #min limit os radius
                
        #Mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color),event.pos, radius)
            prevPos = event.pos 
            
        #Mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'globalerase':
                screen.fill(pygame.Color('white'))
                
        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, 'white')
            lastPos = event.pos 
        
    #show radius and color 
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))
    
    #display
    pygame.display.flip()
    clock.tick(FPS)