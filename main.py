import numpy
import pandas
import cv2 as opencv
image = opencv.imread(input("Input a File location: "))
index = ["color","color_name","hex","R","G","B"]
dataset = pandas.read_csv("dataset.csv", names=index, header=None)
clickstate = False
r=0
g=0
b=0
position_x = 0
position_y = 0
def recognizer(R,G,B):
    minimum = 1000
    for i in range(len(dataset)):
        d = abs(R - int(dataset.loc[i,"R"])) + abs(G - int(dataset.loc[i, "G"])) + abs(B - int(dataset.loc[i, "B"]))
        if(d<=minimum):
            minimum = d
            cname = dataset.loc[i, "color_name"]
    return cname
def clickhandler(event, x, y,f,p):
    if event == opencv.EVENT_LBUTTONDBLCLK:
        global b,g,r,position_x,position_y, clickstate
        clickstate = True
        position_x = x
        position_y = y
        b,g,r = image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

opencv.namedWindow('Color Recognition Application')
opencv.setMouseCallback('Color Recognition Application', clickhandler)
while(1):
    opencv.imshow("Color Recognition Application",image)
    if (clickstate):
   
        #opencv.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        opencv.rectangle(image,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = recognizer(r,g,b) + "  RGB("+str(r)+","+str(g)+","+str(b)+")"
        
        #opencv.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        opencv.putText(image, text,(50,50),2,0.8,(255,255,255),2,opencv.LINE_AA)
        #For very light colours we will display text in black colour
    if(r+g+b>=600):
        opencv.putText(image, text,(50,50),2,0.8,(0,0,0),2,opencv.LINE_AA)
            
        clickstate=False
        #Break the loop when user hits 'esc' key    
    if opencv.waitKey(20) & 0xFF ==27:
        break 
opencv.destroyAllWindows()


