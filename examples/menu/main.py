import machine
from machine import Pin, I2C
import pyb
from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf
from lib.umenu import *


i2c = machine.I2C(1)
display = SSD1306_I2C(128,64, i2c)

pinLeft = Pin(Pin.cpu.A2,  mode=Pin.IN, pull=Pin.PULL_UP)
pinRight= Pin(Pin.cpu.A1,  mode=Pin.IN, pull=Pin.PULL_UP)
pinClick= Pin(Pin.cpu.A0,  mode=Pin.IN, pull=Pin.PULL_UP)


menu = Menu(display, 4, 12)
menu.set_screen(MenuScreen('Main Menu')
                .add(SubMenuItem('Settings')
                     .add(SubMenuItem('Date')
                          .add(ValueItem('Year', 2023, 2023,2050, 1, print))
                          .add(ValueItem('Month', 10, 1, 12, 1, print))
                          .add(ValueItem('Day', 10, 1, 31, 1, print)))
                     .add(SubMenuItem('Time')
                          .add(ValueItem('Hour', 1, 1, 60, 1, print))
                          .add(ValueItem('Minute', 1, 1, 60, 1, print))))
                .add(SubMenuItem('Games')
                     .add(EnumItem("Play", ['Pong', 'Snake'], print, 0))))


while True:
    menu.draw()
    if pinLeft.value()==0:
        menu.move(-1)
    if pinRight.value()==0:
        menu.move(1)
    if pinClick.value()==0:
        menu.click()
    display.show()
    pyb.delay(100)
