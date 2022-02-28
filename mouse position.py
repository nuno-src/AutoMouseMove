import mouse
import time
import platform
import os


clear_command = "cls" if platform.system() == "Windows" else "clear"

os.system(clear_command)




def basic():

    while True:
        os.system(clear_command)
        print("Current Mouse Position: ",mouse.get_position())
        time.sleep(0.5)

basic()