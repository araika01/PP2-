import pygame 
import datetime 

pygame.init()
screen = pygame.display.set_mode((800, 800))
window_title = pygame.display.set_caption("mickey mouse clock")
clock = pygame.time.Clock()

# loading the images 
bg_surf = pygame.image.load("mainclock.png")
leftarm = pygame.image.load("leftarm.png")
rightarm = pygame.image.load("rightarm.png")
bg_rect = bg_surf.get_rect(center = (400, 400))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = datetime.datetime.now()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6) - 200

    rotated_leftarm = pygame.transform.rotate(leftarm, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(rightarm, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = bg_rect.center)
    rightarm_rect = rotated_rightarm.get_rect(center = bg_rect.center)

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pygame.display.flip()
    clock.tick(60)