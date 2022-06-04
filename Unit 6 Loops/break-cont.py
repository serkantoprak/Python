# name = 'Serkan Toprak'

# for letter in name:
#     if letter == 'a':
#         continue
#     print(letter)

# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

# 1-100 arasındaki çift sayıları toplama

x = 0
res = 0
while x <= 100:
    x += 1
    if x%2 == 1:
        continue
    res += x
print("Sonuç:",res)
    