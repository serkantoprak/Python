#  1-Ad,yaş ve eğtiim bilgisiyle ehliyet alabilme kontrolü
#    en az 18 yaş ve lise/üniversite eğitimine sahip

# adi  = input('Adınız: ')
# yasi = int(input('Yasiniz: '))
# egitim = input('Eğitim Durumunuz: ')

# if yasi>18:
#     if egitim == 'lise' or egitim == 'üniversite':
#         print('Sayin',adi,'Ehliyet alabilirsiniz...')
#     else:
#         print('Sayin',adi,'Eğitim durumunuzdan dolayı ehliyet almaya uygun değilsiniz...')
# else:
#     print('Sayin',adi,'Yaşınız 18den küçük olduğundan ehliyet alamazsınız...')

# 2- Trafiğe çıkış tarihi alınan bir aracın servis zamanını 
#     aşağıdaki bilgilere göre hesaplayınız.
#     1.bakım --> 1.yıl
#     2.bakım --> 3.yıl 
#     3.bakım --> 5.yıl 

import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı(YYYY/AA/GG)')
tarih = tarih.split('/') #gün ay ve yıl için ayırma
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
gun = fark.days #sadece günleri alabilmek için .days komutu

if gun >= 5*365: #5 yıldan fazlaysa
    print('Aracınızın 3. Bakım zamanı gelmiştir...')
elif gun >= 3*365: #3 yıldan fazlaysa
    print('Aracınızın 2. Bakım zamanı gelmiştir...')
elif gun >= 1*365: #1 yıldan fazlaysa
    print('Aracınızın 1. Bakım zamanı gelmiştir...')
else:
    print('Aracınızın rutin bakıma ihtiyacı yoktur.')