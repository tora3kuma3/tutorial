import cv2
import numpy as np


drawing = False     # true if mouse is pressed
mode = True     # if True, draw rectangle. Press 'm' toggle to curve
ix, iy = -1, -1


def draw(is_rectangle, sx, sy, ex, ey):
    if is_rectangle is True:
        cv2.rectangle(img, (sx, sy), (ex, ey), (0, 255, 0), -1)
    else:
        cv2.circle(img, (ex, ey), 5, (0, 0, 255), -1)


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            draw(mode, ix, iy, x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        draw(mode, ix, iy, x, y)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while 1:
    cv2.imshow('image', img)
    key = cv2.waitKey(20) & 0xff
    if key == 27:
        break
    elif key == ord('m'):
        mode = not mode

cv2.destroyAllWindows()