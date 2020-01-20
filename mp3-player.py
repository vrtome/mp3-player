from tkinter import *
import pygame
from tkinter import filedialog
import os
from tkinter.ttk import *

root = Tk()
root.geometry("705x100")
root.resizable(0, 0)
canvas = Canvas(root, width=180, height=100, scrollregion=(0, 0, 150, 150))
mainframe = Frame(root, width=500, height=100)
listframe = Frame(canvas)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)


sg_no = sg = 0
songs = []
nome = StringVar()
style = Style()
line = 0

state = 0        


dir = filedialog.askdirectory()
os.chdir(dir)
for i in os.listdir(dir):
    if i.endswith('.mp3'):
        songs.append(i)
print(songs)
pygame.mixer.init()
pygame.mixer.music.load(songs[sg_no])

style.configure('W.TButton', font=('calibri', 14, 'bold'))
style.configure('BM.TLabel', font=('calibri', 15, 'bold'))


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


Label(mainframe, textvariable=nome, style='BM.TLabel', width=25).grid(row=0, columnspan=4, column=0, sticky=W+E+N+S)
Button(mainframe, text='>', command=play_song, style='W.TButton').grid(row=1, column=3, padx=5, pady=5)
Button(mainframe, text='||', command=stop_song, style='W.TButton').grid(row=1, column=4)
Button(mainframe, text='>|', command=next, style='W.TButton').grid(row=1, column=2, padx=5)
Button(mainframe, text='|<', command=previous, style='W.TButton').grid(row=1, column=1)
for music in songs:
    Label(listframe, text=music, width=16).grid(row=line, column=1)
    Button(listframe, text='>', command=lambda btn=songs.index(music): load(btn)).grid(row=line, column=2)
    line += 1

if line > 3:
    canvas.configure(scrollregion=(0, 0, (line*30), (line*30)))
scrollbar.grid(row=0, column=3, rowspan=3, ipady=25)
canvas.create_window(0, 0, anchor=NW,  window=listframe)
mainframe.grid(row=0, column=0)

canvas.grid(row=0, column=2)

#listframe.grid(row=0, column=2, columnspan=3)

root.mainloop()
