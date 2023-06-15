from Oled import Oled
from Controller import controller
from Oled import animation
import os
import time
import threading

class control:

    def __init__(self):
        os.system("clear")
        # self.animation = animation.Start()
        self.oled = Oled.MyDisplay()
        self.controller = controller.controller()
        self.controller.run()
        self.flag = True

        threading.Thread(target=self.set).start()
        self.run()
        pass

    def run(self):
        while True:
            print(">>> ",end="")
            i=input()
            if(i=="clear"):
                self.oled.clear()
            elif(i=="draw"):
                self.oled.drawFull()
            elif(i.split(" ")[0]=="draw"):
                self.oled.drawSentense(i[5:])
            elif(i=="start"):
                # self.animation.stop()
                self.oled.run()
            elif(i=="exit"):
                # self.animation.stop()
                self.oled.stop()
                self.controller.stop()
                self.flag = False
                self.oled.clear()
                os.system("clear")
                break
            elif(i=="stop"):
                self.oled.stop()
                self.oled.clear()
            os.system("clear")

    def set(self):
        while self.flag:
            time.sleep(.01)
            self.oled.setDirection(self.controller.getDirection())

