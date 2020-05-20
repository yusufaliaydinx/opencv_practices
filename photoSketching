import cv2
import numpy as np

img = "togg.jpg"

image = cv2.imread(img)

scale_percent = 0.2
width = int(image.shape[1]*scale_percent)
height = int(image.shape[0]*scale_percent)

dimensions = (width,height)
resized = cv2.resize(image,dimensions,interpolation = cv2.INTER_AREA)  # resizing the image

kernel_sharpening = np.array([[-1,-1,-1],       #Typical kernel for sharpening
                              [-1, 9,-1],
                              [-1,-1,-1]])

sharpened = cv2.filter2D(resized,-1,kernel_sharpening)  # shape the image

gray = cv2.cvtColor(sharpened , cv2.COLOR_BGR2GRAY) # convert to gray

object_detection = cv2.cvtColor(sharpened, cv2.COLOR_BGR2HSV )  #convert in image detection formate

inv = 255-gray  # convert inverse form

gauss = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)   # convert gauss form

sketching = cv2.divide(gray,255-gauss,scale=256)

cv2.imshow("original",image)
cv2.imshow("resized",resized)
cv2.imshow('sharp',sharpened)
cv2.imshow("gray", gray)
cv2.imshow('sketching',sketching)
cv2.waitKey(0)
cv2.destroyAllWindows()
