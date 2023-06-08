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

class MyDisplay():

    def __init__(self):
        self.disp =  Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

        self.width = self.disp.width
        self.height = self.disp.height
        self.flagStop = True
        print(f"SUCCESS : init Oled, height = {self.height}, width = {self.width}")

    def clear(self):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
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

    def drawSentense(self,sentense):
        image = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

        font = ImageFont.load_default()
        draw.text((2, 7), sentense,  font=font, fill=255)

        self.disp.image(image)
        self.disp.display()

    def drawTime(self):
        while self.flagStop:
            image = Image.new('1', (self.width,self.height))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0,0,self.width,8), outline=0, fill=0)

            font = ImageFont.load_default()
            # draw.text((4, 0), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  font=font, fill=255)
            # make it center
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

    def run(self):
        threading.Thread(target=self.drawTime).start()

    def stop(self):
        self.flagStop = False