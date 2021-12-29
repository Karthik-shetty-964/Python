from pygame import mixer
from datetime import datetime
import time

# import pygame
# print(pygame.__version__)
def reminderOn(stoper):
    mixer.init()
    mixer.music.load("reminder.ogg")
    mixer.music.play()
    while True:
        a=input()
        if a==stoper:
            mixer.music.stop()
            break


# reminderOn("done")

if __name__ == '__main__':
    with open('HealthRecord.txt','a') as f:
        f.write(f"\n\t\t\t-----Record of------[{time.asctime(time.localtime(time.time()))}]\n\n")
    initWater = time.time()
    initeyes = time.time()
    initphy = time.time()
    # waterBreak = 10
    # eyeBreak = 20
    # phyBreak = 30
    while True:
          if time.time()-initWater>=10:
             print("Its Water time!!! Press 'done' to stop reminder")
             reminderOn("done")
             with open('HealthRecord.txt', 'a') as f:
                 f.write(f"Took a Water break at [{datetime.now()}]\n")
             initWater=time.time()
             # break

          if time.time()-initeyes>=20:
             print("Its Eye break time!!! Press 'done' to stop reminder")
             reminderOn("done")
             with open('HealthRecord.txt', 'a') as f:
                 f.write(f"Took a Eye break at [{datetime.now()}]\n")
             initeyes=time.time()


          if time.time()-initphy>=30:
             print("Its physical break time!!! Press 'done' to stop reminder")
             reminderOn("done")
             with open('HealthRecord.txt', 'a') as f:
                 f.write(f"Took a physical break at [{datetime.now()}]\n")
             initphy=time.time()
