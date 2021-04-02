
import cv2
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

#A debug toolbar appears along the top with the following commands from left to right: continue (F5),
#  step over (F10),
#  step into (F11), 
# step out (Shift+F11), 
# restart (Ctrl+Shift+F5), 
# and stop (Shift+F5).