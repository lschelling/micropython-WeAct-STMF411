import machine
from machine import Pin, I2C
import pyb
from pyb import Timer
import random
from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf

from pong import Ball
from pong import Paddle
from lib.pbm import pbm
i2c = machine.I2C(1)
display = SSD1306_I2C(128,64, i2c)
# 3 obieject erzeugen 
pinLeft = Pin(Pin.cpu.A2,  mode=Pin.IN, pull=Pin.PULL_UP)
pinRight= Pin(Pin.cpu.A1,  mode=Pin.IN, pull=Pin.PULL_UP)
img= pbm('res/pong.pbm')
explimg= pbm('res/expl.pbm')        

def ontime():
    global ball
    ball.onTimer()
    
led=pyb.LED(1)


while True:
    display.fill(0)
    display.text('click',64,18)
    display.text('right',64,28)
    display.text('to',64,38)
    display.text('Start',64,48)
    display.blit(img.getFb(),0,0)
    display.show()
    ball=Ball(random.randint(44,84),10,5)
    ball.draw(display)
    display.show()
    paddle=Paddle(50,128//2,25,10)
    while pinLeft.value()==1:
        pyb.delay(100)
    c=0
    while paddle.hit(ball.locx(),ball.locy()):
          c=c+1
          pyb.delay(20)
          ball.onTimer()
          if pinLeft.value()==0:
             paddle.moveLeft(2)
          if pinRight.value()==0:
             paddle.moveRight(2)
          display.fill(0)
          ball.draw(display)
          paddle.draw(display)
          if c%4==0:
              display.show()
              
    display.text("Gameover",30,5)
    display.blit(explimg.getFb(),ball.locx()-5,ball.locy()-10)
    display.show()
    pyb.delay(2000)
     