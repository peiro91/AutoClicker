import tkinter as tk
import master
from pynput.keyboard import Listener as KeyboardListener
from setup import *

def check_save(window,click_number_str):#It checks fields correctly populated in menu and return True or False
    #initializes variables
    global check_clicks
    global click_number
    global check
    global text_check_click
    check_clicks="OK"
    
    try:
        click_number=int(click_number_str)
        if click_number<1 or click_number>1000:
            check_clicks="Enter a number between 0 and 1000"
            text_check_click.config(text=check_clicks)
            return check,click_number,check_clicks
        else:
            click_number=int(click_number_str)
            check=True
            window.quit()
            window.destroy()
            return check,click_number,check_clicks
    except:
        check_clicks="Enter a number between 0 and 1000"
        click_number=0
        text_check_click.config(text=check_clicks)
        return check,click_number,check_clicks

def initialize_setup(): #user is asked to set a position he wants to perform clicks 
    global X_pos
    global Y_pos
    
    pyautogui.alert('Press Ok and click the point you want to click')
    window.iconify() #minimize window
    with Listener(on_click=is_clicked) as listener: #using listener to wait mouse click
        listener.join()
    X_pos,Y_pos=pyautogui.position() #when moouse is clicked, position is saved
    ok_button['state'] = 'normal'#enablig ok button
    X_label.config(text="X position: "+str(X_pos))
    Y_label.config(text="Y position: "+str(Y_pos))
    window.deiconify() #de-minimize window

def initialize_setup_multi(): #user is asked to set a position he wants to perform clicks 
    global X_pos
    global Y_pos
    global X_pos_arr
    global Y_pos_arr
    X_pos_arr=[]
    Y_pos_arr=[]
    pyautogui.alert('Press Ok and click the point you want to click')
    window.iconify() #minimize window
    #it registers 3 clickes
    for count in range(3):
        with Listener(on_click=is_clicked) as listener: #using listener to wait mouse click
            listener.join()
            X_pos,Y_pos=pyautogui.position() #when mouse is clicked, position is saved
            X_pos_arr.append(X_pos)
            Y_pos_arr.append(Y_pos)

    ok_button['state'] = 'normal'#enablig ok button
    X_label.config(text="X position: "+str(X_pos_arr[0]))
    Y_label.config(text="Y position: "+str(Y_pos_arr[0]))
    window.deiconify() #de-minimize window

def disable_event():
    window.destroy()
    master.enablebutton()
    
def Menu_Graphic(master_menu):


    #define global variables
    global X_pos
    global Y_pos
    global X_pos_arr
    global Y_pos_arr
    global check_clicks
    global click_number
    global check
    global text_check_click
    global ok_button
    global X_label
    global Y_label
    global window
    
    #define window properties
    window=tk.Toplevel(master_menu)
    window.geometry("600x100")
    window.title("autoGUI")
    window.configure(background="white")

    #initialize variables
    X_pos=""
    Y_pos=""
    X_pos_arr=[]
    Y_pos_arr=[]
    check_clicks=""
    check=False
    click_number_str="0"
    click_number=0
    color_check="red"

    #define window components
    #Button Ok
    ok_button=tk.Button(window,text="OK",state=DISABLED, command= lambda: check_save(window,click_number_str.get()))
    ok_button.grid(row=0,column=0)
    ok_button.config(height = 1, width = 10)

    #Button Set
    set_button=tk.Button(window,text="Click Set", command=initialize_setup)
    set_button.grid(row=0,column=1)
    set_button.config(height = 1, width = 10)

    #If number entered is not between 0 and 1000, it shows message
    text_check_click = tk.Label(window,background="white",text=check_clicks,fg=color_check, font=("Helvetica",16))
    text_check_click.grid(row=1,column=2)

    #User enters number of click he wants to perfom
    click_number_str = tk.Entry(window,background="grey")
    click_number_str.grid(row=1,column=1)

    #Label 
    text_label_click = tk.Label(window,background="white",text="Number Of Clicks:  ")
    text_label_click.grid(row=1,column=0)

    #X label
    X_label = tk.Label(window,background="white",text="X position: ")
    X_label.grid(row=2,column=0)

    #Y label
    Y_label = tk.Label(window,background="white",text="Y position: ")
    Y_label.grid(row=2,column=1)
    window.wm_protocol("WM_DELETE_WINDOW", lambda: disable_event())
    window.mainloop() #avvio del menu

    return check,click_number

def Menu_Graphic_Multi(master_menu):


    #define global variables
    global X_pos
    global Y_pos
    global check_clicks
    global click_number
    global check
    global text_check_click
    global ok_button
    global X_label
    global Y_label
    global window
    
    #define window properties
    window=tk.Toplevel(master_menu)
    window.geometry("600x100")
    window.title("autoGUI")
    window.configure(background="white")

    #initialize variables
    X_pos=""
    Y_pos=""
    check_clicks=""
    check=False
    click_number_str="0"
    click_number=0
    color_check="red"

    #define window components
    #Button Ok
    ok_button=tk.Button(window,text="OK",state=DISABLED, command= lambda: check_save(window,click_number_str.get()))
    ok_button.grid(row=0,column=0)
    ok_button.config(height = 1, width = 10)

    #Button Set
    set_button=tk.Button(window,text="Click Set", command=initialize_setup_multi)
    set_button.grid(row=0,column=1)
    set_button.config(height = 1, width = 10)

    #If number entered is not between 0 and 1000, it shows message
    text_check_click = tk.Label(window,background="white",text=check_clicks,fg=color_check, font=("Helvetica",16))
    text_check_click.grid(row=1,column=2)

    #User enters number of click he wants to perfom
    click_number_str = tk.Entry(window,background="grey")
    click_number_str.grid(row=1,column=1)

    #Label 
    text_label_click = tk.Label(window,background="white",text="Number Of Clicks:  ")
    text_label_click.grid(row=1,column=0)

    #X label
    X_label = tk.Label(window,background="white",text="X position: ")
    X_label.grid(row=2,column=0)

    #Y label
    Y_label = tk.Label(window,background="white",text="Y position: ")
    Y_label.grid(row=2,column=1)
    window.wm_protocol("WM_DELETE_WINDOW", lambda: disable_event())
    window.mainloop() #avvio del menu

    return check,click_number






