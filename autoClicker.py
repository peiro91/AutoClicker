import Graphic_app
from setup import *
from Graphic_app import *

if __name__ == "__main__":
    check = False
  
    while check==False:
        check,number=Menu_Graphic()
    auto_click(number,Graphic_app.X_pos,Graphic_app.Y_pos)