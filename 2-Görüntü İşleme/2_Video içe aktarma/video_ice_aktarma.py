


import cv2
import time

# video ismi 
video_name = "cam.mp4"

# video içe aktar: capture cap
cap = cv2.VideoCapture(video_name)

if cap.isOpened() == False:
    print("Video açılamıyor")
    
print("Genişlik:",cap.get(3))
print("Yükseklik:",cap.get(4)) 


while True:
    ret,frame = cap.read()
    if ret == True:
        time.sleep(0.01) # kullanmazsak çok hızlı akar
        cv2.imshow("Video",frame)
    else:
        break
    
    if cv2.waitKey(1) &0xFF == ord("q"):
        break

cap.release() # stop capture(video)
cv2.destroyAllWindows(q)