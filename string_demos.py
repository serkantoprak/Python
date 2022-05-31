from unittest import result


website = "www.serkantoprak.com"
course = "Bastan sona Python Kursu"

# 1- ' Hello World ' baştaki ve sondaki boşluğu silme

result = ' Hello World '.strip()

# 2- 'www.serkantoprak.com' içindeki serkantoprak haricindeki tüm karakterleri silme

result = website.lstrip('www.').rstrip('.com')

#3 course tüm harfleri küçük yapma

result = course.lower()

#4 'website' içinde kaç tane a harfi var

result = website.count('a')

#5 website www ile başlayıp com ile bitiyor mu?

result  = website.startswith('www')
result = website.endswith('com')

#6 website içinde .com var mı
result = website.find('.com')

#7 course içerisindeki karakterlerin hepsi alfabetik mi?
result = course.isdigit()
result = course.isalpha()

#8 contents ifadesini 50 karakterin ortasına yerleştir ve * koy

result = 'Contents'.center(50,'*')

#9 course içerisindeki tüm boşlukları - ile değiştirme

result = course.replace(' ','-')

#10 'Hello World' world yerine there koy

result = 'Hello World'.replace('World','There')

#11 course mesajını boşluklardan ayırma

result = course.split()

print(result)