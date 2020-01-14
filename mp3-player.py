from tkinter import *
import pygame
from tkinter import filedialog
import os
from tkinter.ttk import *

root = Tk()

mainframe = Frame(root, width=500, height=200)
listframe = Frame(root, width=200, height=100)
sg_no = sg = 0
songs = []
nome = StringVar()
style = Style()
line = 0

state = 0         # Defines if the song the is playing(0) or paused(1)


dir = filedialog.askdirectory()
os.chdir(dir)
for i in os.listdir(dir):
    if i.endswith('.mp3'):
        songs.append(i)
print(songs)
pygame.mixer.init()
pygame.mixer.music.load(songs[sg_no])

style.configure('W.TButton', font=('calibri', 14, 'bold'))
style.configure('BM.TLabel', font=('calibri', 20, 'bold'))
root.geometry("700x100")
root.resizable(0, 0)


def load(sg):
    global sg_no
    sg_no = sg
    pygame.mixer.music.load(songs[sg])


def play_song():
    global state
    if state == 0:
        pygame.mixer.music.play()
        nome.set(songs[sg_no])
    else:
        pygame.mixer.music.unpause()
        state = 0


def stop_song():
    global state
    state = 1
    pygame.mixer.music.pause()


def next():
    global sg_no
    sg_no += 1
    pygame.mixer.music.load(songs[sg_no])
    play_song()


def previous():
    global sg_no
    sg_no -= 1
    pygame.mixer.music.load(songs[sg_no])
    play_song()


Label(mainframe, textvariable=nome, style='BM.TLabel').grid(row=0, columnspan=4, column=0, sticky=W+E+N+S)
Button(mainframe, text='>|', command=play_song, style='W.TButton').grid(row=1, column=3, padx=5, pady=5)
Button(mainframe, text='||', command=stop_song, style='W.TButton').grid(row=1, column=4)
Button(mainframe, text='>|', command=next, style='W.TButton').grid(row=1, column=2, padx=5)
Button(mainframe, text='|<', command=previous, style='W.TButton').grid(row=1, column=1)
for music in songs:
    Label(listframe, text=music).grid(row=line, column=0, sticky=W+E+N+S)
    Button(listframe, text='>', command=lambda btn=songs.index(music): load(btn)).grid(row=line, column=1, sticky=W+E+N+S)
    line += 1


mainframe.grid(row=0, column=0)
listframe.grid(row=0, column=1, columnspan=2, padx=20)


root.mainloop()
