



import cv2
import matplotlib.pyplot as plt

def imageShow(image,name):
    plt.figure()
    plt.imshow(image,cmap="gray")
    plt.axis("off")
    plt.title(name)
    plt.show()
    
img = cv2.imread("sudoku.jpg",0)
imageShow(img, "Orijinal")

# x gradyan
sobelx = cv2.Sobel(img,ddepth = cv2.CV_16S, dx=1, dy=0, ksize=5)
imageShow(sobelx, "Sobel x")

# y gradyan
sobely = cv2.Sobel(img,ddepth = cv2.CV_16S, dx=0, dy=1, ksize=5)
imageShow(sobely, "Sobel x")

# laplacian gradyan
laplacian = cv2.Laplacian(img,ddepth = cv2.CV_16S)
imageShow(laplacian, "Laplacian")