

import cv2
from deepface import DeepFace

img = cv2.imread('happyboy.jpeg')

import matplotlib.pyplot as plt
import numpy as np

plt.imshow(img) #BGR

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


predictions = DeepFace.analyze(img)

predictions

type(predictions)

predictions['dominant_emotion']

"""##rectangle around face"""



faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml' ) # haar algo to detect face

gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #print(faceCascade.empty())

faces = faceCascade.detectMultiScale(gray, 1.1 , 4)
#to draw rectangle around faces
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 
           predictions['dominant_emotion'],
            (0, 50),
           font, 3,
           (0,255,0),
           2,
           cv2.LINE_4);

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

import cv2

from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml' )

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Can not open Webcam")
    
while True:
    ret, frame = cap.read()
    
    result = DeepFace.analyze(frame, actions =['emotion'])
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #print(faceCascade.empty())

    faces = faceCascade.detectMultiScale(gray, 1.1 , 4)
    #to draw rectangle around faces
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
        
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, 
                predictions['dominant_emotion'],
                (0, 50),
                font, 3,
                (0,255,0),
                2,
                cv2.LINE_4)
    cv2.imshow('Original video', frame)
    
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

