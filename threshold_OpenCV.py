import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
# cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold inv', thresh_inv)

# adaptive thresholding
a_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("a_thresh", a_thresh)

cv.waitKey(0)