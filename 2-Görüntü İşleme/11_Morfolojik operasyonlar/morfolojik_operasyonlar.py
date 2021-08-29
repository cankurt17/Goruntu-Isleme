


"""

 Erezyon : Ön plandaki nesnein sınırlarını aşındırır
 Genişleme : Görüntüdeki beyaz bölgeyi arttırır sınırları genişletir
 Açma : Erezyon + Genişleme Ardarda uygulanır beyaz gürültünün giderilmesinde faydalıdır
 Kapatma : Genişleme + Erezyon ön plandaki nesnede küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır
 Morfolojik gradyan : Görüntünün genişlemesi ve erezyon arasındaki farktır
 
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np


def imageShow(image,name):
    plt.figure()
    plt.imshow(image,cmap="gray")
    plt.axis("off")
    plt.title(name)
    plt.show()
    
img = cv2.imread("datai_team.jpg",0)
imageShow(img,"Orijinal")

# Erezyon
kernel = np.ones((5,5),dtype = np.uint8)
result = cv2.erode(img,kernel,iterations = 1)
imageShow(result,"Erezyon")

# Genişleme dilation
result2 = cv2.dilate(img,kernel,iterations=1)
imageShow(result2, "Genisleme")

# white noise - beyaz gürültü
whiteNoise = np.random.randint(0,2,size=img.shape[:2])
whiteNoise = whiteNoise*255
imageShow(whiteNoise, "White noise")

noise_img = whiteNoise + img
imageShow(noise_img,"Img white noise" )

# Açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
imageShow(opening, "Acilma")


# black noise - siyah gürültü
blackNoise = np.random.randint(0,2,size=img.shape[:2])
blackNoise = blackNoise*-255
imageShow(whiteNoise, "Black noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
imageShow(black_noise_img, "Black noise image")
 
# Kapatma
clossing = cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
imageShow(clossing, "Kapama")


gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
imageShow(gradient, "Gradyan")






















