# 1-100e kadar

# x=1
# while x <= 100:
#     if x % 2 ==0:
#         print(x)
#     x += 1

# print('bitti...')

# name = '' #False
# while not name.strip(): #bilgi girilmedikce tekrar 
#     name = input('Adinizi giriniz: ')
# print('Merhaba',name)
    
#########################while-samples#################################
from hashlib import new


sayilar = [1,3,5,7,9,12,19,21]
# 1- Sayilari tek tek while ile ekrana yazdir
# i=0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

# 2- Baslangic ve bitis degerlerini kullanicidan 
#                   alip tek sayilari ekrana yazdir
# start = int(input('Baslangic degeri giriniz: '))
# finish = int(input('Bitis degeri giriniz:'))
# if start <= finish:
#     while start <= finish:
#         if start % 2 == 1:
#             print(start)
#         start +=1
# else:
#     print('Baslangic degeri bitis degerinden büyük olamaz.')    

# 3- Kullanicidan alacaginiz 5 sayiyi ekranda sirali bir sekilde yazdirin.
# newList = []
# x = 0
# while x < 5:
#     numb = int(input('sayi giriniz'))
#     newList.append(numb)
#     x += 1
# print(newList)

# 4- Kullanicidan sinirsiz urun bilgisi alarak urunler listesinde saklayin
#       **urun sayisini kullanicidan alin
#       **dictionary(name,price) seklinde 
#       **urun ekleme bittiginde while ile yazdirin
sayi = int(input('Urun sayisini giriniz:'))
urunler = []
i = 0
while i < sayi:
    name = input('ürün ismi:')
    price = input('ürün fiyati: ')
    urunler.append({
        'name':name,
        'price':price
    })
    i += 1
for urun in urunler:
    print(f'ürün adi: {urun["name"]} ürün fiyati: {urun["price"]} ')
    