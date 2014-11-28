import cv2


cap = cv2.VideoCapture()
if cap.isOpened() is not True:
    # if there is a single camera connected, just pass 0
    device_id = 0
    cap.open(device_id)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
