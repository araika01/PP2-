import pygame

pygame.init()
pygame.mixer.init()

def play_a_next_song():
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
player_icon = pygame.transform.scale(pygame.image.load("player.png"), (600, 600))
clock = pygame.time.Clock()
songs = ['a.mp3', 'b.mp3', 'c.mp3']
current_song_index = 0
currently_playing_song = songs[current_song_index]

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                play_pause_music()
            elif key[pygame.K_RIGHT]:
                play_a_next_song()
            elif key[pygame.K_LEFT]:
                play_previous_song()
            elif key[pygame.K_DOWN]:
                stop_music()
               
    screen.blit(player_icon, (0,0))    
    pygame.display.flip()
    clock.tick(60)
    