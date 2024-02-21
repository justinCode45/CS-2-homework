import cv2
# new comment
#set window's size
# cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)

# Read the input image
img = cv2.imread('test.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale', gray)

# Wait for a key press and close the image window
cv2.waitKey(0)
