#identity operator: is

# x = y = [1,2,3]
# z = [1,2,3]

# print(x==y) #liste karşılaştırması 
# print(x==z) #içerik ve değer karşılaştırması

# x= [1,2,3]
# y=[2,4]
# del x[2]
# y[1]=1
# y.reverse()

# print(x==y) #elemanlar aynı
# print(x is y) #kimlik farklı
# print(x is not y) #değil mi
# print(x is z) #objeler aynı değilse false/içerikten bağımsız

##Membership operator: in

x = ['apple','banana']
print('banana' in x)
print('ana' not in x)