import machine
from machine import Pin, I2C
import pyb
from pyb import Timer
import random

from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf

from pong import Ball
from pong import Paddle

i2c = machine.I2C(1)
display = SSD1306_I2C(128,64, i2c)
# 2 obieject erzeugen 
ball=Ball(random.randint(10,118),10,5)
paddle=Paddle(55,128//2,25,10)
pinLeft = Pin(Pin.cpu.A2,  mode=Pin.IN, pull=Pin.PULL_UP)
pinRight= Pin(Pin.cpu.A1,  mode=Pin.IN, pull=Pin.PULL_UP)
       

def ontime():
    global ball
    ball.onTimer()
    
led=pyb.LED(1)

timer=Timer(1, freq=20)
timer.callback(lambda x: ontime())

while paddle.hit(ball.getXPos(), ball.getYPos()):
    pyb.delay(100)
    display.fill(0)
    ball.draw(display)
    if pinLeft.value()==0:
        paddle.moveLeft(5)
    if pinRight.value()==0:
        paddle.moveRight(5)
    paddle.draw(display)
    display.show()


display.text("Failed",50,32)
display.show()
pyb.delay(100)
