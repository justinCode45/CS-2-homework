import cv2


# Load the img

img = cv2.imread('test.jpg')

# Convert the img to grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#show the img

cv2.imshow('gray', gray)