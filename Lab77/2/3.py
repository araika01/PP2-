import pygame

pygame.init()
pygame.mixer.init()

def play_a_different_song():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index
    
def play_previous_song():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index -1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index
    
def stop_music():
    pygame.mixer.music.stop()
    
def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

screen = pygame.display.set_mode((600, 600))
songs = ['a.mp3', 'b.mp3', 'c.mp3']
current_song_index = 0
currently_playing_song = songs[current_song_index]

done = False

class play(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("play.png")
        self.rect = self.image.get_rect()
        self.rect.center = ((300, 300), 0)
        
class next(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("next.png")
        self.rect = self.image.get_rect()
        self.rect.center = ((500, 300), 0)

class prev(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("prev.png")
        self.rect = self.image.get_rect()
        self.rect.center = ((200, 300), 0)
     
class stop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("stop.png")
        self.rect = self.image.get_rect()
        self.rect.center = ((400, 300), 0)
 
PL = play()
PR = prev()
ST = stop()
NX = next()

all_sprites = pygame.sprite.Group()
all_sprites.add(PL)
all_sprites.add(PR)
all_sprites.add(ST)
all_sprites.add(NX)       

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                
    screen.fill((255, 255, 255))
    pygame.display.flip()
