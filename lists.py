from cgitb import reset
import numbers
from unittest import result


# list1 = ['one','two','three']
# list2 = ['four','five','six','seven']

# numbers = list1 + list2
# print(numbers)
# print(len(numbers)) #dizi uzunluğu
# print(numbers[3]) #dizinin i. elemanı

# userA = ['Serkan Toprak',24]
# userB = ['Necmettin Toprak',27]
# users = userA + userB #çıktısı //['Serkan Toprak', 24, 'Necmettin Toprak', 27] 
# userslist = [userA,userB] #çıktısı liste içinde liste //[['Serkan Toprak', 24], ['Necmettin Toprak', 27]]
# print(users,'\n', userslist)

################################################

#1-"BMW,Mercedes,Opel,Mazda" ile dizi oluştur
otomobil = ['BMW','Mercedes','Opel','Mazda']
print(otomobil)
#2-Liste kaç elemanlı 
print(len(otomobil))
#3-Listenin ilk ve son elemanı
print(otomobil[0],otomobil[3]) #sonuncu eleman için [-1] kullanılabilir
#4- Mazda verisini Toyota ile değiştirin
otomobil[-1] = 'Toyota'
print(otomobil)
#5- Mercedes listenin bir elemanı mıdır
result = 'Mercedes' in otomobil
#6- Listenin ilk 3 elemanı
result = otomobil[0:3]
result = otomobil[:3]
result = otomobil[-2:]
#7- listeye "Audi" ve "Porshce" ekle
result = otomobil + ['Audi','Porsche']
#8- listenin ilk elemanını sil
del otomobil[0]
result = otomobil
#9- listeyi tersten yazdır
result = otomobil[::-1]

print(result)
