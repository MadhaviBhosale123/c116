import cv2
img = cv2.imread('F:/Madhavi Folder/New folder/poster.jpg')
cv2.imshow('Display Image',img)
print(img)
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('Image',grey)

cv2.waitKey(0)
