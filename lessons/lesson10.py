# MAVZU ; TUPLE
# oddiy tuple yaratish 

# my_typle = (1,2,3,4)
# print(my_typle)
# Natija (1,2,3,4) 


# Tuple dagi elementlarga index orqali murojat qilish 

# my_typle = ('apple','Banan','Cherry')
# print(my_typle[1])
# Natija #Banan 


# Mashq - MIsol 
#  # bu xolatga olip keladi 
# Natija Eror hatolik beradi 




# Tuple royxatga ozgartirish 

# my_tuple = (1,2,3)
# my_list = list(my_tuple)
# print(my_list)

# Royxatni tuplega ozgartirish 
# my_list= (1,2,3)
# my_tuple= tuple(my_list)
# print(my_tuple)

# Natija 
# [1,2,3]
# [1,2,3]



# Task 1: Tuple yaratish va elementlarga murojaat qilish
# 1.Quyidagi tuple'ni yarating: fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi').
# 2.Tuple'dagi birinchi va oxirgi elementlarni chiqaring.
# 3.Tuple'dagi uchinchi elementni toping

fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')
print(fruits[0])
print(fruits[-1])
print(fruits[2])

#Task 2: Tuple'dan ro'yxatga aylantirish
# 1.Quyidagi tuple'ni yarating: colors = ('red', 'green', 'blue') va unga yangi element qo'shing: 'yellow'.
# va tupleni ekranga chiqaring

# colors = ('red', 'green', 'blue')
# ranglar = list(colors)
# ranglar.append("yellow")
# print(ranglar)
# colors = tuple(ranglar)
# print(colors)

#Task 3;  Tuple'ni teskari qilish
# 1.Quyidagi tuple'ni yarating: letters = ('a', 'b', 'c', 'd', 'e').
# 2.Tuple'dagi elementlarni teskari qilib chiqaring

# letters = ('a', 'b', 'c', 'd', 'e')
# reversed_letters = letters[::-1]
# print("Teskari tuple:", reversed_letters)

# reverse - funksiya orqaga aylantirip beradi 

# Task 4: Tuple va ro'yxat bilan ishlash
# 1.Quyidagi tuple'ni yarating: my_tuple = (10, 20, 30, 40, 50).
# 2.Tuple'ni ro'yxatga o'zgartiring va 60 raqamini qo'shing.
# 3.Ro'yxatni yana tuple'ga o'zgartiring va natijani ekranga chiqaring.

# my_tuple = (10, 20, 30, 40, 50)
# # list(my_tuple)
# # ichidagi jarayon 
# bosh_list = []
# bosh_list.append(my_tuple[0])
# bosh_list.append(my_tuple[1])
# bosh_list.append(my_tuple[2])
# bosh_list.append(my_tuple[3])
# bosh_list.append(my_tuple[4])
# yangi_list = bosh_list
# print(yangi_list)
# a = list(my_tuple)
# print(a)

# my_tuple = (10, 20, 30, 40, 50) 
# yangi_list = list(my_tuple)
# yangi_list.append(60)
# my_tuple = tuple(yangi_list)
# print(my_tuple)



# 1.Ikkita tuple yarating: tuple1 = (1, 2, 3) va tuple2 = (4, 5, 6).
# 2.Ikkala tuple'ni birlashtirib yangi tuple hosil qiling

# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# # tuple3 = tuple1 + tuple2
# print(tuple3)

# 2 yoli 

# list1 = list(tuple1)
# list2 = list(tuple2)
# list1.extend(list2)
# new_tuple = tuple(list1)
# print(new_tuple)



# 2. Juft sonlarni o'chirish
# Sizga tupleda sonlar beriladi va bitta son 2 marta takrorlanmaydi . Berilgan tupledagi eng katta sonnipo
# o’chiring



# my_tuple = (10,20,30,40,50,60,70,80)
# new_list = list(my_tuple)
# del new_list[3:6]
# print(new_list)
# my_tuple = tuple(new_list)
# print(my_tuple)

# Berilgan tupledagi 2-indeksdagi elementni o'chiring.
# cities = ("Toshkent", "Samarqand", "Buxoro", "Qashqadaryo", "Navoiy")
# shaharlar = list(cities)
# del shaharlar [2]
# cities = tuple(shaharlar)
# print(cities)



# 5. Faqat bitta elementli ro'yxat yaratish
# 5 ta elementga ega bo’lgan tuple bor va unda string type dagi malumotlar yozilgan, shu tupledagi eng
# uzun matinning uzunligini aniqlang
# 5 ta elementdan tashkil topgan ixtiyoriy tuple uchun ishlashi kerak pastda misol namuna sifatida
# ko’rsatilgan.
# fruits = ["apple", "banana","elderberry" "cherry", "date"]
# Natija: 10

# fruits = ["apple"*3, "banana","elderberry" "cherry", "date"]
# fruits_lenght = (len[fruits[0]],len [fruits[1]],len [fruits[3]],len [fruits[3]],len [fruits[4]])
# fruits_lenght.sort
# print(fruits_lenght[-1])


# Elmementni indexni aniqlash
# index = fruits.index("cherry")
# print( index)


# Task 11: Listdagi takroriy elementlarni olib tashlash
# Faqat sonlarda tashkil topgan list berilgan va unda faqat 2 raqami bir necha marotaba takrorlangan shu listda
# bitta 2 raqami qolsin va list malumotlarni kamayish tartiba consolega chopeting
# Misol : [12,1,2,2,3,2,4,2,25]

# number = [12,1,2,2,3,2,4,2,25,2,2,2,2,2,2,]
# number.sort()
# count_two = number.count(2)
# two_index = number.index(2)
# # del number (12.5)
# del number [two_index+1:two_index+count_two]
# number.reverse
# print(number)















