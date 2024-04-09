#Imports
import pygame
import sys
import random, time
from pygame.locals import*

#Initializing
pygame.init()

#Setting up FPS
FPS = 60
clock = pygame.time.Clock()

#Creating colors
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorGrey = (128, 128, 128)
colorRed = (255, 0, 0)

#Other Variables for use in the program
W = 400
H = 600
SPEED = 5
SCORE = 0
COINS = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBlack)

background = pygame.image.load(".\\resources\\AnimatedStreet.png")

#Create a white screen
screen = pygame.display.set_mode((W, H))
screen.fill(colorWhite)
pygame.display.set_caption("Game")

#Class for Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)
        
    def move(self):
        global SCORE, bonus, all_sprites
        self.rect.move_ip(0, SPEED)
        if(self.rect.bottom > H):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

#Class for coins
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('.\\resources\\coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, W - 40), 0)
    
    def contact(self):
        global COINS
        COINS += 1
        self.rect.top = 0
        self.rect.center = (random.randint(40, W - 40), 0)   
         
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)

#Class for Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < W:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Setting up Sprites     
P1 = Player()
E1 = Enemy() 
C1 = Coins()  

#Creating Sprite Croups
enemies = pygame.sprite.Group()
enemies.add(E1)
bonus = pygame.sprite.Group()
bonus.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)    

#Game Loop  
while True:
    #Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, colorBlack)
    screen.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, colorBlack)
    screen.blit(coins, (360, 10))
    
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        
        #take a coin
        if pygame.sprite.spritecollideany(P1, bonus):
            C1.contact()
            for entity in bonus:
                entity.kill()
            C1 = Coins()
            bonus.add(C1)
            all_sprites.add(C1)
    #To be run if collision between Player and  Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(".\\resources\\crash.wav").play()
        time.sleep(0.5)
        
        screen.fill(colorRed)
        screen.blit(game_over, (30, 250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    pygame.display.update()
    clock.tick(FPS)
    