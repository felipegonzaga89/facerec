import face_recognition
import cv2

known_image = face_recognition.load_image_file("/home/felipe/Desktop/Django/Teste facerec/fotos/13.jpg")
unknown_image = face_recognition.load_image_file("/home/felipe/Desktop/Django/Teste facerec/fotos/10.jpg")

know_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([know_encoding], unknown_encoding)


print(know_encoding)
print(unknown_encoding)
print(results)