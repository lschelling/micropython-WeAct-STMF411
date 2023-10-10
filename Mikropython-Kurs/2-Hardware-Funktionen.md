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
let.intensity()
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
