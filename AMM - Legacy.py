import mouse
import time


print("""

    _    __  __ __  __ 
   / \  |  \/  |  \/  |
  / _ \ | |\/| | |\/| |
 / ___ \| |  | | |  | |
/_/   \_\_|  |_|_|  |_|

""")
print("Auto Mouse Move")






def basic():

    print("\nAMM is running...")

    while True:
        time.sleep(5)
        localtime = time.localtime()
        time_formated = time.strftime("%H:%M:%S", localtime)
        print(time_formated)
        print("Posição do rato atual: ",mouse.get_position())
        time.sleep(30)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Posição: ",mouse.get_position())
        mouse.click('right')
        print("Right Click")
        time.sleep(110)
        mouse.move(1030, 350, absolute=True, duration=2)
        print("Posição: ",mouse.get_position())
        time.sleep(140)
        mouse.move(100, 400, absolute=True, duration=2)
        print("Posição: ",mouse.get_position())
        time.sleep(145)
        mouse.move(800, 617, absolute=True, duration=3)
        print("Posição: ",mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(100)
        mouse.move(220, 600, absolute=True, duration=2)
        print("Posição: ",mouse.get_position())
        time.sleep(20)
        mouse.move(345, 222, absolute=True, duration=2) 
        print("Posição: ", mouse.get_position()) # Back
        mouse.click('left')
        print("Left Click")
        time.sleep(2)
        mouse.move(778, 483, absolute=True, duration=2) # come back
        print("Posição: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(80)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Posição: ",mouse.get_position())
        time.sleep(80)
        mouse.move(770, 680, absolute=True, duration=3) # New Map
        print("Posição: ",mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(120)
        print("\nCycle finished! Starting over...")
        #break

    print("AMM has stoped")

basic()






