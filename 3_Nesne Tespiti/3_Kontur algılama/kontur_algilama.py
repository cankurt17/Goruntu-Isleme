



import cv2
import matplotlib.pyplot as plt
import numpy as np

def imageShow(image):
    plt.figure()
    plt.imshow(image,cmap="gray")
    plt.axis("off")
    #plt.imshow()
    
img = cv2.imread("contour.jpg",0)
imageShow(img)

# kontur = resimde figürelerin sınırlarını belli eden çizgi
# (img,iç ve dış konturları belirler, yatay dikey ve çapraz bölümleri sıkıştırarak yalnızca uç noktalarıo bırakır)
contours,hierarch = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape) 

for i in range(len(contours)): 
    # external
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour,contours,i,0.2,-1) # 255 renk -1 kalınlık(konturlarla sınırlı alanı doldur anlamına gelir)
    else: # internal
        cv2.drawContours(internal_contour,contours,i,255,-1) 

imageShow(external_contour)
imageShow(internal_contour)