

import cv2 as cv
import numpy as np
blank = np.zeros((400, 400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle' , rect)

cv.imshow('Circle', circle)

# Bitwise And => returns only intersected region
bitwise_and = cv.bitwise_and(rect, circle)
# cv.imshow('bitwise_and', bitwise_and)

# Bitwise OR => returns interect + non-intersect also
bitwise_or = cv.bitwise_or(rect, circle)
# cv.imshow('bitwise_or', bitwise_or)

# Bitwise XOR => non-intersected region
bitwise_xor = cv.bitwise_xor(rect, circle)
# cv.imshow('bitwise_xor', bitwise_xor)

# Bitwise NOR = just inverts blact into white and white into black
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)