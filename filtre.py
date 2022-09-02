import random,os,cv2,glob,consts
from Filtreler import bilateral,gaussian,gray,median,unsharp

# Filtre Uygulama
def FiltreUygula():
    for dir in glob.glob(os.path.join(consts.resim_yolu,'*')):  # Resimler klasöründeki tüm klasör ve dosyaları listeleme
        for file in glob.glob(os.path.join(dir,'*')):           # Resimler klasöründeki klasörlerin içindeki dosya ve klasörleri listeleme
            if os.path.isfile(file):
                dosya_adi,uzanti=os.path.splitext(file)         # Dosyaların ad ve uzantısını bulma
                rand=random.randrange(1,6)                      # 1-7 arası rastgele sayı üretme
                if rand==1:
                    cv2.imwrite('{0}_bilateral{1}'.format(dosya_adi,uzanti),bilateral.BilateralFilter(file))
                elif rand==2:
                    cv2.imwrite('{0}_gaussian{1}'.format(dosya_adi,uzanti),gaussian.GaussianFilter(file))
                elif rand==3:
                    cv2.imwrite('{0}_gray{1}'.format(dosya_adi,uzanti),gray.Gray(file))
                elif rand==4:
                    cv2.imwrite('{0}_median{1}'.format(dosya_adi,uzanti),median.MedianFilter(file))
                elif rand==5:
                    cv2.imwrite('{0}_unsharp{1}'.format(dosya_adi,uzanti),unsharp.UnsharpFilter(file))
                else:
                    pass
            '''
                Rastgele üretilen sayı
                    1 ise bilateral filtresini uygular,
                    2 ise gaussian filtresini uygular,
                    3 ise gray filtresini uygular,
                    4 ise ise median filtresini uygular,
                    5 ise resmin parlaklığını düşürür yada arttırır,
                    6 ise unsharp  filtresini uygular.
            '''