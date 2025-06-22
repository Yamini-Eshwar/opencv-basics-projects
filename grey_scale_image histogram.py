import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
cv.imshow('gray_hist', gray_hist)

plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('Pixel')
plt.plot(gray_hist)

plt.xlim([0,256])
plt.show()

cv.waitKey(0)