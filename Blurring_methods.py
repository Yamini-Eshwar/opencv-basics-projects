import cv2 as cv

img = cv.imread(r"C:\Users\vamsi\Downloads\Cat2.jpg")
cv.imshow('cat', img)

# averaging
average = cv.blur(img, (7, 7))  # as kernel size increases, blurness also
cv.imshow('average', average)

# Guassian Blur
guss = cv.GaussianBlur(img, (7, 7), 0) # sigma=0 here
cv.imshow('Guassian Natural Blur', guss)

# Median blur
median = cv.medianBlur(img, 9)
cv.imshow('median blur', median)

# Bilateral Blur- slow, but preserves edges sharpness
cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('bilateral blur', img)

cv.waitKey(0)