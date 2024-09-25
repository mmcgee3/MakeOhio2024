import serial
import serial.tools.list_ports
import numpy as np
import cv2
import time

frontalCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height

ser = serial.Serial('/dev/cu.usbmodem1101', 115200)

command = ""

ser.close()
ser.open()

count = 0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Max', 'Matthew', '3', '4'] 
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        
        
        # If confidence is less them 100 ==> "0" : perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            # if id == "Matthew":
            #     face_center_x = x + w / 2
            #     frame_center_x = img.shape[1] / 2
            
            #     if face_center_x < frame_center_x - 75:
            #         command = "right"
            #     elif face_center_x > frame_center_x + 75:
            #         command = "left"
            #     else:
            #         command = ""
                
            #     print("Sending command:", command)
            #     command = command.encode('utf-8')
            #     ser.write(command)
            #     print("Command sent successfully")
            #     count = 0
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            # if id == "Matthew":
            face_center_x = x + w / 2
            frame_center_x = img.shape[1] / 2
        
            if face_center_x < frame_center_x - 75:
                command = "right"
            elif face_center_x > frame_center_x + 75:
                command = "left"
            else:
                command = ""
            
            print("Sending command:", command)
            command = command.encode('utf-8')
            ser.write(command)
            print("Command sent successfully")
            count = 0
        
        cv2.putText(
                    img, 
                    str(id), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        cv2.putText(
                    img, 
                    str(confidence), 
                    (x+5,y+h-5), 
                    font, 
                    1, 
                    (255,255,0), 
                    1
                   )
    # Frontal face detection
    # frontal_faces = frontalCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.2,
    #     minNeighbors=5,
    #     minSize=(20, 20)
    # )
    # for (x, y, w, h) in frontal_faces:
    #     count += 1
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #     face_center_x = x + w / 2
    #     frame_center_x = img.shape[1] / 2
        
    #     if face_center_x < frame_center_x - 75:
    #         command = "right"
    #     elif face_center_x > frame_center_x + 75:
    #         command = "left"
    #     else:
    #         command = ""
        
    #     if count >= 1:
    #         print("Sending command:", command)
    #         command = command.encode('utf-8')
    #         ser.write(command)
    #         print("Command sent successfully")
    #         count = 0
    
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

cap.release()
ser.close()
cv2.destroyAllWindows()
