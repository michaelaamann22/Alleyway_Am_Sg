# Number of columns and rows in the grid
nCols = 10;
nRows = 10;
n_Steine = nRows * nCols;


Steine_Breite = 30;
Steine_Hoehe = 10;




Ball_r = 16;
Schieber_r = 15;
v1 = PVector(200, 100) # Startpunkt des Spielballs
velocity = PVector(2, 2) # Geschwindigkeit des Spielballs
v2 = PVector(300, 300) # Startpunkt des Schiebers
velocity2 = PVector(5, 5) # Geschwindigkeit des Schiebers
v3 = PVector (100, 100) # Steine

def setup():
  size (600, 400);
  background(0, 80, 125)
  global f
  f = createFont("Arial",16) 
  
def touch (value):
    global t
    t = value
t = False

  



def draw():
    global f
    textFont(f,44)            
    fill(0)
    rect(0,0,width,height); 
    fill(255.10);
    v1.add(velocity);
    if t == True:
        fill(0)
        rect (v3.x, v3.y, Steine_Breite, Steine_Hoehe)
    else:
        rect (v3.x, v3.y, Steine_Breite, Steine_Hoehe)
    
#Veränderung des Balls
   
    if v1.x > width or v1.x < 0: #PVector.dist(v1,v2) < 35
        velocity.x = velocity.x * -1;

    if v1.y < 0:
        velocity.y = velocity.y * -1;
        
    # Vektor in die richtige Richtung zurück spicken
    if v1.x - v2.x > 30 and PVector.dist(v1,v2) <= Ball_r+Schieber_r:
        velocity.x = velocity.x * -1; 
    
    if v1.x - v2.x < 30 and PVector.dist(v1,v2) <= Ball_r+Schieber_r:
        velocity.y = velocity.y * -1;
        

    if v1.x - v3.x > 5 and PVector.dist(v1,v3) <= Ball_r+Steine_Breite:
        velocity.x = velocity.x * -1 
    
    
    if v1.x - v3.x < 5 and PVector.dist(v1,v3) <= Ball_r+Steine_Hoehe:
        velocity.y = velocity.y * -1 
    

          
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
    if v1.x - v3.x > 5 and PVector.dist(v1,v3) <= Ball_r+Steine_Breite:
        fill(0)
        rect (v3.x, v3.y, Steine_Breite, Steine_Hoehe)
        touch(True)
    
    if v1.x - v3.x < 5 and PVector.dist(v1,v3) <= Ball_r+Steine_Hoehe:
        fill(0)
        rect (v3.x, v3.y, Steine_Breite, Steine_Hoehe)
        touch(True)
        
# print (t); um zu überprüfen    
    
#Anzeige
    #rect (v3.x, v3.y, Steine_Breite, Steine_Hoehe)
    fill(200);
    ellipse(v2.x, v2.y, Schieber_r*2, Schieber_r*2);                
    fill(175);
    ellipse(v1.x,v1.y,Ball_r,Ball_r);

 
