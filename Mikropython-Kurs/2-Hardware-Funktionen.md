# Hardware Funktionen

Jedes Prozessorboard wie dein WeAct Board hat bestimmte Funktionen welche von der Boardhardware zur Verfügung gestellt werden. So hat das WeAct Board zum Beistpiel eine LED (Lämpchen) einen Schalter oder auch Funktionen vom Prozessor wie die interne Uhr.

Mikropython hat darum eine Objekte welche all diese Funktionen abbildet.

- `pyb` Board Funktionen
- `machine` Funktionen vom Prozesor


## LED

Eine Light Emitting Diode (LED) ist ein Bauelement das wie ein Lämpchen funktioniert. Auf deinem Board ist eine blaue LED drauf. Es gibt die aber in verschiedenen farben, also auch rot, grün, gelb usw.

Du kannst die LED so ansteuern:

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
led.intensity()
```

## Schalter

Der Schalter auf deinem Board muss ich wahrscheinlich nicht erklären. Wenn du ihn drückst ist er 1=True wenn er nicht betätigt ist, ist er 0=False.


```
import pyb

sw=pyb.Switch()

if sw.value():
    print("Schalter gedrückt")
else:
    print("Schalter nicht gedrückt")

```
Etwas eleganter ist es, mit der callback Methode eine Funktion anzugeben welche aufgerufen wird wenn der Zustand des Schalters sich ändert.

In diesen Beispiel ändert sich die LED immer wenn du den Schalter betätigst. (drückst oder loslässt.)

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
## Pin

### Als Eingang

Soll ein Anschulss (Pin) vom Board abgefragt werden kann das mit der Pin Klasse gemacht werden.

Der Name des Eingangs ist auf dem Board aufgedruckt. Dort muss das Signal, zB Schalter angeschlossen werden

Im Beispiel fräst du den Eingang A2 vom Board ab. Mit mode=Pin.IN sagst du dem Prozessor dass der A2 als Eingang geschaltet wird, mit pull=Pin.PULL_UP dass er 
vom Prozessor auf 1 gesetzt wird. Wenn du den Eingang auf GND setzt wir der Wert von `pin.value()` 0 geben.

```
pin = Pin(Pin.cpu.A2,  mode=Pin.IN, pull=Pin.PULL_UP)
pin.value()
```
### Als Ausgang

Wenn du einen Ausgang setzen willst geht das fast genau gleich.

```
pin = Pin(Pin.cpu.A2,  mode=Pin.OUT)
pin.value(0)
```

### Als interrupt

Mit der `Pin.irq()` Finktion kannst du, wie beim Schalter oder Timer, eine lambda Funktion angeben welche aufgerufen wird wenn sich der Ausgang ändert.

Detail findes du [hier](https://docs.micropython.org/en/v1.9.3/wipy/library/machine.Pin.html).

### Timer

Der Prozessor hat eine Anzahl von sogenannten Timer eingebaut. Ein Timer ist ein Zähler welcher mit einer festen Frequenz zählt. Die Frequenz wird in Herz angegeben. Ein Herz (Hz) ist 1 mal pro Sekunde. 2 Herz sind 2 mal pro Selunde.

Der Timer kann sehr schnelle Frequenzen zählen. Bis einige millionen Herz. (das ist dan ein Megaherz (MHz))

Das folgende Beispiel zeigt einen Timer mit 5 Hz der 5 mal pro Sekunde die LED ändert.

```
from time import sleep
from pyb import Timer

led=pyb.LED(1)
timer=Timer(1, freq=5)
timer.callback(lambda t: led.toggle())

while True:
    sleep(1)

```
