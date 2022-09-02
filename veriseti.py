import os,platform,consts,shutil,numpy,kontrol,pathlib
from sklearn.model_selection import train_test_split

def VerisetiOlustur():
    kontrol.kontrol_et()                                # consts dosyasındaki dosya yolları yoksa oluşturur.
    if os.path.exists(consts.resim_yolu) is False:
        print('Resimleri Masaüstündeki "Resimler" Klasörü İçine Koymanız Gerekmektedir !')  
        return -1
    klasorler=os.listdir(consts.resim_yolu)             # resim_yolu (masaüstündeki Resimler klasörü) içindeki tüm dosya ve klasörleri listeler
    if len(klasorler)==0:
        print('Resimleri Masaüstündeki "Resimler" Klasörü İçine Koymanız Gerekmektedir !')  
        return -1
    for dir in klasorler:
        classes=os.path.join(consts.resim_yolu,dir)
        dizi=numpy.array([os.path.join(classes,file) for file in os.listdir(classes)])
        train,validation=train_test_split(dizi,train_size=.7)
        for file in train:
            dizi=file.split('\\' if platform.system().lower()=='windows' else '/')
            kayit_yolu=os.path.join(consts.egitim_yolu,dizi[-2])
            if os.path.exists(kayit_yolu) is False:os.mkdir(kayit_yolu)
            yeni=os.path.join(kayit_yolu,dizi[-1])
            shutil.move(file,yeni)
        for file in validation:
            dizi=file.split('\\' if platform.system().lower()=='windows' else '/')
            kayit_yolu=os.path.join(consts.validation_yolu,dizi[-2])
            if os.path.exists(kayit_yolu) is False:os.mkdir(kayit_yolu)
            yeni=os.path.join(kayit_yolu,dizi[-1])
            shutil.move(file,yeni)

'''
    Masaüstündeki Resimler klasörü içindeki tüm resimleri alıp rastgele %70'ini eğitim, kalan %30'unu test olarak ayırıp
    eğitim için olanları Masaüstü > Veriseti > train klasörü içine,
    test için olanları Masaüstü > Veriseti > validation klasörü içine taşır.
'''