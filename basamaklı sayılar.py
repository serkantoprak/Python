liste=[]

sayi=1000000000000000000000
toplam=0

while sayi < 10000000000000000000000:
    for rakam in str(sayi):
        toplam +=int(rakam)
    if toplam ==99:
        liste.append(sayi)
    sayi+=1
    toplam=0
print(f"rakamlar toplamı 99 olan, {len(liste)}adet, 22 basamaklı sayı vardır")
print(liste)
