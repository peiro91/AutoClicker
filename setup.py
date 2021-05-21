from tkinter import *
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
import pyautogui,time

def is_clicked(x, y, button, pressed):
    if pressed:
        return False # to stop the thread after click

def auto_click(click_number,X,Y):   #perform clicks base on initialize_setup return.
    for click in range(click_number):
        pyautogui.click(x=X, y=Y, interval=0.1)
    pyautogui.alert('autoGUI finished')

def multi_click(click_number,X=[],Y=[]):   #perform clicks base on initialize_setup return.
    for click in range(click_number):
        for i in range(len(X)):
            pyautogui.click(x=X[i], y=Y[i], interval=0.1)
    pyautogui.alert('autoGUI finished')