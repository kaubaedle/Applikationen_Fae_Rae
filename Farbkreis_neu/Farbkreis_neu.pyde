background_color = 127
    
def setup() :
    size(768, 512)
    background(255,255,255)
    fill(0)
    textSize(42)
    text("Interaktiver Farbvergleich", 20, 40)
    textSize(15)
    text("Veraendere die Farbe mit der Maus. Horizontal veraendert den Rot-Wert, Vertikal den Gruen-Wert, ", 20, 80)
    text("das Mausrad den Blau-Wert.", 20, 100)
    text("Waehle mit der linken und rechten Maustaste eine Farbe fuer den Vergleich aus.", 20, 120)
    text("Setze deine Auswahl mit der linken und rechten Maustaste zurueck", 20, 140)
    
    #Hier wird die Zeichenfläche mit dem Titel und der Anleitung abgebildet
    
def draw() :
    fill(mouseX,mouseY-256,background_color)
    stroke(255)
    square(0, 256, 256)
    
    #Diese Funktion zeichnet ein Quadrat dessen Farbe aus der Position der Maus und des Mausrades abgeleitet wird
    
def mouseWheel(event) :
    global background_color 
    e = event.getCount()
    background_color += event.getCount()
    # keep value in range
    background_color = background_color % 255
    
    #Diese Funktion holt die Information der Position des Mausrades und wandelt sie in einen Wert um, der für die Farbeingabe benutzt werden kann. Der Wert wird unter der Variable background_color gespeichert. Die Funktion stammt von: https://py.processing.org/reference/mouseWheel.html

def RechteckLinks():
    rect(375,300,50,140)
    text("r = " + str(mouseX), 300, 316)
    text("g = " + str(mouseY-256), 300, 376)
    text("b = " + str(background_color), 300, 436)
    
    #Diese Funktion zeichnet bei einem Linksklick ein Rechteck und die Angaben zur Farbe in der entsprechenden Farbe auf der linken Seite
    
def RechteckRechts():
    rect(575,300,50,140)
    text("r = " + str(mouseX), 500, 312)
    text("g = " + str(mouseY-256), 500, 376)
    text("b = " + str(background_color), 500, 436) 
    
    #Diese Funktion zeichnet bei einem Rechtsklick ein Rechteck und die Angaben zur Farbe in der entsprechenden Farbe auf der rechten Seite
    
def LinksLeer():
    fill(255)
    rect(280, 301, 200, 160)
    
    #Diese Funktion löscht bei betätigen der linken Pfeiltaste die Farbangaben und das Rechteck auf der linken Seite 
    
def RechtsLeer():
    fill(255)
    rect(480, 301, 200, 160)
    
    #Diese Funktion löscht bei betätigen der rechten Pfeiltaste die Farbangaben und das Rechteck auf der rechten Seite

def Kreis():
    ellipse(mouseX, mouseY, 20, 20)
    
    
def mouseClicked(event) :
    # print(mouseX, mouseY, background_color)
    if mouseClicked:
        if mouseButton == LEFT:
            RechteckLinks()
            #Kreis()

        if mouseButton == RIGHT:
            RechteckRechts()
            #Kreis()

    #Diese Funktion erfasst einen Mausklick und betätigt die jeweilige Funktion        
    

def keyPressed():
    if key == CODED:
        if keyCode == LEFT:
            LinksLeer()
        if keyCode == RIGHT:
            RechtsLeer()

    #Diese Funktion erfasst einen Tastendruck und betätigt die jeweilige Funktion
            
