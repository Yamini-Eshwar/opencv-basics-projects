import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
# cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  
# img.shape → (height, width, channels) 
# img.shape[:2] → (720, 1280) You are slicing the first two values of the shape=> height, width thats it
# cv.imshow('blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 +45, img.shape[0]//2 +45), 100, 255, -1)
# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)