import pygame
import RPi.GPIO as GPIO
import time
import threading

motor_a_in1_pin = 26
motor_a_in2_pin = 19
motor_b_in1_pin = 13
motor_b_in2_pin = 6

GPIO.setwarnings(False)  # 模块内置功能，一般要加上
GPIO.setmode(GPIO.BCM)  # 设置GPIO引脚为BCM编码模式
GPIO.setup(motor_a_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_a_in2_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_b_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_b_in2_pin, GPIO.OUT)  # 设置该端口为输出模式


class controller:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.forward=0
        self.back=0
        self.lr=0
        self.flag = True

    def run(self):
        threading.Thread(target=self.Motor).start()
        threading.Thread(target=self.control).start()

    def control(self):
        num_joysticks = pygame.joystick.get_count()
        if num_joysticks > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            while self.flag:

                for event in pygame.event.get():

                    if event.type == pygame.JOYAXISMOTION:
                        axis = event.axis
                        value = event.value
                        if(axis==5):
                            if(value!=self.forward):
                                self.forward=value
                                # print(f"Joystick left motion on joystick : {value}")

                        elif(axis==2):
                            if(value!=self.back):
                                self.back=value
                                # print(f"Joystick right motion on joystick : {value}")
                            
                        elif(axis==0):
                            if(value!=self.lr):
                                self.lr=value
                                # print(f"Joystick right motion on joystick : {value}")
                                
                    # elif event.type == pygame.JOYBUTTONDOWN:
                    #     self.flag = False
                    #     exit(0)
            
        pygame.joystick.quit()
        pygame.quit()

    def Motor(self):
        while self.flag:
            time.sleep(0.1)
            if(self.lr>0.5):
                GPIO.output(motor_a_in1_pin, GPIO.HIGH)
                GPIO.output(motor_a_in2_pin, GPIO.LOW)
                GPIO.output(motor_b_in1_pin, GPIO.LOW)
                GPIO.output(motor_b_in2_pin, GPIO.HIGH)
            elif(self.lr<-0.5):
                GPIO.output(motor_a_in1_pin, GPIO.LOW)
                GPIO.output(motor_a_in2_pin, GPIO.HIGH)
                GPIO.output(motor_b_in1_pin, GPIO.HIGH)
                GPIO.output(motor_b_in2_pin, GPIO.LOW)
            elif(self.forward>0.5):
                GPIO.output(motor_a_in1_pin, GPIO.HIGH)
                GPIO.output(motor_a_in2_pin, GPIO.LOW)
                GPIO.output(motor_b_in1_pin, GPIO.HIGH)
                GPIO.output(motor_b_in2_pin, GPIO.LOW)
            elif(self.back>0.5):
                GPIO.output(motor_a_in1_pin, GPIO.LOW)
                GPIO.output(motor_a_in2_pin, GPIO.HIGH)
                GPIO.output(motor_b_in1_pin, GPIO.LOW)
                GPIO.output(motor_b_in2_pin, GPIO.HIGH)
            else:
                GPIO.output(motor_a_in1_pin, GPIO.LOW)
                GPIO.output(motor_a_in2_pin, GPIO.LOW)
                GPIO.output(motor_b_in1_pin, GPIO.LOW)
                GPIO.output(motor_b_in2_pin, GPIO.LOW)
    
    def stop(self):
        self.flag = False
        pygame.joystick.quit()
        pygame.quit()
                
# if __name__ == "__main__":
#     c=controller()
#     c.run()