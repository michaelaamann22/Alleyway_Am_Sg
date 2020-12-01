import math
from random import seed
from random import randint

# Number of columns and rows in the grid https://py.processing.org/tutorials/2dlists/
nCols = 10;
nRows = 10;
n_Steine = nRows * nCols;

Ball_r = 16;
Schieber_r = 15;

v2 = PVector(100, 300)
velocity2 = PVector(5, 5)
v1 = PVector(200, 100)
velocity = PVector(2, 2) # Geschwindigkeit des Spielballs
v2 = PVector(300, 300)
velocity2 = PVector(5, 5)
v3 = (0,0)

def setup():
  size (600, 600);
  smooth();
  background(0, 80, 125)
  global f, nCols, nRows, grid
  f = createFont("Arial",16)
  grid = makeGrid()
  for i in xrange(nCols):
      for j in xrange(nRows):
          #intialisieren der einzelnen Objekte
          grid[i][j] = Cell(i*20,j*20,20,20,i+j)
          


def draw():
    global f, nCols, nRows, grid
    background(0)
    textFont(f,44)            
    fill(255)
    rect(0,0,width,height); 
    v1.add(velocity);

    #Anzeige
    stroke(0);
    fill(200);
    ellipse(v2.x, v2.y, Schieber_r*2, Schieber_r*2);                
    stroke(0);
    fill(175);
    ellipse(v1.x,v1.y,Ball_r,Ball_r);
        
#Backsteine    
    for i in xrange (nCols):
        for j in xrange(nRows):
            grid[i][j].display()
            
#Veränderung des Balls
   
    if v1.x > width or v1.x < 0: #PVector.dist(v1,v2) < 35
        velocity.x = velocity.x * -1;

    if v1.y < 0:
        velocity.y = velocity.y * -1;
    
    if v1.x - v2.x > 30 and PVector.dist(v1,v2) < Ball_r+Schieber_r:
        velocity.x = velocity.x * -1;
    
    if v1.x - v2.x < 30 and PVector.dist(v1,v2) < Ball_r+Schieber_r:
        velocity.y = velocity.y * -1;
          
#Ball fällt runter
    if v1.y >= height:
        textAlign(CENTER)
        text("Game Over!",width/2, 200);                            
        
#Der Schieber     
   
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            v2.x -= 5
        elif keyCode == RIGHT:
            v2.x += 5

# Creates a 2D List of 0's, nCols x nRows large
def makeGrid():
    global nCols, nRows
    grid = []
    for i in xrange(nCols):
        # Create an empty list for each row
        grid.append([])
        for j in xrange(nRows):
            # Pad each column in each row with a 0
            grid[i].append(0)
        return grid

# A Cell object
class Cell():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, tempX, tempY, tempW, tempH, tempAngle):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH
        self.angle = tempAngle
        
def display(self):
    stroke(255)
    # Color calculated using sine wave
    fill(127+127*sin(self.angle))
    rect(self.x,self.y,self.w,self.h)
   
    

      
