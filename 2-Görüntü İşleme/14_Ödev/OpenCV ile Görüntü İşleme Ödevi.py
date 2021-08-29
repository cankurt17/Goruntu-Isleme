# opencv kütüphanesini içe aktaralım
import cv2

# matplotlib kütüphanesini içe aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("odev1.jpg",0)

# resmi çizdirelim
cv2.imshow("Odev resmi",img) 

# resmin boyutuna bakalım
print(img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
imgResized = cv2.resize(img,(int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
cv2.imshow("Resized",imgResized) 


# orijinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv2.putText(img,"Kopek",(400,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
cv2.imshow("Text",img)

img = cv2.imread("odev1.jpg",0)

# orijinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım, 
# binary threshold yöntemi kullanalım ve resmi çizdirelim 
_,thresh_img=cv2.threshold(img,thresh=50,maxval=255,type=cv2.THRESH_BINARY) 
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

# orijinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gb = cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7) 
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show() 

# orijinal resme Laplacian  gradyan uygulayalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_64F)
cv2.imshow("Laplacian",laplacian)


# orijinal resmin histogramını çizdirelim
img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])    
plt.figure()
plt.plot(img_hist) 
















