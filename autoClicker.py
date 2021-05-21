import Graphic_app
from setup import *
from Graphic_app import *

def launch_autoclicker(master_menu):
    check = False
  
    while check==False:
        check,number=Menu_Graphic(master_menu)     
    auto_click(number,Graphic_app.X_pos,Graphic_app.Y_pos)

def launch_multiclicker(master_menu):
    check = False
  
    while check==False:
        check,number=Menu_Graphic_Multi(master_menu)     
    multi_click(number,Graphic_app.X_pos_arr,Graphic_app.Y_pos_arr)


#if __name__ == "__main__":
#   launch_autoclicker(master_menu)