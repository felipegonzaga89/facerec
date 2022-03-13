import cv2
import os
import face_recognition
from PIL import Image


cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:
    face_1_image = face_recognition.load_image_file('/home/felipe/Desktop/Django/Teste facerec/fotos/3.jpeg')
    face_1_face_encoding =  face_recognition.face_encodings(face_1_image)[0]

    small_frame = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
   
    
    rgb_small_frame = small_frame[:,:,::-1]
    
   # while True:
    #    cv2.imshow('Rosto na Camera', small_frame)
     #   if cv2.waitKey(5) == 27:
      #      break
   # cv2.imwrite("fotos/filename.jpg",img)


    cam.release()


    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(img)

    check=face_recognition.compare_faces(face_1_face_encoding, face_encodings)
            
    
print(check)






#xml_path = ('/Users/marce/Desktop/Django/Teste facerec/face_rec/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
#clf = cv2.CascadeClassifier(xml_path)
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#faces = clf.detectMultiScale(gray)