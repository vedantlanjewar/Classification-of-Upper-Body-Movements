# -*- coding: utf-8 -*-
"""COMP 597

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B-I-a41bSjvfmjhfzCIbxqT_Rq2bRqQE
"""

#!pip install mediapipe opencv-python

import cv2
import pandas
import mediapipe as mp
import numpy as np

# Using Mediapipe library to capture pose
# https://google.github.io/mediapipe/solutions/pose#python-solution-api
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

data_1=[]
cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            temp=[]
            temp.append(frame)
            landmarks = results.pose_landmarks.landmark
            temp.append(landmarks)
            data_1.append(temp)
        except:
            pass
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

df = pandas.DataFrame(data_1)
df.to_csv("./data_1.csv", sep=',',index=False)
