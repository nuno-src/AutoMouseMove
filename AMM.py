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

    print("\nAMM está em execução...")

    while True:
        time.sleep(5)
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
        print("\n Ciclo concluido! A recomeçar...")
        #break

    print("AMM has stoped")





def basicBC():

    print("\nAMM está em execução...")

    while True:
        time.sleep(5)
        print("Current mouse position: ", mouse.get_position())
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        mouse.click('right')
        print("Right Click")
        time.sleep(110)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(160)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Position: ", mouse.get_position())
        time.sleep(50)
        mouse.move(800, 617, absolute=True, duration=3)
        print("Position: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(160)
        print("\n Ciclo concluido! A recomeçar...")
        #break

    print("AMM has stoped")




def basic2BC():

    print("\nAMM está em execução...")

    while True:
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Posição: 150:350")
        mouse.click('right')
        print("Right Click")
        time.sleep(110)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Posição: 1030:350")
        time.sleep(160)
        pyautogui.click(green.PNG)
        time.sleep(2)
        pyautogui.click(tesouro.PNG)
        mouse.move(800,617, absolute=True, duration=3)
        print("Posição: 800:617")
        mouse.click('left')
        print("Left Click")
        time.sleep(100)
        mouse.move(189, 967, absolute=True, duration=2)
        print("Posição: 189:967")
        time.sleep(80)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Posição: 1020:380")
        mouse.move(800, 617, absolute=True, duration=3)
        print("Posição: 800:617")
        time.sleep(160)
        print("\n Ciclo concluido! A recomeçar...")
        #break

    print("AMM has stoped")



opc =""
while opc != "exit":

    print("1) - V1")
    print("2) - V1 Adapted for BombCrypto")
    print("3) - V2 Adapted for BombCrypto(pyautogui)")


    opc = input("Insira uma opção: ")

    if opc == "1":
        print("Chosen: 1 - V1")
        basic()
    elif opc == "2":
        print("Chosen: 1 - V1 Adapted for BombCrypto")
        basicBC()
    elif opc == "3":
        print("Chosen: 2 - V2 Adapted for BombCrypto(pyautogui)")
        basic2BC()
    elif opc == "exit":
        print("A sair...")
    else:
        print("Opção inválida")






