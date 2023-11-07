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
    def locx(self):
        return self.x
    def locy(self):
        return self.y

    def debug(self):
        print(self.x)
        print(self.y)
    

    def draw(self, fb):
        fb.circle(self.x, self.y, self.r,1, True)

        
class Paddle:
    def __init__(self, xpos, ypos, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.hits=0
        self.ground=False

    # moves the paddle based on supplied values
    def moveLeft(self, inc):
        self.xpos += inc

    def moveRight(self, inc):
        self.xpos -= inc
 
    def hit(self, x, y):
        if y > 50:
            if not self.ground:
                self.ground=True
                self.hits=self.hits+1
            return  x >= self.xpos - self.width/2-5 and x <= self.xpos + self.width/2+5 
        else:
            self.ground=False
            return True 
    
    def draw (self, fb):
        fb.text(str(self.hits),5,5)
        fb.rect(self.xpos-self.width//2, self.ypos-self.height//2, self.width, self.height, 1, Tru