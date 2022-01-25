import pyautogui
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
        print("Time:", time_formated)
        print("Current mouse position: ", mouse.get_position())
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(110)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(160)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(50)
        mouse.move(800, 617, absolute=True, duration=3)
        print("Position: ", mouse.get_position())
        time.sleep(160)
        print("\nCycle finished! Starting over...")
        #break

    print("AMM has stoped")





def basicBC():

    print("\nAMM is running...")

    while True:
        time.sleep(5)
        localtime = time.localtime()
        time_formated = time.strftime("%H:%M:%S", localtime)
        print("Time:", time_formated)
        print("Current mouse position: ", mouse.get_position())
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        mouse.click('right')
        print("Right Click")
        time.sleep(110)
        mouse.move(770, 680, absolute=True, duration=3)  # New Map
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(60)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(150)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(50)
        mouse.move(800, 617, absolute=True, duration=3)
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(60)
        mouse.move(770, 680, absolute=True, duration=3)  # New Map
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(160)
        print("\nCycle finished! Starting over...")
        #break

    print("AMM has stoped")





def ativar():

    # Ativar heros inativos
    time.sleep(5)
    pyautogui.click('/images/lista-heros.PNG')
    time.sleep(2)
    pyautogui.click('/images/lista2.PNG')
    time.sleep(2)
    pyautogui.click('/images/botao-all.PNG')
    time.sleep(2)
    pyautogui.click('/images/botao-all.PNG')
    time.sleep(2)
    pyautogui.click('/images/exit.PNG')
    time.sleep(2)
    pyautogui.click('/images/bcoin.PNG')
    time.sleep(10)




def basic2BC():

    print("\nAMM is running...")

    count = 0
    while True:
        time.sleep(5)
        localtime = time.localtime()
        time_formated = time.strftime("%H:%M:%S", localtime)
        print("Time:", time_formated)
        print("Current mouse position: ", mouse.get_position())
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        mouse.click('right')
        print("Right Click")
        time.sleep(110)
        mouse.move(770, 680, absolute=True, duration=3)  # New Map
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        mouse.move(1030,350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(160)
        pyautogui.click('/images/green.PNG')
        time.sleep(2)
        pyautogui.click('/images/tesouro.PNG')
        mouse.move(800,617, absolute=True, duration=3)
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(100)
        mouse.move(189, 967, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(80)
        mouse.move(770, 680, absolute=True, duration=3)  # New Map
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(60)
        # Ativar heros inativos
        if count == 14:
            ativar()
        elif count == 24:
            ativar()
        elif count == 36:
            ativar()
        else:
            pass

        time.sleep(60)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(60)
        mouse.move(1010, 390, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(60)
        mouse.move(800, 400, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        mouse.move(800, 617, absolute=True, duration=3)
        print("Position: ", mouse.get_position())
        time.sleep(160)
        print("\nCycle finished! Starting over...")
        count += 1
        print("Current count: ", count)
        #break

    print("AMM has stoped")



opc =""
while opc != "exit":

    print("1) - Simple Mouse Movvment V1")
    print("2) - AMM V1 Adapted for BombCrypto")
    print("3) - AMM V2 Adapted for BombCrypto(pyautogui)")


    opc = input("Choose an option: ")

    if opc == "1":
        print("Chosen: 1 - Simple Mouse Movvment V1")
        basic()
    elif opc == "2":
        print("Chosen: 1 - AMM V1 Adapted for BombCrypto")
        basicBC()
    elif opc == "3":
        print("Chosen: 2 - AMM V2 Adapted for BombCrypto(pyautogui)")
        basic2BC()
    elif opc == "exit":
        print("Turning off...")
    else:
        print("Invalid Option!")






