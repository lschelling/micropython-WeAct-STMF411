import lib.framebuf2 as framebuf   

class Ball:
    def __init__(self, x, y, r):
        self.x=x
        self.y=y
        self.r=r
        self.speedx=1
        self.speedy=2

    def onTimer(self):
        if self.x > 128-self.r or self.x < self.r:
            self.speedx=self.speedx*-1
        if self.y > 64-self.r or self.y < self.r:
            self.speedy=self.speedy*-1            

        self.x=self.x+self.speedx
        self.y=self.y+self.speedy


    def debug(self):
        print(self.x)
        print(self.y)
    

    def draw(self, fb):
        fb.circle(self.x, self.y, self.r,1, True)
        
    def getXPos(self):
        return self.x
        
    def getYPos(self):
        return self.y

        
class Paddle:
    def __init__(self, xpos, ypos, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

    # moves the paddle based on supplied values
    def moveLeft(self, inc):
        self.xpos += inc

    def moveRight(self, inc):
        self.xpos -= inc

    def hit(self, x, y):
        print('X:'+str(x)+' Y:'+str(y))
        if y>=54:
            return  x >= self.xpos - self.width/2 and x <= self.xpos + self.width/2
        else:
            return True
    
    def draw (self, fb):
        fb.rect(self.xpos-self.width//2, self.ypos-self.height//2, self.width, self.height, 1, True)
    