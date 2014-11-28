import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)


cv2.circle(img, (256, 128), 60, red, 50)
cv2.circle(img, (160, 288), 60, green, 50)

pts = np.array([[256, 128], [160, 288], [352, 288]], np.int32)
cv2.fillPoly(img, [pts], black)
cv2.circle(img, (352, 288), 60, blue, 50)
pts2 = np.array([[304, 200], [400, 200], [352, 288]], np.int32)
cv2.fillPoly(img, [pts2], black)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, white, 10, 4)

cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()