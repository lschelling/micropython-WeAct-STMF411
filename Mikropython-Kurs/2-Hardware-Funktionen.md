# Hardware Funktionen

Jedes Prozessorboard wie dein WeAct Board hat bestimmte Funktionen welche von der Boardhardware zur Verfügung gestellt werden. So hat das WeAct Board zum Beistpiel eine LED (Lämpchen) einen Schalter oder auch Funktionen vom Prozessor wie die interne Uhr.

Mikropython hat darum eine Objekte welche all diese Funktionen abbildet.

- `pyb` Board Funktionen
- `machine` Funktionen vom Prozesor


## LED


```
import pyb
led = pyb.LED(1)

# schaltet LED ein
led.on()

# schaltet LED off
led.off())

# wechselt LED status 
led.toggle()

# setzt die Helligkeit (0 schwarz, 255=maximale Helligkeit)
let.intensity()
```

## Schalter

```
import pyb

sw=pyb.Switch()

if sw.value():
    print("Schalter gedrückt")
else:
    print("Schalter nicht gedrückt")

```

Oder etwas eleganter mit einer Funktion welche aufgerufen wird wenn sich der Schalter ändert:

```
import pyb
from time import sleep
from pyb import Timer

led=pyb.LED(1)
sw=pyb.Switch()
sw.callback(lambda:led.toggle())

while True:
    sleep(1)
```

### Timer


```
from time import sleep
from pyb import Timer

led=pyb.LED(1)
timer=Timer(1, freq=5)
timer.callback(lambda t: led.toggle())

while True:
    sleep(1)

```

