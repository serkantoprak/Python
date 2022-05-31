from traceback import print_stack


numbers = [1,10,8,3,34,2,8]
letters = ['v','t','y','r','a','u','p','p','p']

val = min(numbers)
val = max(numbers)
val = min(letters) #harflerin sayısal değerlerine göre
val = max(letters)
val = numbers[3:6] #3. elemandan 6.elemana kadar yazdırma
# print(val)
numbers[0] = 17 #0. elemana yeni değer atama
numbers.append(60) #yeni değer ekleme *dizinin sonuna*
numbers.insert(2,3) #2. elemana 3 değerini ekleme
numbers.insert(-1,55) #-1.elemana 55 değerini ekleme
numbers.pop(3) #3.elemanı sil
numbers.remove(8) #8 değerini bul ve sil
numbers.sort() #elemanları sıralar
letters.sort() 
numbers.reverse() #elemanları tersten sıralar
letters.reverse()
# numbers.clear() #tüm elemanları temizler

print(numbers)
print(letters)
print(numbers.count(3)) #içerisinde kaç tane 3 var
print(letters.count('p'))
