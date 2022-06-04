# import random

# sayi = random.randint(1,10)
# can = int(input('Kaç hak olmalı: '))
# hak = can
# sayac = 0

# while hak > 0:
#     hak -= 1
#     sayac += 1
#     tahmin = int(input('Tahmininiz:'))
#     if sayi == tahmin:
#         print(sayac,'. denemede bildiniz. Toplam puanınız:',100-(100/can)*(sayac-1))
#         break
#     elif sayi > tahmin:
#         print('Yukari')
#     else:
#         print('Asagi')
#     if hak == 0:
#         print('Hakkiniz bitti. Tutulan sayı:',sayi) 

#-----------------------------------------------------------
sayi = int(input('Bir sayi giriniz: '))
asalmi = True

if sayi == 1: 
    asalmi = False

for i in range(2,sayi):
    if sayi%i == 0:
        asalmi = False
        break

if asalmi:
    print(sayi,'sayısı asaldır')
else:
    print(sayi,'sayısı asal değildir')