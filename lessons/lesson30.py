# Mavzu: Lambda funksiyasi 
# - nomsiz funksiya 
# - va bir qator kod ishlatiladi 

# sonlar = ["Akobir","Jalol","Jasur","Javohir","Mehruz"]
# b=max(sonlar,key=lambda a:len(a))
# print(b)

# Colectionerlarni filtirlash 
# filter ()


# a = list(filter(lambda x:len(x)<=6,sonlar))
# print(a)


# raqamlar = (1,0,2,3,9,5,4,6)
# # raqarmlar tuple dan faqat juft sonlarni olish
# b = tuple(filter(lambda x:x%2==0,raqamlar))
# print(b)


# def custom_filter():
#      son = []
#      for i in raqamlar:
#          if i % 2 == 0:
#               son.append(i)
#               return tuple(son)
         

# custom_filter(raqamlar=)


# map dan qachon foydalanamiz 
# map() - collection elementlarga biror element qoshmoqchi bolsam 


# raqamlar = (1,0,2,3,9,5,4,6)
# def custom_map(sonlar:tuple)->tuple:
#     son = []
#     for i in sonlar:
#         son.append(i+18)
#         return tuple(son)

# a = custom_map(sonlar=raqamlar)
# print(a)
# print(tuple(map(lambda x:x+10,raqamlar)))


# Mustaqil ish 
# 1. Ikkita sonni qo‘shish uchun lambda yozing. 

# hisoblash = lambda a1,a2:a1+a2
# print(hisoblash(10,20))

# 2. Ro‘yxatdan juft sonlarni ajratib olish uchun lambda ishlating.

# raqamlar = [1,0,2,3,9,5,4,6]
# print(list(filter(lambda x:x %2==0,raqamlar)))

# 4. Sonning kvadratini hisoblash uchun lambda funksiyasini tuzing.

# hisoblash = lambda a1,a2:a1**a2
# print(hisoblash(10,2))

# 5. Ro‘yxatdan "A" harfi bilan boshlanadigan ismlarni ajratib oling.

# ismlar = ["Akmal","Jamol","Laziz","Bekzod","Alisher",]
# print(list(filter(lambda a:a [0]=="A",ismlar)))

# 6. Narxga 10% soliq hisoblash uchun lambda yozing

# Narxlar = [1,2,3,4,9]
# print(list(map(lambda x:x*0.1,Narxlar)))

# 7. Ismlar ro‘yxatini bosh harflar bilan yozish uchun map() va lambda funksiyasini birga qo‘llang.

# ismlar = ["akmal","jamol","laziz","bekzod","alisher",]
# bosh_harflar = list(map(lambda ism: ism.capitalize(), ismlar))
# print(bosh_harflar)

# 8. Asosiy arifmetik amallar (qo‘shish, ayirish, ko‘paytirish, bo‘lish) uchun lambda yozing.

# # Qo'shish
# def qoshish(x, y):
#     return x + y

# # Ayirish
# def ayirish(x, y):
#     return x - y

# # Ko'paytirish
# def kopaytirish(x, y):
#     return x * y

# # Bo'lish
# def bolish(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Nolga bo‘lish mumkin emas"

# print(qoshish(5, 3)) 
# print(ayirish(5, 3))  
# print(kopaytirish(5, 3)) 
# print(bolish(5, 3))  
# print(bolish(5, 0))  


# 9 Misol Kortejlarni saralash uchun lambda ishlating

kortejlar = [(1, 5), (2, 3), (4, 1), (3, 4)]
saralangan = sorted(kortejlar, key=lambda x: x[1])
print(saralangan) 
saralangan_birinchi = sorted(kortejlar, key=lambda x: x[0])
print(saralangan_birinchi)  
