'''
Name- Pratik Lagaskar
Roll no.- 238
Batch- B2
Mini-Project based on OpenCV
Title- 1.Face-Detection 
'''
# importing opencv library
import cv2
from random import randrange

# loading pre-trained data on face frontals from opencv(haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#image reading 
#img = cv2.imread('mum2.jpg')

#video-image reading(real time)
webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Iterates forever over frames
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

    # changing the image to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Drawing boxes around the faces
    for (x, y, w, h) in face_coordinates:  
        cv2.rectangle(frame,(x, y),(x+w, y+h),(randrange(256),randrange(256),randrange(256)),3)\
    
    # show image
    cv2.imshow('Pratik_Face_Detector_App',frame)
    # waits
    key = cv2.waitKey(1)
    
    #force quit
    if key==81 or key==113:
        break

#print(face_coordinates)
# Release the videoCapture Object
webcam.release()

print("~Sayonara~")

