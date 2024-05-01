from tkinter import*
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("700x500")

pygame.mixer.init()
pygame.init()

menubar = Menu(root)
root.config(menu = menubar)

  
def next():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index
    
def prev():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index -1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index
    
def stop():
    pygame.mixer.music.stop()
    
def play():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

songs = ['a.mp3', 'b.mp3', 'c.mp3']
current_song_index = 0
currently_playing_song = songs[current_song_index]    

songlist = Listbox(root, bg = "Black", fg = "white", width = 150, height = 20)
songlist.pack()

play = PhotoImage(file = 'play.png')
next = PhotoImage(file = 'next.png')
prev = PhotoImage(file = 'prev.png')
stop = PhotoImage(file = 'stop.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image = play, borderwidth = 0, command = play())
next_btn = Button(control_frame, image = next, borderwidth = 0, command = next())
prev_btn = Button(control_frame, image = prev, borderwidth = 0, command = prev())
stop_btn = Button(control_frame, image = stop, borderwidth = 0, command = stop())

play_btn.grid(row = 0, column = 2, padx = 7, pady = 10)
next_btn.grid(row = 0, column = 3, padx = 7, pady = 10)
prev_btn.grid(row = 0, column = 0, padx = 7, pady = 10)
stop_btn.grid(row = 0, column = 1, padx = 7, pady = 10)

root.mainloop()
