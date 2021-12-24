import mouse
import time

print("""

    _    __  __ __  __ 
   / \  |  \/  |  \/  |
  / _ \ | |\/| | |\/| |
 / ___ \| |  | | |  | |
/_/   \_\_|  |_|_|  |_|

""")
print("Auto Mouse Move (Adapted for Bomb Crypto)")

def basicBC():

    print("\nAMM está em execução...")

    while True:
        time.sleep(5)
        print("Posição atual do rato: ", mouse.get_position())
        time.sleep(10)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Posição: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(110)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Posição: ", mouse.get_position())
        time.sleep(160)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Posição: ", mouse.get_position())
        time.sleep(50)
        mouse.move(800, 617, absolute=True, duration=3)
        print("Posição: ", mouse.get_position())
        mouse.click('left')
        print("Left Click")
        time.sleep(160)
        print("\n Ciclo concluido! A recomeçar...")
        #break

    print("AMM has stoped")
    
    
basicBC()