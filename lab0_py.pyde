def setup():
    size(600,600)
    
def draw():
    background(255,255,255)
    global centerX
    centerX = width/2
    global centerY
    centerY = height/2
    global scaled
    scaled = 50.0
    global realList
    realList = [1]
    global imaginaryList
    imaginaryList = [0]
    global  xList
    xList = [0]
    global yList
    yList = [0]
    
    def toTraditionalPlot(x,y):
        x = (x - centerX) / scaled
        y = (-y + centerY) / scaled
        return (x,y)
    
    
    def complexMultiply(x1,y1,x2,y2):
        x = (x1*x2) - (y1*y2)
        y = (x1*y2) + (y1*x2)
        return (x,y)

    def calculateVPowers(x,y):
        for i in range(1,10):
            x1, y1 = complexMultiply(x,y,realList[i-1],imaginaryList[i-1])
            realList.append(x1)
            imaginaryList.append(y1)
    
    def calculatePoints():
        currentV = 0
        previousV = 0
        for i in range(1,1023):
            ##alternate between addition and subtraction
            if (i % 2 ==1):
                xList.append(xList[previousV]+realList[currentV])
                yList.append(yList[previousV]+imaginaryList[currentV])
            else:
                xList.append(xList[previousV]-realList[currentV])
                yList.append(yList[previousV]-imaginaryList[currentV])
                previousV += 1
                ##move to next term of V
            if(i == (2**(currentV+2)-2)):
                currentV += 1
                
    def toScreenCoordinates(x,y):
        x = (x*scaled) + centerX
        y = (y*-1*scaled) + centerY
        return(x,y)
    
    def plotPoints():
        for i in range(0,1023):
            fill(0,0,0)
            x,y = toScreenCoordinates(xList[i], yList[i])
            if (x > centerX and y > centerY):
                fill(255,0,0)
            elif (x > centerX and y < centerY):
                fill(0,255,0)
            elif (x < centerX and y > centerY):
                fill(0,0,255)
            else:
                fill(150,150,150)
            ellipse(x,y,5,5)
            
    x, y = toTraditionalPlot(mouseX, mouseY)
    calculateVPowers(x,y)
    calculatePoints()
    plotPoints()
    
    