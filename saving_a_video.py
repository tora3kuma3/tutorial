import cv2


device_id = 0
cap = cv2.VideoCapture(device_id)

codec = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
fps = 20.0
size = (640, 480)
out = cv2.VideoWriter('output.mp4v', codec, fps, size)

while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        cv2.imshow('frame', frame)

        # Write the flipped frame
        out.write(frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
