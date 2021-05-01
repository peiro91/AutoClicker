import autoClicker
from autoClicker import *
import tkinter as tk


def autoclick():
    auto_click_button.configure(state=tk.DISABLED)
    launch_autoclicker(menu)
    auto_click_button.configure(state="normal")
   # menu.quit()

def Menu():
    global menu
    global auto_click_button

#define window properties
    menu=tk.Tk()
    menu.geometry("600x600")
    menu.title("Automatic Tools")
    menu.configure(background="white")

#Button Set autoclicker launch
    auto_click_button=tk.Button(text="One Spot\n Clicker", command=autoclick)
    auto_click_button.grid(row=0,column=0)
    auto_click_button.config(height = 5, width = 10)
    tk.mainloop()
def enablebutton():
    #here I need to re-activate button but I don't know how to do.
    pass

if __name__ == "__main__":
    Menu()




