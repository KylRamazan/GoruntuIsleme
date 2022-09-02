import os,glob,consts
from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array

def ResimCogaltma():
    # Resim Çoğaltma
    '''
        ImageDataGenerator sınıfı ile çoğaltma işleminin özellikleri belirleniyor.
        --- rotation_range: döndürme açısı
        --- width_shift_range: genişlik kaydırma aralığı (resmin 5'te birine kadar yanlardan kesebilir)
        --- height_shift_range: yükseklik kaydırma aralığı (resmin 5'te birine kadar yukarıdan kesebilir)
        --- shear_range: kesme aralığı (resmin 5'te birine kadar kesebilir)
        --- zoom_range: yakınlaştırma aralığı (resmi 5'te bir oranda büyütebilir)
        --- horizontal_flip: yatay çevirme (resmi yatay eksende döndürme)
        --- vertical_flip: dikey çevirme (resmi dikey eksende döndürme)
    '''
    datagen=ImageDataGenerator(rotation_range=20,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,vertical_flip=True,fill_mode='nearest')
    for dir in glob.glob(os.path.join(consts.resim_yolu,'*')): # resimlerin olduğu klasörün içindeki tüm klasörleri alma
        karakter=os.path.basename(dir)          # resimlerin olduğu klasörün adı (bisiklet/motor)
        kayit_klasoru=os.path.join(consts.klasor,'Resimler',karakter) # resimlerin kendi sınıfına göre kaydedileceği klasörün belirlenmesi
        if(os.path.exists(kayit_klasoru)==False): # belirlenen klasör yoksa oluşturma
            os.mkdir(kayit_klasoru)
        for dosya in glob.glob(os.path.join(dir,'*')): # klasör içindeki tüm resimleri bulma
            if os.path.isfile(dosya):
                dosyaadi,uzanti=os.path.splitext(dosya) # dosyanın adı ve uzantısını ayırma
                x=img_to_array(load_img(dosya)) # resmi piksellerine ayırma (0-255 aralığında olan matrislere çevirme)
                x=x.reshape((1,)+x.shape) # resmi yeniden boyutlandırma
                i=0
                '''
                    resim çoğaltmanın yapıldığı yer.
                    --- x: yeniden boyutlandırılmış resim matrisi
                    --- save_to_dir: oluşturulan resmin kaydedileceği klasör
                    --- save_format: oluşturulan resmin uzantısı
                '''
                for batch in datagen.flow(x,batch_size=1,save_to_dir=kayit_klasoru,save_format='png'):
                    i+=1
                    if i==20:
                        break