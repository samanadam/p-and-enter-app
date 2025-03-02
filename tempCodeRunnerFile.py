import keyboard
import time
while not keyboard.is_pressed("q"):
    if keyboard.is_pressed("z"):
        keyboard.press_and_release("p")
        while keyboard.is_pressed('z'):  # Z tuşuna basılı tutmayı engellemek için 
            pass
        
    if keyboard.is_pressed("x"):
        keyboard.press_and_release("enter")
        while keyboard.is_pressed('x'):  # X tuşuna basılı tutmayı engellemek için 
            pass
