# Klassen und Objekte
Eine Klasse fasst Variablen und Funktionen zusammen. Mit den Funktionen wird auf die internen Variablen zugegriffen.
Diese Variablen werden auch Attribute genannt. Ein Objekt wird aus eine Klasse erzeugt. Es ist möglich beliebig viele Objekte aus einer Klasse zu erzeugen.

Wenn wir jetzt für unser Pong Spiel überlegen welche Klassen da Sinn machen wären das.

- Paddle: der Schieber welche den Ball auffängt
- Ball: der Ball
- uns sicher noch einige mehr welche uns im Verlauf des Projekts in den Sinn kommen

## Definition einer Klasse
Schauen wir uns mal das Beispiel `Paddle` an:

```
class Paddle:
    def __init__(self, xpos, ypos, xmin, xmax, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.xmax = xmax
        self.xmin = xmin
        self.width = width
        self.height = height

    # moves the paddle based on supplied values
    def MoveInc(self, inc):
        if (self.xpos - inc < self.xmax):
            self.xpos += inc

    def MoveDec(self, inc):
        if (self.xpos + inc > self.xmin):
            self.xpos -= inc

    def Collision(self, x, y):
        return  x >= self.xpos - self.width/2 and x <= self.xpos + self.width/2 and y >= self.ypos - self.height/2 and y <= self.ypos + self.height/2
```

Du siehtst dass eine Klasse im mit dem Schlüsselwort `class` beginnt. Danach kommt die Funktion `__init__`. Dieser Name ist von Python so vorgegeben. Die Funktion wird immer als erstes ausgeführt wenn du ein Objekt aus einer Klasse erzeugst. In der objektorientierten Programmierung wird diese Funktion auch `Constructor` genannt.

Du kannst auch eine Funktion `__del__` definieren. Diese wird immer aufgerufen wenn ein Objekt gelöscht wird. Diese Funktion wird auch `Destructor` genannt.

Bei den Funktionen wird bei der Klassendefinition immer der Wert `self` mitgegeben. Uber `self` kann dann innerhalb der Klasse auf die Klassenattribute zugegriffen werden.


