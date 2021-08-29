



import cv2
import matplotlib.pyplot as plt
import numpy as np


def imageShow(image):
    plt.figure()  
    plt.axis("off")
    plt.imshow(image,cmap = "gray")
    
coin = cv2.imread("coins.jpg")
imageShow(coin)

# lpf: bluring
coin_blur = cv2.medianBlur(coin,13)
imageShow(coin_blur)

# grayscale
coin_gray = cv2.cvtColor(coin_blur,cv2.COLOR_BGR2GRAY)
imageShow(coin_gray)

# binary threshold
res, coin_thresh = cv2.threshold(coin_gray,75,255,cv2.THRESH_BINARY)
imageShow(coin_thresh)

# kontur
contours, hierarchy = cv2.findContours(coin_thresh.copy(),cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin,contours,i,(0,255,0),10)

imageShow(coin)



# watershed
    
coin = cv2.imread("coins.jpg")
imageShow(coin)

# lpf: bluring
coin_blur = cv2.medianBlur(coin,13)
imageShow(coin_blur) 

# grayscale
coin_gray = cv2.cvtColor(coin_blur,cv2.COLOR_BGR2GRAY)
imageShow(coin_gray)

# binary threshold
res, coin_thresh = cv2.threshold(coin_gray,65,255,cv2.THRESH_BINARY)
imageShow(coin_thresh)

# açılma
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN,kernel,iterations =2)
imageShow(opening)

# nesneler arası distance
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
imageShow(dist_transform)

# resmi küçült 
ret, sure_foregraund = cv2.threshold(dist_transform,0.4*np.max(dist_transform),255,0)
imageShow(sure_foregraund)

# arka plan için resmi büyült
sure_backgraund = cv2.dilate(opening,kernel,iterations=1)
sure_foregraund = np.uint8(sure_foregraund)
unknown = cv2.subtract(sure_backgraund,sure_foregraund) 
imageShow(unknown)

# bağlantı
ret, marker = cv2.connectedComponents(sure_foregraund)
marker = marker + 1
marker[unknown == 255] = 0
imageShow(marker)

marker = cv2.watershed(coin,marker)
imageShow(marker)


# kontur
contours, hierarchy = cv2.findContours(marker.copy(),cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin,contours,i,(255,0,0),10)

imageShow(coin)
























