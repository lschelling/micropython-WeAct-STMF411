import machine
from machine import Pin, I2C
import pyb
from pyb import Timer

from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf

from ball import Ball

i2c = machine.I2C(1)
display = SSD1306_I2C(128,64, i2c)

ball=Ball(64,32,5)

def ontime():
    global ball
    ball.onTimer()
   
led=pyb.LED(1)

timer=Timer(1, freq=20)
timer.callback(lambda x: ontime())

while True:
    pyb.delay(100)
    display.fill(0)
    ball.draw(display)
    display.show()
