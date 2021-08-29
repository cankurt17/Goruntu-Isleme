import numpy as np

# 1*15 array-dizi
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) 
print(dizi)

# array in boyutu
print(dizi.shape)

dizi2 = dizi.reshape(3,5)
print("Şekil: ",dizi2.shape)
print("Boyut: ",dizi2.ndim)
print("Veri Tipi: ",dizi2.dtype.name)
print("Boy: ",dizi2.size)

# array type
print("Type: ",type(dizi2))

# 2 boyutlu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

# 0 lardan olusan array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

# 1 lardan olusan array
bir_dizi = np.ones((3,4))
print(bir_dizi)

# bos array
bos_dizi = np.empty((3,4))
print(bos_dizi)

# arange(x,y,basamak)
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)
 

# matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6]) 

print(a+b)
print(a-b)
print(a**2)

# dizi elamanı toplama 
print(np.sum(a))

# max deger
print(np.max(a))

# min deger 
print(np.min(a))

# mean ortalama
print(np.mean(a))

#median ortalama
print(np.median(a))

# rastgele sayi üretme [0,1] arasında sürekli uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# indeks
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])
print(dizi[0:4])

#dizinin tersi
print(dizi[::-1])

#
dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# 1. satır 1. sutun
print(dizi2D[1,1])

# 1.sütun ve tüm satırlar
print(dizi2D[:,1])

# satır 1 ,sütun 1,2,3
print(dizi2D[1,1:4])


# sonm satır tüm sutunlar
print(dizi2D[-1,:])

#
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

# vektor haline getirme
vektor = dizi2D.ravel() 
print(vektor)

# max sayının indeksi
max_index = vektor.argmax()
print(max_index)
























