#  Mavzu : Set va Dictionori takrorlash 
# UNIT-4: ProgrammingUNIT-4: Programming
# Basics of Programming 2
# Sinfdagi bazi o’quvchilar matematika, inglistili va IT dan qo’shimcha darslarga borishadi.
# Namuna:
# matimatika = [“olim” ,”Behruz” ,”Shohruh”,.....]
# Inglistili = [“olim” ,”Jasur” ,”Jamshid”.....]
# IT = [“Akobir”, “olim”, “Jurabek”...]





# Topshiriq 1. Faqat matimatikdan boradigan talabalar ro’yxatini chiqarib bering

# matimatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo"]
# Inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib"]
# IT = ["Akobir","Olim" ,"Jurabek","Jamshid","Bekzod"]

# matimatika = set(matimatika)
# Inglistili = set(Inglistili)
# IT = set(IT)
# print(matimatika.difference(Inglistili,IT))






# Topshiriq 2.Faqat inglis dan boradigan talabalar ro’yxatini chiqarib bering

# informatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo"]
# inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib"]
# rustili = ["Akobir","Olim" ,"Jurabek","Jamshid","Bekzod"]

# informatika = set(informatika)
# inglistili = set(inglistili)
# rustili = set(rustili)

# print(inglistili.difference(informatika,rustili))







# Topshiriq 3. Faqat IT dan boradigan talabalar ro’yxatini chiqarib bering

# informatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo"]
# inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib"]
# rustili = ["Akobir","olim" ,"Jurabek","Jamshid","Bekzod","Laziz"]

# informatika = set(informatika)
# inglistili = set(inglistili)
# rustili = set(rustili)

# print(rustili.difference(inglistili))








# Topshiriq 4. Faqat matimatikdan va inglistili boradigan talabalar ro’yxatini chiqarib bering


# matimatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo"]
# Inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib","Abdullo"]
# IT = ["Akobir","olim" ,"Jurabek","Jamshid","Bekzod"]

# matimatika = set(matimatika)
# Inglistili = set(Inglistili)
# IT = set(IT)
# ikkita_fan = matimatika.intersection(Inglistili)
# # print(ikkita_fan)
# print(ikkita_fan-IT)
# print(ikkita_fan.difference(IT)) 






# Topshiriq 5 . Faqat matimatika va IT dan boradigan talabalar ro’yxatini chiqarib bering

# matimatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo","Laziz"]
# Inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib","Abdullo"]
# IT = ["Akobir","olim" ,"Jurabek","Jamshid","Bekzod",'Laziz']

# matimatika = set(matimatika)
# Inglistili = set(Inglistili)
# IT = set(IT)
# ikkita_fan = matimatika.intersection(IT)
# print(ikkita_fan-Inglistili)
# print(ikkita_fan.difference(Inglistili)) 







# Topshiriq 6 . Faqat matimatik , inglistili va IT dan boradigan talabalar ro’yxatini chiqarib bering


# matimatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo","Laziz"]
# Inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib","Abdullo","Laziz"]
# IT = ["Akobir","olim" ,"Jurabek","Jamshid","Bekzod","Laziz"]

# matimatika = set(matimatika)
# Inglistili = set(Inglistili)
# IT = set(IT)
# ikkita_fan = IT.intersection(matimatika,Inglistili)
# print(ikkita_fan) 







# Topshiriq 7. Umumiy kursga boradigan talabalar sonini aniqlang

# matimatika = ["olim","Behruz" ,"Shohruh","javlon","Abdullo","Laziz"]
# Inglistili = ["olim" ,"Jasur" ,"Jamshid","Ahmad","Tolib","Abdullo","Laziz"]
# IT = ["Akobir","olim" ,"Jurabek","Jamshid","Bekzod","Laziz"]

# matimatika = set(matimatika)
# Inglistili = set(Inglistili)
# IT = set(IT)
# a = IT.union(matimatika,Inglistili)
# print(len(a))


