



import cv2
import matplotlib.pyplot as plt


def imageShow(image):
    plt.figure()  
    plt.axis("off")
    plt.imshow(image,cmap = "gray")
    
einstein = cv2.imread("einstein.jpg",0)
imageShow(einstein)

# Sınıflandırma
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    
    cv2.rectangle(einstein,(x,y),(x+w,y+h),(255,255,255),10)
    
imageShow(einstein)

# //////////////////////////////////////////////////

barcelona = cv2.imread("barcelona.jpg",0)
imageShow(barcelona)

# minNeighbors değeri yanlış sonuçları bulamsını önler (örn: 7 komşusuda yüzü tanıyorsa tanımlar)
face_rect = face_cascade.detectMultiScale(barcelona, minNeighbors = 7)


for (x,y,w,h) in face_rect: 
    cv2.rectangle(barcelona,(x,y),(x+w,y+h),(255,255,255),10)
    
imageShow(barcelona)


# video 
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    if ret:
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
        for (x,y,w,h) in face_rect: 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),10)
        cv2.imshow("face detect",frame)
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    











