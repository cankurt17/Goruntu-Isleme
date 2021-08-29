



import cv2
import matplotlib.pyplot as plt
import numpy as np


def imageShow(image):
    plt.figure()
    plt.imshow(image,cmap="gray")
    plt.axis("off")
    #plt.imshow()
    
img = cv2.imread("london.jpg",0)
imageShow(img)

edges = cv2.Canny(image=img,threshold1=0,threshold2=255)
imageShow(edges) 

med_val = np.median(img)
print(med_val)

# Genelde kullanılan max ve min threshold hesabı
low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image=img,threshold1=low,threshold2=high)
imageShow(edges) 

# blur
blurred_img=cv2.blur(img,ksize=(5,5))
imageShow(blurred_img)
 
med_val = np.median(blurred_img)
print(med_val)

# Genelde kullanılan max ve min threshold hesabı
low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image=blurred_img,threshold1=low,threshold2=high)
imageShow(edges) 









