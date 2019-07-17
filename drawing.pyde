#By Joshua Lewis
#July 16, 2019
baseSize = 1000        #Creation of baseSize variable
drawMode = True;       #Creation of drawMode variable with defalut set to true
rainbowMode = False;   #Creation of rainbowMode variable with defalut set to false
rectangleMode = False; #Creation of rectangleMode variable with defalut set to false
circleMode = False;    #Creation of circleMode variable with defalut set to false
triangleMode = False;  #Creation of triangleMode variable with defalut set to false

def setup():
    global r,g,b,brushThickness,eraserThickness,drawMode,rainbowMode,rectangleMode,circleMode,triangleMode              #Makes variables visable in setup
    size(baseSize,baseSize)                                                                                               #Sets size to value of baseSize
    noStroke()                                                                                                            #Removes border from background
    background(0)                                                                                                         #Sets background color to black
    r = 255                                                                                                               #Initailize's the value r in setup
    g = 255                                                                                                               #Initailize's the value g in setup
    b = 255                                                                                                               #Initailize's the value b in setup
    brushThickness = 5
    eraserThickness = 15
    
def draw():
    global r,g,b,brushThickness,eraserThickness,drawMode,rainbowMode,rectangleMode,circleMode,triangleMode    
    #Location of Box's
    colorRed = mousePressed and mouseX < 25 and mouseY < 25                              #Checks for a press in the position of red box
    colorGreen = (mousePressed and mouseX < 25 and mouseY in range(25, 50))              #Checks for a press in the position of green box
    colorBlue = (mousePressed and mouseX < 25 and mouseY in range(50, 75))               #Checks for a press in the position of blue box
    colorYellow = (mousePressed and mouseX < 25 and mouseY in range(75, 100))            #Checks for a press in the position of yellow box
    colorTeal = (mousePressed and mouseX < 25 and mouseY in range(100, 125))             #Checks for a press in the position of teal box
    colorRandom = (mousePressed and mouseX < 25 and mouseY in range(125, 150))           #Checks for a press in the position of random box
    colorRainbow = (mousePressed and mouseX < 25 and mouseY in range(150, 175))          #Checks for a press in the position of rainbow box
    
    modeRectangle = (mousePressed and mouseX < 50 and mouseY in range(225, 250))         #Checks for a press in the position of the rectangle
    modeCircle = (mousePressed and mouseX < 37.5 and mouseY in range(263, 288))          #Checks for a press in the position of the circle
    modeTriangle = (mousePressed and mouseX < 40 and mouseY in range(300, 325))          #Checks for a press in the position of the triangle
    eraserSmall = (mousePressed and mouseX > 975 and mouseY in range(110,135))           #Checks for a press in the position of eraser 
    eraserMedium = (mousePressed and mouseX > 965 and mouseY in range(60,95))    
    eraserLarge = mousePressed and mouseX > 950 and mouseY < 50    
      
    #Drawing
    if (mousePressed and drawMode and not rainbowMode and mouseX > 50):
        strokeWeight(brushThickness)                              #Makes the pen thicker
        stroke(r,g,b)                                             #Sets pen color to the value of variables r g, and  b
        line(pmouseX,pmouseY,mouseX,mouseY)                       #Starts at past mouse position and ends at current to draw a line 
        
     #Color Chooser    
    if colorRed:                                     #Checks if mouse is clicked between those positions. If so changes color to rgb value
        r = 255                                      #Changes the value of r
        g = 0                                        #Changes the value of g
        b = 0                                        #Changes the value of b
        drawMode = True                              #Sets drawMode to true
        rainbowMode = False                          #Sets rainbowMode to false
        rectangleMode = False
        circleMode = False
        triangleMode = False
        
    elif colorGreen:
          r = 0
          g = 255
          b = 0
          drawMode = True 
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
        
    elif colorBlue:
          r = 0
          g = 0
          b = 255
          drawMode = True
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
        
    elif colorYellow:
          r = 255
          g = 255
          b = 0
          drawMode = True
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
        
    elif colorTeal:
          r = 32
          g = 247
          b = 244
          drawMode = True
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
        
    elif colorRandom:
          r = random(255)
          g = random(255)
          b = random(255)
          drawMode = True
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
        
    elif colorRainbow:                               #Checks if mouse is clicked bwtween those positions. If so changes from normal drawing to rainbow mode.
          drawMode = True                            #Changes value of drawMode to true
          rainbowMode = True                         #Changes value of rainboeMode to true
          rectangleMode = False                      #Changes value of rectangleMode to false
          circleMode = False                         #Changes value of circleMode to false
          triangleMode = False                       #Changes value of triangleMode to false
       
    elif eraserSmall:                                     
          drawMode = False
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
          eraserThickness = 5

    elif eraserMedium:                                     
          drawMode = False
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
          eraserThickness = 15

    elif eraserLarge:                                     
          drawMode = False
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = False
          eraserThickness = 30
       
    elif modeRectangle:
          drawMode = False
          rainbowMode = False
          rectangleMode = True
          circleMode = False
          triangleMode = False
          
    elif modeCircle:
          drawMode = False
          rainbowMode = False
          rectangleMode = False
          circleMode = True
          triangleMode = False
          
    elif modeTriangle:
          drawMode = False
          rainbowMode = False
          rectangleMode = False
          circleMode = False
          triangleMode = True
            
        
    #Rainbow Pen
    if (mousePressed and drawMode and rainbowMode):
        r = random(255)
        g = random(255)
        b = random(255)
        strokeWeight(5)
        stroke(r,g,b)
        line(pmouseX,pmouseY,mouseX,mouseY)
        
    #Erase
    if(mousePressed and not drawMode):
        r = 0
        g = 0
        b = 0
        strokeWeight(eraserThickness)
        stroke(r,g,b)
        line(pmouseX,pmouseY,mouseX,mouseY)
    
    if(mousePressed and not drawMode and rectangleMode):
        fill(255,255,255)
        rect(mouseX,mouseY,20,10)
         
    # if(mousePressed and not drawMode and circleMode):
    #     #TODO add action
         
    # if(mousePressed and not drawMode and triangleMode):
    #     #TODO add action
    
    #Box Setup
    #Red Square
    noStroke()
    fill(255,0,0)
    rect(0,0,25,25)
    
    #Green Sqaure
    noStroke()
    fill(0,255,0)
    rect(0,25,25,25)
    
    #Blue Square
    noStroke()
    fill(0,0,255)
    rect(0,50,25,25)
    
    #Yellow Square
    noStroke()
    fill(255,255,0)
    rect(0,75,25,25)
    
    #Light Blue Square
    noStroke()
    fill(32,247,244)
    rect(0,100,25,25)
    
    #Random Sqaure
    noStroke()
    fill(255,255,255)
    rect(0,125,25,25)
    fill(255,0,0)
    ellipse(12,138,10,10)
    
    #Rainbow Sqaure
    noStroke()
    fill(111,17,184)
    rect(0,150,25,5)
    fill(65,200,184)
    rect(0,155,25,5)
    fill(255,255,0)
    rect(0,160,25,5)
    fill(45,247,23)
    rect(0,165,25,5)
    fill(235,75,203)
    rect(0,170,25,5)
    fill(0,255,255)
    rect(0,175,25,5)
    
    #Rectangle
    noStroke()
    fill(255)
    rect(0,225, 50,25)
    
    #Circle
    noStroke()
    fill(255)
    ellipse(25,275,25,25)
    
    #Triangle
    noStroke()
    fill(255)
    triangle(25,300,10,325,40,325)
    
    #Eraser Small
    noStroke()
    fill(255,192,203)
    rect(975,105,25,25)    
    
    #Eraser Medium
    noStroke()
    fill(255,192,203)
    rect(965,60,35,35)
    
    #Eraser Large
    noStroke()
    fill(255,192,203)
    rect(950,0,50,50)
    
