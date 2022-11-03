import cv2
import time

video=cv2.VideoCapture(0) # 0 is the webcam number

while True:
    check, frame = video.read() # check is a bool, frame is the 1st frame captured
    print(check)
    print(frame)

    time.sleep(1)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(2000) # 0 means wait infifnitely for a key, otherwise wait x milliseconds are the key

    if key==ord('e'):
        break
video.release() # releases the camera
cv2.destroyAllWindows