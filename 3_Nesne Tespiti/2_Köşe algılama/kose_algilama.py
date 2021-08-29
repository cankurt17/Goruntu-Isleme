



import cv2
import matplotlib.pyplot as plt
import numpy as np


def imageShow(image):
    plt.figure()
    plt.imshow(image,cmap="gray")
    plt.axis("off")
    #plt.imshow()
    
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
print(img.shape)
imageShow(img)

# harris corner detection köşe algılama
# (fotoğraf,komşuluk mesafesi,pencere boyutu,serbest değer)
dst = cv2.cornerHarris(img,blockSize =2, ksize=3,k=0.04)
imageShow(dst)

dst = cv2.dilate(dst,None) 
img[dst>0.2*dst.max()] = 1
imageShow(dst)

# shi tomasi detection    
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)
# (img,bulunacak köşe sayısı,kalite,iki köşe arasındaki min mesafe)
corners = cv2.goodFeaturesToTrack(img,120,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel() # düzleştirme
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)

imageShow(img)













