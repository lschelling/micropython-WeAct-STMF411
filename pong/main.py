import machine
from machine import Pin, I2C
import pyb
from pyb import Timer

from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf

from pong import Ball
from pong import Paddle

i2c = machine.I2C(1)
display = SSD1306_I2C(128,64, i2c)
# 2 obieject erzeugen 
ball=Ball(64,32,5)
paddle=Paddle(55,128//2,25,10)
pinLeft = Pin(Pin.cpu.A2,  mode=Pin.IN, pull=Pin.PULL_UP)
pinRight= Pin(Pin.cpu.A1,  mode=Pin.IN, pull=Pin.PULL_UP)

        

def ontime():
    global ball
    ball.onTimer()
    
led=pyb.LED(1)

timer=Timer(1, freq=20)
timer.callback(lambda x: ontime())

while True:
    pyb.delay