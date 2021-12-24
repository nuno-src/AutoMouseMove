#import sched
#import schedule
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
        time.sleep(40)
        mouse.move(150, 350, absolute=True, duration=2)
        print("Posição: 150:350")
        time.sleep(110)
        mouse.move(1030,350, absolute=True, duration=2)
        print("Posição: 1030:350")
        time.sleep(160)
        mouse.move(100,400, absolute=True, duration=2)
        print("Posição: 100:400")
        time.sleep(145)
        mouse.move(800,617, absolute=True, duration=3)
        print("Posição: 800:617")
        time.sleep(100)
        mouse.move(189, 967, absolute=True, duration=2)
        print("Posição: 189:967")
        time.sleep(80)
        mouse.move(1020, 380, absolute=True, duration=2)
        print("Posição: 1020:380")
        mouse.move(800, 617, absolute=True, duration=3)
        print("Posição: 800:617")
        time.sleep(180)
        #break

    print("AMM has stoped")

basic()


# def move_mouse():
#     mouse.move(1030, 350, absolute=True, duration=2)
#
# sched.scheduler()
# sched.scheduler.
# scheduler
#
# schedule.every(15).minutes.do(move_mouse)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)





