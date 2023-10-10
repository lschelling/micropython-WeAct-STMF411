from time import sleep
from pyb import Timer
Time=0

def ontime():
    global Time
    Time= Time+4**2
   
led=pyb.LED(1)
timer=Timer(1, freq=1.5)
timer.callback(lambda x: ontime())

while True:
    sleep(1)
    print(Time)