



import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def imageShow(image,name):
    plt.figure()
    plt.imshow(image)
    plt.axis("off")
    plt.title(name)
    plt.show()

# blurring (detayı azaltır ve gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imageShow(img,"Orijinal")

 
# Ortalama bulanıklaştırma yöntemi 
dst2 = cv2.blur(img,ksize=(3,3))
imageShow(dst2,"Ortalama blur") 

 
# gaussian blur 
gb = cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
imageShow(gb,"Gaussian blur")
 
# Medyan blur 
mb = cv2.medianBlur(img,ksize = 3) 
imageShow(mb,"Medyan blur")


def gaussianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy


# içe aktar ve normalize et 0-255 değer aralığını 0-1 aralık formatına donustur
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
imageShow(img,"Orijinal") 

gaussianNoisyImage = gaussianNoise(img)
imageShow(gaussianNoisyImage, "Gaussian Noisy") 

# gaus blur 
gb2 = cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7) 
imageShow(gb2, "With gaussian blur")


# Tuz biber gürültüsü
def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # salt beyaz Tuz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    # salt beyaz Tuz
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    coords = [np.random.randint(0,i-1,int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
imageShow(spImage, "SP Image")
 
# Medyan blur 
mb2 = cv2.medianBlur(spImage.astype(np.float32),ksize = 3) 
imageShow(mb,"with Medyan blur")






























