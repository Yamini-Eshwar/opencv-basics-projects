import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
cv.imshow('Original', img)


# BGR TO GRAY
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
# cv.imshow('Gray', gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Lab', lab)


# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# plt.imshow(rgb)
# plt.show()


# HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)


cv.waitKey(0)