import keyboard
import time
#with q you can exit
while not keyboard.is_pressed("q"):
    if keyboard.is_pressed("z"):
        keyboard.press_and_release("p")
        # it prevent holding p
        while keyboard.is_pressed('z'):  
            pass
        
    if keyboard.is_pressed("x"):
        keyboard.press_and_release("enter")
         # it prevent holding enter
        while keyboard.is_pressed('x'): 
            pass
