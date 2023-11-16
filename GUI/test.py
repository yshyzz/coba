import tkinter as tk
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('musik/rasakan.mp3')  # Ganti 'musik.mp3' dengan nama file musik kamu
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Pemutar Musik")

play_button = tk.Button(root, text="Putar Musik", command=play_music)
play_button.pack()

stop_button = tk.Button(root, text="Stop Musik", command=stop_music)
stop_button.pack()

root.mainloop()
