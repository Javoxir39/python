# Dictionaty dan misolar 

# 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir
# kalit va qiymatni for tsikli yordamida ekranga chiqaring

# a = {"2":"Bir","1":"on","4":"ooo","55":"opp","6":"ouuu","67":"oii","2":"Bir","2":"Bir","2":"Bir","2":"Bir"}
# for o,b in a.items():
#     print(o,b)


# ustoz lorsatgan misol 

# a = {1:"Dushanba",2:"Seshanba",3:"Chorshanba",4:"Payshanba",5:"Juma",6:"Shaba",7:"Yakshanba"}
# for k,v in a.items():
#     print(f"Key = {k}")
#     print(f"value = {v}")



# 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin
# poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

# b = {"Toshkent":"Uazbekiston","Astana":"Qozogiston","Washington":"Aqsh"}

# davlart nomlari va poytaxtlarni alifbo tartibida chiqaring 

# poytaxt = [] # dictionarri barcha kiylar qoshish kerak
# davlat = [] 

# for k,v in b.items():
#     poytaxt.append(k)
#     davlat.append(v)
    
# poytaxt.sort()
# davlat.sort() 
# print(poytaxt)
# print(davlat)

# K Va v dan alohida shaxar va poytaxtni olish uchun 

# print(b["Astana"])

# Homework 3.4.5.6


# 3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni
# chiqaring


# Poytaxt = {"O‘zbekiston":"Toshkent","Moskva":"Rossiya","Astana":"Qoraqalpogiston","Azerbajan":"Armeniya"}

# davlat = input("Qaysi davlat paytaxtini qidiryapsiz = ")
# if davlat in Poytaxt:
#     print(f"{davlat}ning paytaxti= {Poytaxt[davlat]}shaxri")
# else:
#     print(" menda bunday malumot yoq")



# 4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta
# ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom
# menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring


# u1 = input("Xoxlagan taomingizni kiriting = ")
# u2 = input("Xoxlagan taomingizni kiriting = ")
# u3 = input("Xoxlagan taomingizni kiriting = ")
# taomlar = {    
#     "Shashlik": 30000,
#     "Osh": 25000,
#     "Manti": 15000,
#     "Lagmon": 20000,
#     "Somsa": 10000,
#     "Shurva": 22000,
#     "Chuchvara": 18000,
#     "Beshbarmak": 35000,
# }
# for i in [u1,u2,u3]:
#     if i in taomlar:
#      print(f"{i}ning narhi {taomlar[i]} so'm.")
# else:
#     print("Bizda sizga yoqadigon emish yoq")


# Topshiriq 6

# List berilagan sonlar = [...] shu listdagi raqamlar necha marta qatnashganini aniqlash. user dan input oling listda qaysi son
# necha marta qatnashganini bilishni xoxlaysiz degan manada son qabul qilinadi agar user kiritgan Son listda bo’lmasa listda
# bunday son mavjude emas degan xabar bersin
# Namuna
# sonlar = [ 1, 2,4,2,3,67,8,4,5,6,3,2,6,89,59]
# User kiritgan son 2 bo’lsa 3 marta qatnashgan chegan yozuvchiqishi kerak
# Agar user kiritgan son 100 bo’lsa listda bunday son mavjud emas degan yozuv chiqsin


