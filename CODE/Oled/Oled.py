import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import os
import threading
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

LEFT = 0
RIGHT = 1
FORWARD = 2
BACK = 3
WAIT = 4

class MyDisplay():

    def __init__(self):
        self.disp =  Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

        self.width = self.disp.width
        self.height = self.disp.height
        self.flagStop = True
        self.sentence = "Hello World!"

        self.direction = 0
        print(f"SUCCESS : init Oled, height = {self.height}, width = {self.width}")

    def clear(self):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,-2,self.width,self.height), outline=0, fill=0)
        self.disp.image(image)
        self.disp.display()

    def drawShapes(self):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

        padding = 2
        shape_width = 20
        top = padding
        bottom = self.height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = padding
        # Draw an ellipse.
        draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=100)
        x += shape_width+padding
        # Draw a rectangle.
        draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
        x += shape_width+padding
        # Draw a triangle.
        draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
        x += shape_width+padding
        # Draw an X.
        draw.line((x, bottom, x+shape_width, top), fill=255)
        draw.line((x, top, x+shape_width, bottom), fill=255)
        x += shape_width+padding

        font = ImageFont.load_default()
        
        draw.text((x, top),    'Hello',  font=font, fill=255)
        draw.text((x, top+20), 'World!', font=font, fill=255)

        self.disp.image(image)
        self.disp.display()

    def drawSentense(self,sentence):
        self.sentence = sentence

    def drawTime(self):
        while self.flagStop:
            image = Image.new('1', (self.width,self.height))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0,0,self.width,8), outline=0, fill=0)

            font = ImageFont.load_default()
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            draw.text(((self.width-6*len(nowtime))/2, -2), nowtime,  font=font, fill=255)
            
            self.disp.image(image)
            self.disp.display()
            time.sleep(.1)

    def drawFull(self):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((-2,-2,self.width,self.height), outline=0, fill=255)

        self.disp.image(image)
        self.disp.display()

    def draw(self):
        while self.flagStop:
            image = Image.new('1', (self.width,self.height))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0,0,self.width,8), outline=0, fill=0)

            font = ImageFont.load_default()
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            draw.text(((self.width-6*len(nowtime))/2, -2), nowtime,  font=font, fill=255)



            # print(self.direction)
            if(self.direction == LEFT):
                start=(0, self.height/2+4)
                end=( self.width, self.height/2+4)
                draw.line((start,end[0]-10,end[1]),width=7, fill=255)

                draw.polygon((end[0]-15,end[1]-10,end[0]-15,end[1]+10,end[0],end[1]), fill=255)
            elif(self.direction == RIGHT):
                start=(0, self.height/2+4)
                end=( self.width, self.height/2+4)
                draw.line((start[0]+10,start[1],end),width=7, fill=255)

                draw.polygon((start[0]+15,start[1]-10,start[0]+15,start[1]+10,start[0],start[1]), fill=255)

            elif(self.direction == FORWARD):
                start=(self.width/2, 8)
                end=( self.width/2, self.height)
                draw.line((start[0],start[1]+10,end),width=7, fill=255)

                draw.polygon((start[0]-10,start[1]+15,start[0]+10,start[1]+15,start[0],start[1]), fill=255)

            elif(self.direction == BACK):
                start=(self.width/2, 8)
                end=( self.width/2, self.height)
                draw.line((start,end[0],end[1]-10),width=7, fill=255)

                draw.polygon((end[0]-10,end[1]-15,end[0]+10,end[1]-15,end[0],end[1]), fill=255)
            elif(self.direction == WAIT):
                draw.text((20, 7), "Wang Xu Gang",  font=font, fill=255)
                draw.text((20, 17), "Wei Yang Jing",  font=font, fill=255)

            self.disp.image(image)
            self.disp.display()
            time.sleep(.01)

    def run(self):
        threading.Thread(target=self.draw).start()
        
    def setDirection(self,direction):
        # print(f"SUCCESS : set direction from{self.direction} to {direction}")
        self.direction = direction

    def stop(self):
        self.flagStop = False