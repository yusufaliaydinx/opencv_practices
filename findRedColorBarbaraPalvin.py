import cv2
import numpy as np

resim = cv2.imread("barbara.jpg")

scale_percent = 50
width = int(resim.shape[1] * scale_percent / 100)
height = int(resim.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(resim, dsize)


down = np.array([150,50,50])
up = np.array([190,255,255])


hsv = cv2.cvtColor(output,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,down,up)
last_image = cv2.bitwise_and(hsv,hsv,mask = mask)


cv2.imshow("resized",output)
cv2.imshow("BGR default",output)
cv2.imshow("red in mask",mask)
cv2.imshow("HUE STRATION VALUE(HSR) space",hsv)
cv2.imshow("red processing",last_image)


cv2.waitKey(0)
cv2.destroyAllWindows()