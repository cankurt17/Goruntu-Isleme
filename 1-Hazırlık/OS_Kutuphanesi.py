 
import os

print(os.name)

currentDir = os.getcwd()
print(currentDir)

# new folder
folder_name = "new_folder"
os.mkdir(folder_name)

# dosya ismi değiştir
folder_name2 = "new_folder2"
os.rename(folder_name, folder_name2)

# yeni dizine geç
os.chdir(currentDir+"\\"+folder_name2) 
os.chdir(currentDir) 
 
# mevcut dizindeki dosyaları çeker
files = os.listdir()

# py uzantılı dosyalar
for f in files:
    if f.endswith(".py"):
        print(f)
        
# dosya silme
os.rmdir(folder_name2)

# dizinde dosyaları çekme
for i in os.walk(currentDir):
    print(i)

# dosya kontrolü
os.path.exists("numpy.py")

    
