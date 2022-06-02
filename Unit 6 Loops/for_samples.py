sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayilar 3un katidir
# for a in sayilar:
#     if a%3==0:
#         print(a,'3un kati')

# 2- Sayilar listesindeki sayilarin toplami kactir
# x=0
# for b in sayilar:
#     x += b
# print(x)

# 3- Sayilar listesindeki tek sayilarin karesini aliniz
# for c in sayilar:
#     if c%2 == 1:
#         c=c*c
#         print(c)

sehirler = ['kocaeli','istanbul','ankara','izmir','bursa']

# 4- Sehirlerin hangileri en fazla 5 karakterlidir
# tot = 0
# for sehir in sehirler:
#     if len(sehir) <= 5:
#         tot += 1
#         print(sehir)
# print(tot)

urunler = [
    {'name':'samsung s6','price':3000},
    {'name':'samsung s7','price':4000},
    {'name':'samsung s8','price':5000},
    {'name':'samsung s9','price':6000},
    {'name':'samsung s10','price':7000}
]

# 5- Urunlerin fiyatlari toplami nedir
# total = 0
# for urun in urunler:
#     fiyat = int(urun['price'])
#     total += fiyat
# print(total)

# 6- Urunlerden fiyati en fazla 5000 olan urunleri gosteriniz
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])