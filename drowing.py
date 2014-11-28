import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

blue = (255, 0, 0)
cv2.line(img, (0, 0), (511, 511), color=blue, thickness=5)

green = (0, 255, 0)
cv2.rectangle(img, (384, 0), (510, 128), color=green, thickness=3)

red = (0, 0, 255)
cv2.circle(img, (447, 63), 63, red, -1)

cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 100, color=blue, thickness=-1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, red)

font = cv2.FONT_HERSHEY_SIMPLEX
white = (255, 255, 255)
cv2.putText(img, 'OpenCV', (10, 500), font, 4, white, 2, 4)

cv2.imshow('draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()