from email import message
from operator import index
from textwrap import indent
message = '  hello there. I am Serkan Toprak'

# message = message.upper() #tüm harfler büyük
# message = message.lower() #tüm harfler küçük
# message = message.title() #sadece kelimelerin ilk harfleri büyük
# message = message.capitalize() #sadece ilk harf büyük
# message = message.strip() #baştaki boşlukları siler
# message = message.split() #mesajı boşluklardan ayırır/kelimelere
# message = message.split('.') #mesajı noktalardan ayırır/cümlelere
# message = '//'.join(message) #ayrılan elemanların arasına belirlenen stringi ekler
# index = message.find('Serkan') #mesaj içinde kelime arama
# print(index) #index sayısını yazdırma
# isFound = message.startswith(' ') #bu harfle mi başlıyor?
# isFound = message.endswith('k') #bu harfle mi bitiyor?
# message = message.replace('there','everyone') #kelimenin yerini değiştirme
# message = message.center(50) #50 karakter içersine ortala(web vb uygulamalarda)

print(message)
# print(message[4]) #mesajdaki i. elemanı gösterir