# Micropython

## REPL
Python erlaubt, dass du Code direkt in der Shell (Ein-/Ausgabefenster) eingeben und testen könnt. Das nennt sich `REPL` für „Read-Evaluate-Print Loop“. 

Mit `Ctrl-D` verlässt du den REPL und startest, falls das Python Programm `main.py` auf dem Board ist, das Programm.

Mit `Ctrl-C` beendest du die Auführung und kommst zurück in den REPL.

## Einfache Datentypen
Probier es aus, indem du zunächst `a = 42` (oder eine andere Zahl) eingbst und mit Enter bestätigt. Die nächste Anweisung lautet `print("a =", a)`. Als Ausgabe erhälst du `a = 42`. Mit `type(a)` frägst du den Variablentyp von `a` ab. 

Dann gebt ihr `a = 1.0` ein, danach einfach a und schließlich wieder `type(a)`:

Erste Schritte mit MicroPython in der `Thonny` Shell.
```
>>> a=42
>>> print("a = ", a)
a = 42
>>> type(a)
<class 'int'>
>>> a=1.0
>>> a
1.0
type(a)
<class 'float'>
>>> a="zweiundvierzig"
>>> type(a)
<class 'str'>
```

|Typ   | Eigenschaft|
|----|----------|
|int   | ganze Zahl 1,2,3, usw |
|float | Zahl mit Komma. 1.2,  45.5, 3.141|
|str   | Zeichenkette zB 'Thierry' oder 'Hallo Welt' |
|boolean| Kann `True` oder `False` sein |

Damit hast du schon einiges über Python gelernt:

Du musst keine Variablentypen deklarieren. Python interpretiert den Typ aus der Art der Eingabe:
`a = 42.0` ergäbe ein Float.
Mit `a = "42"` wäre a ein String. Gleichbedeutend ist `a = '42'`.

Anweisungen werden nicht durch ein Semikolon, sondern durch einen Zeilenumbruch abgeschlossen.
Variablentypen sind als Klasse definiert.
Die `print()` Funktion sorgt automatisch für einen Zeilenumbruch.
In der Shell reicht der Variablenname + Enter, um den Wert der Variablen zu erhalten.

Explizite Umwandlungen, z. B. `float(variable)`, `int(variable)` oder `str(variable)` sind auch möglich.
Ihr könnt mehrere Ausgaben in einer `print()` Anweisung zusammenfassen, jeweils durch ein Komma getrennt.
Python fügt automatisch Leerzeichen zwischen den Teilen der Ausgabe ein.
Wenn du den Zeilenumbruch verhindern willst, gib als letztes Argument `end = ""` ein, also z.B. `print("a =", a, end="")`.

Sehr angenehm ist, dass du mit den „Hoch-/Runter“-Pfeiltasten zwischen vorherigen Eingaben herum scrollen könnt.

## Datentyp boolean

Eine Variable von Datentyp `boolean` kann den Wert `True` oder `False` haben.

```
b = 5==6
```

Da 5 nicht gleich 6 ist wird in diesem Fall die Variable den Wert False bekommen.

```
print("b=", b)
b=False
```

## Operatoren

Bei den arithmetischen Operatoren `+`, `-`, `*`, `/` nicht umgewöhnen, ebenso wenig beim Modulo `%`. Exponentialfunktionen realisiert du mit `**`, also z.B. `2**4` für „2 hoch 4“. Das Zeichen für die ganzzahlige Division ist `//`.


Als logische Operatoren steht dir `and`, `or` und `not` zur Verfügung. 

Die Bit- und Shiftoperatoren `&`, `|`, `^`, `~`, `<<`, `>>` sind wieder identisch mit der Arduino / C++ Schreibweise. 

Dasselbe gilt für die Vergleichsoperatoren: `<`, `>`, `<=`, `>=`, `==`, `!=`


## Code Blöcke

Für die nächsten Kapitel musst du wissen was in Python ein Code Block ist. Ein Code Block wird in Python durch einrücken der Befehle erreicht.

Ein Block kann aus beliebig vielen Kommandos bestehen. 

Der erste Block muss immer auf der Spalte 1 sein:

```
if n > 0:
    print("if-block-command-1")
    print("if-block-command-2")
else:
    print("else-block-command-1")
    print("else-block-command-2")
```

Kommandos mit einem `:` am Ende verlangen einen neuen Block zu beginnen. (eine Einrückungstufe höher zu gehen.)


## if – else – elif Konstruktionen

Zu `if` und `else` gibt es wenig zu sagen. Ein else `if` heisst in Micropython `elif`. Hier ein – zugegebenermaßen an sich ziemlich sinnloses – Beispiel:

```
from time import sleep
from random import randint   
while True:
    n = randint(-10, 30)   # random integer between -10 and +30
    print("Random number =", n)
    if n > 0:
        if n > 20:
            print("Number is bigger than 20")
        elif n > 10:
            print("Number is bigger than 10")
        else:
            print("Number is bigger than 0")
    elif n <= 0:
        print("Number <= 0")
    print("...........")
    sleep(1.5)
```

Zusätzlich lernst durch dieses Beispiel:

Zufallszahlen in einem Bereich von x bis y (einschließlich der Grenzen) erzeugt du mit `randint(x,y)`.
Die Funktion randint() muss importiert werden.
`sleep()` funktioniert auch mit Fließkommazahlen.

## For – Schleifen

Gebt Folgendes in der Shell ein:

```
for i in range(1,4):
    print(i)
```

Du siest, dass MicroPython intelligent ist und nach dem Doppelpunkt weitere Eingaben erwartet. Ihr erhaltet:

Du kannst `range()` auch einen dritten Parameter übergeben und damit das Inkrement ändern. Probier mal `range(1,10,2)` und `range(4,1,-1)` und schaut was passiert.

Oder du übergbst nur einen Parameter, nämlich das obere Limit. `range(x)` entspricht `range(0,x)`.

## While Schlaufen

Mit einer While Schlaufe wiederholt sich ein Programmblock solange wie eine Bedingung (in diesem Fall `a < 5') erfüllt ist.
```
>>> a=0
>>> while a < 5:
       print(a)
       a=a+1
    
0
1
2
3
4
>>>
```

Falls du ein Programmblock immer wieder wiederholen will kannst du dass ebenfalls mit dem while Kommando machen:

```
while True:
   led.toggle()
   sleep(1)
```

## Die input() Funktion

Mit der `input()` Funktion kannst du Daten über die Shell eingeben. Die Eingabe wird als String interpretiert und muss ggf. explizit umgewandelt werden.

```
while True:
    n = input("Input a number: ")
    n = int(n)
    if n > 0:
        if n > 20:
            print(n, "is bigger than 20")
        elif n > 10:
            print(n, "is bigger than 10")
        else:
            print(n, "is bigger than 0")
    elif n <= 0:
        print(n, "is <= 0")
    print("...........")
```

## Das erste Programm
Die direkte Eingabe von Code ist sehr praktisch, aber normalerweise wirst du deine Programme in Form von Dateien schreiben. Dazu kommen wir jetzt. Außerdem willst du sicherlich sehen, wie du mit MicroPython die LED steuert.


```
import pyb
import time 

led = pyb.LED(1)

while True:
    led.toggle()
    time.sleep(1)
```

Speichert das Programm über die Menüleiste (File → Save) oder über das Diskettensymbol.


