#amaç: farklı listeler kullanmak yerine tek dictionary ile veri elde etmek

from pydoc import plain


# plakalar = {'kocaeli': 41,'istanbul': 34,'izmir': 35,'ankara': 6 }
# print(plakalar['izmir']) #izmir'e karşılık gelen değer

# plakalar['mersin'] = 33 #yeni eleman ekleme
# plakalar['izmir'] = 'gevrek'
# print(plakalar)

# users = {
#     'serkantoprak' : {
#         'age':24,
#         'email':'serkan.toprakk8@gmail.com',
#         'adress':'izmit',
#         'phone':'+90 555 555 5555'
#     }
# }

# print(users['serkantoprak']['email'])
numbers = {}
print("no:",numbers)

numbers.update( #toplu veri güncellemek için
    {
        number: {
            'ad':name,
            'soyad':surname,
            'telefon':phone 
        }
    }
)