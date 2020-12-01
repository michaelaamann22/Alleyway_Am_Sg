import math
from random import seed
from random import randint

# Number of columns and rows in the grid
nCols = 10;
nRows = 10;
n_Steine = nRows * nCols;


Steine_Breite = 30;
Steine_Hoehe = 10;

Stein_x = 15;
Stein_y = 10;

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
  size (600, 400);
  smooth();
  background(0, 80, 125)
  global f
  f = createFont("Arial",16)
  #Zufallszahlen für die Startposition des Balls


def draw():
    global f
    background(255)
    textFont(f,44)            
    fill(0)
    rect(0,0,width,height); 
    fill(255.10);
    v1.add(velocity);
    
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

#die Backsteine

            
    
#Anzeige
    stroke(0);
    fill(200);
    ellipse(v2.x, v2.y, Schieber_r*2, Schieber_r*2);                
    stroke(0);
    fill(175);
    ellipse(v1.x,v1.y,Ball_r,Ball_r);
    

      
