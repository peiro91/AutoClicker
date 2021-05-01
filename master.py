import autoClicker
from autoClicker import *
import tkinter as tk

def Menu():
    
#define window properties
    menu=tk.Tk()
    menu.geometry("600x600")
    menu.title("Automatic Tools")
    menu.configure(background="white")

#Button Set autoclicker launch
    auto_click_button=tk.Button(text="One Spot\n Clicker", command= lambda: launch_autoclicker(menu))
    auto_click_button.grid(row=0,column=0)
    auto_click_button.config(height = 5, width = 10)
    tk.mainloop()

if __name__ == "__main__":
    Menu()