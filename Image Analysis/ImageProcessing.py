import numpy as np
import cv2
import matplotlib as plt
from math import sqrt

# Read the image
image = cv2.imread(r"C:\Users\Nilayy\Desktop\ImageProcessing\resim4.jpeg")
imgray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours = " + str(len(contours)))

def areaOfObjects():
    i=0
    for i in contours:
        area=cv2.contourArea(i)
        print("Area of contour: " + str(area))
    return

def rotatedBoundingBox():
    #Rotated Regtangle Bounding Box
    i=0
    for i in contours:
        rect = cv2.minAreaRect(i)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, (0, 0, 255), 2)
    return

def straightBoundingRectangle_boundingBox():
    #Straight Bounding Rectangle
    i = 0
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return

def majorAxisLength():
    #Fit an elipse
    i = 0
    for i in contours:
        ellipse = cv2.fitEllipse(i)
        cv2.ellipse(image, ellipse, (255, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if w>h:
            majorAxisLength=w/2 #Divide 2 because opencv finds major axis lengths finding 2 times.
        else:
            majorAxisLength = h/2
        print("Major Axis Length of countour: " + str(majorAxisLength))
    return

def minorAxisLength():
    #Fit an elipse
    i = 0
    for i in contours:
        ellipse = cv2.fitEllipse(i)
        cv2.ellipse(image, ellipse, (255, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if w > h:
            minorAxisLength = h/2  # Divide 2 because opencv finds major axis lengths finding 2 times.
        else:
            minorAxisLength = w/2 #Divide 2 because opencv finds minor axis lengths finding 2 times.
        print("Minor Axis Length of contour: " + str(minorAxisLength))
    return

def eccentricity():
    i = 0
    for i in contours:
        ellipse = cv2.fitEllipse(i)
        cv2.ellipse(image, ellipse, (255, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if w > h:
            majorAxisLength = w/2  # Divide 2 because opencv finds major axis lengths finding 2 times.
        else:
            majorAxisLength = h/2 #Divide 2 because opencv finds minor axis lengths finding 2 times.

        if w > h:
            minorAxisLength = h/2  # Divide 2 because opencv finds major axis lengths finding 2 times.
        else:
            minorAxisLength = w/2 #Divide 2 because opencv finds minor axis lengths finding 2 times.
        c=(((majorAxisLength/2)*(majorAxisLength/2)) - ((minorAxisLength/2)*(minorAxisLength/2)))
        foci=sqrt(c)
        eccentricity = (foci/(majorAxisLength/2))
        print("Eccentricity of contour: " + str(eccentricity))
    return

areaOfObjects()
rotatedBoundingBox()
straightBoundingRectangle_boundingBox()
majorAxisLength()
eccentricity()
minorAxisLength()

#show the image
cv2.imshow('image', image)
#cv2.imshow('Image gray', imgray)

##Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()


