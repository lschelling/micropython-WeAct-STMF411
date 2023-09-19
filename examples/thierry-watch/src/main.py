# Setup - run once


import machine
from machine import Pin, I2C
from time import sleep # Get the sleep library from the time module.
import utime as time
import pyb

from lib.ssd1306 import SSD1306_I2C
import lib.framebuf2 as framebuf

tim = pyb.Timer( 4, prescaler=47, period=999 ) # TIM4

pwm = tim.channel(4, pyb.Timer.PWM,
         pin=pyb.Pin.board.PB9, pulse_width=0)
print( 'PWM period   :', tim.period() )
print( 'PWM frequency:', tim.freq()   )

i2c = machine.I2C(1)
i2c.scan()


display = SSD1306_I2C(128,64, i2c)

display.text('Hello, World!', 0, 0, 1)
display.show()


# The line below indicates we are configuring this as an output (not input)
#led = machine.Pin(BUILT_IN_LED_PIN, machine.Pin.OUT)
rtc = machine.RTC()
rtc.datetime((2020, 1, 21, 2, 10, 32, 36, 0))
count = 0
# Main loop: Repeat the forever...
while True:
    (year, month, day, weekday, hour, minute, second, ms) = rtc.datetime();
    count = count + 1
    display.fill(0)
    display.text(str(year) + ' ' + str(month) + '.' + str(day), 0, 0, 1)
    display.large_text(str(hour) + ':' + str(minute) + ':' + str(second), 0, 30,2, 1)
    display.show()
    print(rtc.datetime())
    print('hello')
    #led.high() # turn on the LED
    #sleep(0.5) # leave it on for 1/2 second
    #led.low()  # Turn off the LED
    sleep(1) # leave it off for 1/2 second
