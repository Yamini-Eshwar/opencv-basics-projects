import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
cv.imshow('Cat', img)


plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 255])  # indicates the frquency of each pixel intensity of that color value
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)