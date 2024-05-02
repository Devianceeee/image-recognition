import cv2
import math

img=cv2.imread("image001.jpg")
height=img.shape[0]
width=img.shape[1]
x=round((300*width)/height)

if(height>100):
    img = cv2.blur(img, (5, 5))
img=cv2.resize(img,(x,300))
img=cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 120, 250, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
h1,w1,c1=img.shape

text = ""
var=0

for c in contours:
    accuracy = 0.055*cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,accuracy,True)

    x,y,w,h=cv2.boundingRect(approx)

    if(len(approx)==4):
        var=0
        ax1, ay1 = approx[0][0]
        ax2, ay2 = approx[3][0]
        bokA = math.sqrt((ax1 - ax2) ** 2 + (ay1 - ay2) ** 2)

        bx1, by1 = approx[1][0]
        bx2, by2 = approx[2][0]
        bokB = math.sqrt((bx1 - bx2) ** 2 + (by1 - by2) ** 2)

        cx1, cy1 = approx[0][0]
        cx2, cy2 = approx[1][0]
        bokC = math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

        dx1, dy1 = approx[2][0]
        dx2, dy2 = approx[3][0]
        bokD = math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

        if (bokA > (2 * bokB)) or (bokB > (2 * bokA)):
            var=1
        if (bokC > (2 * bokD)) or (bokD > (2 * bokC)):
            var=1

        if(w>(2*h)) and (w>30):

            if(var==0):
                text="stop"
                draw = cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)


        if(h>(2*w)):

            if(h>(h1/10)) and (h<(h1/2)) and (var==0):

                text="mozna jechac"
                draw = cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

x=0
y=round(h1/2)
org=(x,y)
img = cv2.putText(img, text,org, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 2), 2, cv2.LINE_AA)
cv2.imshow('',img)
cv2.waitKey(0)