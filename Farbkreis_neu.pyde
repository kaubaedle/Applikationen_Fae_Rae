background_color = 127
    
def setup() :
    size(768, 512)
    background(255,255,255)
    
def draw() :
    fill(mouseX,mouseY-256,background_color)
    stroke(255)
    square(0, 256, 256)
    
    # fill(255)
    # rect(374, 0, 374, 256)
    
    # print(mouseX, mouseY, background_color)
    
def mouseWheel(event) :
    global background_color 
    e = event.getCount()
    background_color += event.getCount()
    # keep value in range
    background_color = background_color % 255
    
    # https://py.processing.org/reference/mouseWheel.html

def RechteckLinks():
    rect(375,308.5,50,120)
    text("r = " + str(mouseX), 300, 316)
    text("g = " + str(mouseY-256), 300, 376)
    text("b = " + str(background_color), 300, 436)
    
def RechteckRechts():
    rect(575,308.5,50,120)
    text("r = " + str(mouseX), 500, 312)
    text("g = " + str(mouseY-256), 500, 376)
    text("b = " + str(background_color), 500, 436) 
    
def LinksLeer():
    fill(255)
    rect(280, 301, 200, 160)
    
def RechtsLeer():
    fill(255)
    rect(480, 301, 200, 160)
    
def mouseClicked(event) :
    # print(mouseX, mouseY, background_color)
    if mouseClicked:
        if mouseButton == LEFT:
            RechteckLinks()

        if mouseButton == RIGHT:
            RechteckRechts()
            
    #circle(mouseX, mouseY, 20)

def keyPressed():
    if key == CODED:
        if keyCode == LEFT:
            LinksLeer()
        if keyCode == RIGHT:
            RechtsLeer()
            
