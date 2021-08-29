

import glob
import os
import numpy as np
# keras derin öğrenme kütüphanesi
from keras.models import Sequential
# Dense: Katmanlar 
# Dropout: Seyreltme
# Flatten: Düzleştirme 
# Conv2D: Evrişim ağı
# MaxPooling2D: Piksel ekleme
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
# LabelEncoder: Verimizi etiketleyecek kütüphane 0,1,2,3
# OneHotEncoder: Etiketlenen verileri kerasta eğitilebilir hale getirir
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

imgs = glob.glob("./img_nihai/*.png")

width = 125
height = 50

X = []
Y = []

for img in imgs:
    
    filename = os.path.basename(img)
    label = filename.split("_")[0]
    im = np.array(Image.open(img).convert("L").resize((width,height)))
    im = im/255
    X.append(im)
    Y.append(label)

# train_test_split array kabul ettiği için resimleri arraye dönüştürüyoruz
X = np.array(X) 
# X.reshape(adet,width,height,channel(1=siyah-beyaz))
X = X.reshape(X.shape[0],width,height,1)

# sns.countplot(Y)

def onehot_labels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    onehot_encoded = OneHotEncoder(sparse = False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded),1)
    onehot_encoded = onehot_encoded.fit_transform(integer_encoded)
    
    return onehot_encoded

Y = onehot_labels(Y)

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size = 0.25, random_state = 2)

# cnn model
model = Sequential()

# Evrişim ağı
model.add(Conv2D(32, kernel_size = (3,3), activation = "relu", input_shape = (width,height,1)))
model.add(Conv2D(64, kernel_size = (3,3), activation = "relu" )) 
# Piksel ekleme
model.add(MaxPooling2D(pool_size = (2,2))) 
# Seyreltme
model.add(Dropout(0.25)) 
# Düzleştirme 
model.add(Flatten()) 
# Gizli layer ekleme
model.add(Dense(128,activation = "relu"))
model.add(Dropout(0.4))
# softmaxi ikiden fazla çıktı varsa kullanıyoruz
model.add(Dense(3,activation = "softmax"))

"""
if os.path.exists("./trex_weight.h5"):
    model.load_weights("trex.weight.h5")
    print("Weights yüklendi...")
"""

model.compile(loss = "categorical_crossentropy",optimizer = "Adam", metrics = ["accuracy"])

model.fit(train_X, train_Y, epochs = 35, batch_size = 64)

score_train = model.evaluate(train_X, train_Y)
print("Eğitim doğruluğu: %", score_train[1]*100)

score_test = model.evaluate(test_X, test_Y)
print("Test doğruluğu: %", score_test[1]*100)


open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.h5")



















