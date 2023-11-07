# Joystick Abfragen und Bilder

## Grafik darstellen

Um eine Grafik auf dem Display darzustellen musst du eine BMP Grafikdatei erstellen. Das kannst du am besten mit deinem Grafikeditor machen.
Du kannst die Grafik als bmp Datei abspeichern.
Wenn du die Grafik auf dem Display anzeigen will kannst du das so machen:

```
from lib.pbm import pbm
img = pbm('res/pong.pbm')
display.blit(startimg.getFb(), 20,5)
```

## Joystick

```
from lib.joystick import joystick
stick=joystick(Pin.cpu.A3, Pin.cpu.A4, Pin.cpu.A5)
```
