# Mavzu : Funksiyalar 

# a = abs (-5) # ->5 
# print(a) 
# b = round (3.1655, 1) # ->3,14
# print(b)
# d = pow(4, 0,5) # ->8
# print(d)
# print(5**0.5)



# max funksiyasi
# a = max([2,3,4,5,90])
# print(a)
# b = max(39,49,32)
# print(b)

# c = max("a","bc","absf","w")
# print(c)

# Mavzuga amaliy yondoshish
# dixtagi keylarning ichidan eng katta elementni aniqlash
# keylar intda bolingaligi uchun 20 qaytishi kerak 
# sonlar4 = {-2:"minus ikki",10:"o'n",20:"yigirma",3:"uch",4:"tort"}
# print(max(sonlar4))

# a = max(sonlar4.items())
# print(a[1])

# dictagi eng uzun valuega ega juftlikni key va valueni aniqlash
# print(max(sonlar4.items(),key= lambda y : len(y[1])))

# y = (key,value)






# Topshiriq 
# eng uzun nomga ega davlatraning poytaxtini chiqaring 
davlatlar = {"Toshkent":"Uzbekiston","Ostana":"Qozogiston","Seul":"Janubiy Koreya"}
b = max(davlatlar.items(),key= lambda y:len(y[1]))
print(b[0])


# eng uzun nomga ega bolgan poytaxtni chiqaring 
poytaxt = {"Toshkent":"Uzbekiston","Ostana":"Qozogiston","Seul":"Janubiy Koreya"}
b = max(poytaxt.items(),key= lambda y:len(y[0]))
print(b[0])



# min funks xam ham maxga oxshaydi ishlaydi faqat agar son bolsa kichigini aniqlayadi
#
#
c = min("HELLO","Salom","salom")
print(c)



# Sorted funksiya 

a = (2,4,3,50,30,10)
b = sorted(a)
print(b)




sonlar1 = [-2,10,20,3,4]
print(sorted(sonlar1))

sonlar2 = [-2,10,20,3,4]
print(sorted(sonlar2))

sonlar3 = [-2,10,20,3,4]
print(sorted(sonlar3))



# Misolar 

# 1. Foydalanuvchi kiritgan sonning modulini hisoblang.
# Kiritilgan son: -7 → Natija: 7

# a = int(input("Son kirirting = "))
# b = abs(a)
# print(b)


