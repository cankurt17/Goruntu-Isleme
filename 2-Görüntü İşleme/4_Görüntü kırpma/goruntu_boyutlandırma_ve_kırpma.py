


import cv2

# 
img = cv2.imread("lenna.png")
print("Resim boyutu",img.shape) 
cv2.imshow("Orjinal",img)

# resized
imgResized = cv2.resize(img,(700,700)) 
print("Resized Img Shape",imgResized.shape)
cv2.imshow("Img Resized",imgResized)

# kırp
imgCropped = img[:200,:300] # (height,width)
cv2.imshow("Cropped",imgCropped)

