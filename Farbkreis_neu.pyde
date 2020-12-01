background_color = 127
    
def setup() :
    size(768, 256)
    background(255,255,255)
    
def draw() :
    fill(mouseX,mouseY,background_color)
    stroke(255)
    square(0, 0, 256)
    
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
    rect(375,52.5,50,120)
    text("r = " + str(mouseX), 300, 60)
    text("g = " + str(mouseY), 300, 120)
    text("b = " + str(background_color), 300, 180)
    
def RechteckRechts():
    rect(575,52.5,50,120)
    text("r = " + str(mouseX), 500, 60)
    text("g = " + str(mouseY), 500, 120)
    text("b = " + str(background_color), 500, 180) 
    
def LinksLeer():
    fill(255)
    rect(280, 45, 200, 160)
    
def RechtsLeer():
    fill(255)
    rect(480, 45, 200, 160)
    
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
            
