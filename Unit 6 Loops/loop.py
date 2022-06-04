#   -----RANGE-----
# 
# for item in range(10):
#     print(item,end='-')

# for item in range(2,22):
#     print(item,end='-')


# for item in range(2,22,2):
#     print(item,end='-')
# print(list(range(2,22,2)))

#   -----ENUMARATE-----

# greeting = 'Hello!'

# # for index,letter in enumerate(greeting):
# #     print('index:',index,'letter:',letter)
    
# for item in enumerate(greeting): #stringe ait indexi ve harfi verir
#     print(item)

#   -----ZIP-----

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# # print(list(zip(list1,list2)))

# for item in zip(list1,list2):
#     print(item)

# for a,b in zip(list1,list2):
#     print(a,b)

#   -----LIST COMPREHENSIONS-----

# numberss = []       #Uzun yöntemle
# for x in range(12):
#     numberss.append(-x**2) #her x için (-x^2) yaz
# print(numberss)

# number = [-x**2 for x in range(12)] #kısa yöntemle
# print(number)

#---------------------------
# numm = [x*x for x in range(10) if x%3==0] 
# # her x değeri için eğer 3ün katıysa karesini al ve dizi oluştur
# print(numm)

#---------------------------
# myString = 'Hello'
# myList = [letter for letter in myString]
# print(myList)

#---------------------------
# years = [1985,1977,1973,1968,1998,1995]
# ages = [2022-year for year in years]
# print(ages)

#---------------------------
# results = [x if x%2==0 else 'TEK' for x in range(1,10)]
# print(results)

#---------------------------
# numbers = [(x,y) for x in range(3) for y in range(3)]
# print(numbers)

