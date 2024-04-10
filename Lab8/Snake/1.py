#Imports
import pygame
import time
import random

snake_speed = 10

#Screen size
W = 500
H = 500

#Create colors
colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

#Initializing pygame
pygame.init()

#Create window
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()

#defining snake default position
snake_pos = [105, 45]

#defining first 4 blocks of snake body
snake_body = [[105, 45], [90, 45], [75, 45], [60, 45]]

#fruit position
fruit_pos = [random.randrange(1, (W // 15)) * 15, random.randrange(1, (H // 15)) * 15]

fruit_spawn = True

#setting default snake direction towards
#right
direction = "RIGHT"
change_to = direction

#initial score
score = 0
global level
level = 1

#displaying score function
def show_score(choice, color, font, size):
    
    #create font object score_font
    score_font = pygame.font.SysFont(font, size)
    level_font = pygame.font.SysFont(font, size)
    
    #create the display surface object
    #score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    level_surface = level_font.render('Level : ' + str(level), True, color)
    
    #create a rectangular object for the text
    #surface object
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect()
    
    #displaying text
    screen.blit(score_surface, score_rect)
    screen.blit(level_surface, (level_rect[0], level_rect[1] + 20))
    
#game over function
def game_over():
    
    #creating font object my-font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    #creating a text surface on which text
    #will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, colorRED)
    game_over_surface2 = my_font.render('Your level is : ' + str(level), True, colorRED)
    
    #create a rectangular object for the text
    #surface object
    game_over_rect1 = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
    
    #setting position of the text
    game_over_rect1.midtop = (W / 2, H / 3.5)
    game_over_rect2.midtop = (W / 2, H / 4.7)
    
    #blit will draw the text on screen
    screen.blit(game_over_surface, game_over_rect1)
    screen.blit(game_over_surface2, game_over_rect2)
    pygame.display.flip()
    
    #after 2 seconds we will quit the program
    time.sleep(2)
    
    #deactivating pygame
    pygame.quit()
    
    #quit the program
    quit()
    
def level_up(score, speed):
    if(score % 50 == 0):
        global level
        level += 1
        speed += 20
        
#Main Function
while True:
    
    #handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    #if two keys pressed simultaneously
    #we do not want snake to move into two
    #direction simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    #moving the snake
    if direction == 'UP':
        snake_pos[1] -= 15
    if direction == 'DOWN':
        snake_pos[1] += 15
    if direction == 'LEFT':
        snake_pos[0] -= 15
    if direction == 'RIGHT':
        snake_pos[0] += 15
    
    #snake body growing mechanism
    #if fruits and snakes collide then scores
    #will be incremented by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        level_up(score, snake_speed)
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (W // 15)) * 15, random.randrange(1, (H // 15)) * 15]
    for block in snake_body[1:]:
        if fruit_pos[0] == block[0] and fruit_pos[1] == block[1]:
            fruit_pos = [random.randrange(1, (W // 15)) * 15, random.randrange(1, (H // 15)) * 15]
            
    fruit_spawn = True
    screen.fill(colorBLACK)
    
    for pos in snake_body:
        pygame.draw.rect(screen, colorGREEN, pygame.Rect(pos[0], pos[1], 15, 15))
        
    pygame.draw.rect(screen, colorWHITE, pygame.Rect(fruit_pos[0], fruit_pos[1], 15, 15))
    
    #game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > W - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > H - 10:
        game_over()
        
    #touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
            
    #displaying score continuously   
    show_score(1, colorWHITE, 'times new roman', 20)
    
    #refresh game screen
    pygame.display.update()
    
    #refresh rate
    clock.tick(snake_speed)