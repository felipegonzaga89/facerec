import cv2, os

cap = cv2.VideoCapture(0)
while(not cv2.waitKey(20) & 0xFF == ord('q')):
    s, frame = cap.read()
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(5)
