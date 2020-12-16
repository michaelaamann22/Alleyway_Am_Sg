
Stein_hoehe = 10
Stein_breite = 20
num_Steine_x = 20
num_Steine_y = 20

Ball_r = 16;
Schieber_x = 30;
Schieber_y = 5;
v1 = PVector(100, 100) # Startpunkt des Spielballs
velocity = PVector(3, 3) # Geschwindigkeit des Spielballs
v2 = PVector(200, 500) # Startpunkt des Schiebers
velocity2 = PVector(5, 5) # Geschwindigkeit des Schiebers

def setup():
    global num_Steine_x, num_Steine_y, raster, f
    f = createFont("Arial",16)
    size(400, 600)
    raster = Steinezeichnen()
    for i in range(num_Steine_x):
      for j in range(num_Steine_y):
          #intialisieren der einzelnen Objekte
          raster[i][j] = Steine(i*Stein_breite,j*Stein_hoehe,Stein_breite,Stein_hoehe)
    
#https://www.snakify.org/de/lessons/two_dimensional_lists_arrays/    
          
                      
def draw():
    global num_Steine_x, num_Steine_y, raster, f
    textFont(f,44)            
    fill(255.10);
    v1.add(velocity);
    background(0)
    rect (v2.x, v2.y, Schieber_x, Schieber_y)
    stroke(0);
    fill(175);
    ellipse (v1.x,v1.y,Ball_r,Ball_r);

#Der Schieber       
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            v2.x -= 5
        elif keyCode == RIGHT:
            v2.x += 5 
                
#Veränderung des Balls
    # Berührung der Wände
    if v1.x > 400 or v1.x < 0: #PVector.dist(v1,v2) < 35
        velocity.x = velocity.x * -1;

    if v1.y < 0:
        velocity.y = velocity.y * -1;
        
    # Vektor in die richtige Richtung zurück spicken, Schieber
    if v1.x - v2.x > Ball_r+Schieber_x/2 and PVector.dist(v1,v2) <= Ball_r+Schieber_x/2:
        velocity.x = velocity.x * -1; 
    
    if v1.x - v2.x < Ball_r+Schieber_x/2 and PVector.dist(v1,v2) <= Ball_r+Schieber_x/2:
        velocity.y = velocity.y * -1;
        
# Vektor in die richtige Richtung zurück spicken, Backsteine         
#trifft Stein von unten links  
    if  dist(v1.x, v1.y, Steine.tempX, Steine.tempY) <= Ball_r/2 + Stein_breite/2 and v1.y - Steine.tempY >= 0 and v1.x - Steine.tempX <= 0:
           velocity.y = velocity.y * -1;
           
    #trifft Stein von oben links
    if  dist(v1.x, v1.y, Steine.tempX, Steine.tempY) <= Ball_r/2 + Stein_breite/2 and v1.y - Steine.tempY <= 0 and v1.x - Steine.tempX <= 0:
           velocity.y = velocity.y * -1;    
          
    #trifft Stein von oben rechts 
    if  dist(v1.x, v1.y, Steine.tempX, Steine.tempY) <= Ball_r/2 + Stein_breite/2 and v1.y - Steine.tempY <= 0 and v1.x -Steine.tempX >= 0:
           velocity.y = velocity.y * -1;
          
    #trifft Stein von unten rechts
    if  dist(v1.x, v1.y, Steine.tempX, Steine.tempY) <= Ball_r/2 + Stein_breite/2 and v1.y - Steine.tempY >= 0 and v1.x - Steine.tempX >= 0:
           velocity.y = velocity.y * -1;    
      
        
#Ball fällt runter
    if v1.y >= 600:
        textAlign(CENTER)
        text("Game Over!",400/2, 600/2); 
        
#Steine darstellen          
    for i in range(num_Steine_x):
        for j in range(num_Steine_y):
            # Zelle darstellen
            raster[i][j].Backsteine()
          
# kreiert eine leere Liste für die Backsteine
def Steinezeichnen():
    global num_Steine_x, num_Steine_y
    raster = []
    for i in xrange(num_Steine_y):
        # leere Liste für jede Reihe
        raster.append([])
        for j in xrange(num_Steine_x):
            # Pad each column in each row with a 0
            raster[i].append(0)
    return raster    

#die Backsteine als Klasse
class Steine():
    tempX = 0
    tempY = 0
    tempW = 0
    tempH = 0         
              
    def __init__(self,tempX,tempY,tempW,tempH):
        self.x = tempX
        self.y = tempY
        self.w = tempW
        self.h = tempH    
            
    def Backsteine(self):
        
        fill(255);
        stroke(0);   
        rect(self.x,self.y,self.w,self.h);

    
                                     
      
        
