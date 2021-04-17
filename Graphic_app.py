import tkinter as tk
from setup import *

def check_save(window,click_number_str):#It checks fields correctly populated in menu and return True or False
    #initializa variables
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
    
def Menu_Graphic():

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
    window=tk.Tk()
    window.geometry("600x100")
    window.title("autoGUI")
    window.configure(background="white")

    #initialize variables
    X_pos=""
    Y_pos=""
    check_clicks=""
    check=False
    click_number_str="0"
    color_check="red"

    #define window components
    #Button Ok
    ok_button=tk.Button(text="OK",state=DISABLED, command= lambda: check_save(window,click_number_str.get()))
    ok_button.grid(row=0,column=0)
    ok_button.config(height = 1, width = 10)
    
    #Button Set
    set_button=tk.Button(text="Click Set", command=initialize_setup)
    set_button.grid(row=0,column=1)
    set_button.config(height = 1, width = 10)
    
    #If number entered is not between 0 and 1000, it shows message
    text_check_click = tk.Label(window,background="white",text=check_clicks,fg=color_check, font=("Helvetica",16))
    text_check_click.grid(row=1,column=2)
    
    #User enters number of click he wants to perfom
    click_number_str = tk.Entry(background="grey")
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
  
    tk.mainloop() #avvio del menu

    return check,click_number
