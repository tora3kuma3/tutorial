import cv2


cap = cv2.VideoCapture('output.mp4v')

while cap.isOpened():
    ret, frame = cap.read()

    if ret is not True:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()