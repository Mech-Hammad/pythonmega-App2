import cv2
import time
import pandas as pd

video=cv2.VideoCapture(0) # 0 is the webcam number

data = pd.DataFrame(columns=['Start', 'End'])

first_frame = None
while True:
    check, frame = video.read() # check is a bool, frame is the 1st frame captured

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0) # apply blur to filter out the noise

    # now convert delta frame to black and white threshold frame

    
    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray) # compare current frame with first reference frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY )[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2) #Smoothes Out

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (0,255,0), 3)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)


    key = cv2.waitKey(1) # 0 means wait infifnitely for a key, otherwise wait x milliseconds for the key

    if key==ord('e'):
        break
video.release() # releases the camera
cv2.destroyAllWindows

