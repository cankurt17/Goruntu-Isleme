


import pandas as pd

# sözlük oluştur
dictonary = {"isim":["can","ibo","mcan","mustafa","ali","onur"],
             "yas":[20,21,22,23,24,25],
             "maas":[100,200,300,400,500,600]}
data = pd.DataFrame(dictonary)
print(data)


# ilk 5 satır
print(data.head())

# sutunlar
print(data.columns)

# veri bilgisi
print(data.info())

# istatislik özellikler
print(data.describe())

# yas sütunu
print(data["yas"])

# sutun eklemek
data["sehir"]=["Maras","Denizli","Ankara","Manisa","Manisa","Trabzon"]
print(data)

# yas sütunu
print(data.loc[:,"yas"])

# yas sütunu ve 3 satır
print(data.loc[:3,"yas"])

# yas ve sehir arası sütunu ve 3 satır
print(data.loc[:3,"yas":"sehir"])

# satırları tersten yazdır
print(data.loc[::-1,:])

# yas sutunu with iloc
print(data.iloc[:,1])

# ilk 3 satır yas ve isim
print(data.iloc[:2,[0,1]])

# filtreleme
 
dictonary = {"isim":["can","ibo","mcan","mustafa","ali","onur"],
             "yas":[20,21,22,23,24,25],
             "sehir":["Maras","Denizli","Maras","Manisa","Manisa","Maras"]}

data = pd.DataFrame(dictonary)
print(data)

# yasa gore filtreleme
filtre1= data.yas > 22
yeni_veri = data[filtre1]
print(yeni_veri)

# ortalama yas
ort_yas = data.yas.mean()

data["yas_grubu"] = ["buyuk" if ort_yas <= i else "kucuk" for i in data.yas]
print(data)
 
# birlestirme

dictonary1 = {"isim":["can","ibo","mcan","mustafa","ali","onur"],
             "yas":[20,21,22,23,24,25],
             "sehir":["Maras","Denizli","Maras","Manisa","Manisa","Maras"]}

data1 = pd.DataFrame(dictonary1)
 
dictonary2 = {"isim":["ufuk","halil"],
             "yas":[30,31],
             "sehir":["Ankara","İzmir"]}

data2 = pd.DataFrame(dictonary2)

# dikey 
veri_dikey = pd.concat([data1,data2],axis=0)


# yatay 
veri_yatay = pd.concat([data1,data2],axis=1)













