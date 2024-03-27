import pygame

radius, step = 25, 20
x, y = 50, 50

done = False


pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= step
    if pressed[pygame.K_DOWN]:
        y += step
    if pressed[pygame.K_LEFT]:
        x -= step
    if pressed[pygame.K_RIGHT]:
        x += step
    
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('red'), (x, y), radius)
    
    if x < 15:
        x += step
    elif x > 600 - 10:
        x -= step
    elif y < 15:
        y += step
    elif y > 600 - 10:
        y -= step
    
    pygame.display.flip()
    clock.tick(60)
        