# -*- coding: utf-8 -*-
"""

1) Veri seti oluşturulur:
    negatif : herhangibir şey   
    pozitif : tespit edilecek obje

2) Cascade programı indir
3) Cascade
4) Cascade kullanılarak tespit algoritması yaz

"""

import cv2
import os


# resim depo klasörü
path = "images"

# resim boyutu
imgWidth = 180
imgHeight = 120

# video capture
cap = cv2.VideoCapture(0)
# kamera pikseli
cap.set(3,640)
cap.set(4,480)
# kamera parlaklığı
cap.set(10,180)

global countFolder

def saveDataFunc():
    global countFolder
    countFolder = 0
    
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    
    os.makedirs(path + str(countFolder))

saveDataFunc()

count = 0
countSave = 0

while True:
    
    succes, img = cap.read()
    
    if succes:
        img = cv2.resize(img,(imgWidth,imgHeight))
        if count % 5 == 0:
            cv2.imwrite(path+str(countFolder)+"/"+str(countSave)+"_"+".png",img)
            countSave +=1
            print(countSave)
        count += 1
        
        cv2.imshow("Image",img)
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()















