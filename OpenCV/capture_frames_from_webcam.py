import cv2
import numpy as np
# For taking frames from WebCam
video = cv2.VideoCapture(0)

ptr = 0 # variable to store frame count
fr = 0 # variable to store frame number catptured
while(video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        # Remove below comment to convert frames to Gray Scale
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2. imshow('frame', frame)
        if ptr % 1 == 0: # Change % 1 to capture frames after a specific interval
            cv2.imwrite("frame_no_"+str(fr)+".jpg",frame)
            fr += 1
        ptr += 1
        if(cv2.waitKey(20)==27):
            break
    else:
        break

# After the job is done release all the windows        
video.release()
cv2.destroyAllWindows()
