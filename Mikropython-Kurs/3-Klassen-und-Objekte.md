# Klassen und Objekte



## Definition einer Klass

def isIn(firstCorner=(0,0),secondCorner=(0,0),point=(0,0)):

   #assign values to variables
   x1,y1=firstCorner[0],firstCorner[1]
   x2,y2=secondCorner[0],secondCorner[1]

   x,y=point[0],point[1]
   #A point lies inside or not the rectangle
   #if and only if it’s x-coordinate lies
   #between the x-coordinate of the given bottom-right
   #and top-left coordinates of the rectangle
   #and y-coordinate lies between the y-coordinate of
   #the given bottom-right and top-left coordinates.
   if (x >= x1 and x <= x2 and y >= y1 and y <= y2) :
       return True
   #alternate case if coordinates are in reverse order
   elif(x >= x2 and x <= x1 and y >= y2 and y <= y1):
       return True

   else:
       return False

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

 p=Paddle(64,32,0,128,20,30)