# Mavzu : if else takrorlash 

# hafta_kuni1 = input("Kuni kiriting = ")

# if hafta_kuni1 =="7":
#     print("Dushanba")
# if hafta_kuni1 == "7":
#     print("seshanba")
# if hafta_kuni1 == "7":
#     print("chorshanba")
# if hafta_kuni1 == "7":
#     print("payshanba")
# if hafta_kuni1 == "7":
#     print("JUMA")
# if hafta_kuni1 == "7":
#     print("shanba") 
# if hafta_kuni1 == "7":
#     print("yakshanba")



# hafta_kuni1 = input("Kuni kiriting = ")
# if hafta_kuni1 =="1":
#     print("Dushanba")
# elif hafta_kuni1 == "2":
#     print("seshanba")
# elif hafta_kuni1 == "3":
#     print("chorshanba")
# elif hafta_kuni1 == "4":
#     print("payshanba")
# elif hafta_kuni1 == "5":
#     print("JUMA")
# elif hafta_kuni1 == "6":
#     print("shanba") 
# elif hafta_kuni1 == "7":
#     print("yakshanba")
# else:
#     print("Bunday son mavjud emas")



# oy = input("Oy = ")
# if oy =="1" or oy == "2" or oy == "12":
#     print("Qish")
# elif oy =="3" or oy == "4" or oy == "5":
#     print("Bhor")
# elif oy =="6" or oy == "7" or oy == "8":
#     print("Yoz")    
# elif oy =="9" or oy == "10" or oy == "11":
#     print("Kuz")    



#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333








#      1 - masala
#  Bola voyaga yetga yoki yetmaganligni tekshiradiga dastur tuzing
#  agar voyaga yetga bo'lsa "voyaga yetga" ask holda "voyaga yetmagan"
#  so'zini ekranga chiqaring

# A = int(input("Yoshimngizni kiriting: ")) 
# if A >= 18:
#    print("voyaga yetmaagan")
# else: 
#     print("Siz balogatga yetgansiz")


#      2 - masala
#  Talaba olgan bahosini tekshiring dastur tuzing agr talaba 5 baho olgan bo'lsa
#  a'lo, agar 4 baho olgan bo'lsa yaxshi, agar 3 baho olgan bo'lsa qoniqarli
#  agar 2 baho olgan bo'lsa qoniqarsiz degan so'zlarni ekranga chiqaring

# Baho = int(input("Olgan bahoingizni liriting: "))
# if Baho == 5:
#     print("Alo baho")
# elif Baho ==4:
#     print(" Yahshi")
# elif Baho ==3:
#     print("qoniqarli")
# elif Baho ==2:
#     print("qoniqarsiz")
# else:
#     print("Bunaday Baho mavjud emas")




#      3 - masala
#  Oy raqanimi ekrandan kiritilsa shunga mos fasilni ekranga cjiqaring
#  maslana: 12, 1 yoki 2 raqam kiritilsa Qish fasili deb chiqaring

# Oy = input("Oy raqamini kiriting: ")
# if Oy =="1" or Oy =="2" or Oy =="12":
#     print("Qish fasli ")
# elif   Oy =="3" or Oy =="4" or Oy =="5":
#     print("Bahor fasili ")  
# elif Oy =="6" or Oy =="7" or Oy =="8":
#     print("Yoz fasli ")   
# elif Oy =="9" or Oy =="10" or Oy =="11":
#     print("Kuz fasli  ")   
# else:
#     print("Bunday son mavjud emas: ")      




#  4 - masala
# Havoning harorati haqiqiy sonda kiritilsa unga mos holda 30 dan katta bo'lsa
#  "havo issiq", agar 30 < 20 > 15 "havo iliq" aks holda 15 dan kichik bolsa "havo sovuq"
#  kabi so'zlarni chiqaring

# xarorat = float(input("havo haroratini kiriting: "))
# if xarorat >=30:
#     print(" havo iliq ")
# elif xarorat <=30:
#     print(" havo soviq ")
# else:
#     print("Bunday havo harorati mavjud emas: ")



#  5 - masala

# Hujjatning amal qilish muddati kiritiladi butun sonda agar hujjat amal qilish muddati
# 5 kundan o'tib ketgagn bo'lsa "hujjat amal qilish muddati tugadi" aks holda "hujjat amal qilish muddati tugagan" kabi so'zlarni chiqaring

# muddat = int(input("Hujjat mudadtinui kiritnig: "))
# tugash = int(input("Hujatning tugash sannasini kiriting: "))
# if muddat <5:
#    print("AMAL QILISH MUDATTI YAROQLI: ")
# else:
#    print("amal qilish mudatti tugagan")



# 6 - masala
# To'lov usuli matn sharkida kiritiladi naqt yoki kartada agar naqt deb kiritilsa
# summa kiritishni so'raydi agar karta deb kiritilsa parol kiriing deb so'rasin

# paymet = input("Tolov turuni tanlan\n:Kart\nNaqt:\n")
# if paymet.upper()== "Karta".upper():
#     input("parolni kiriting = ")
# elif paymet.upper() == "Naqt".upper():
#       input("summasini kiriting summa = ") 
# else:
#     print("xato tolov turi nalandi")    




# 7 - masala
# Baho baholash: Foydalanuvchidan bahoni so'rang va 90 dan yuqori bo'lsa "A", 80-89 "B", 70-79 "C", 60-69 "D", 60 dan past bo'lsa "F" deb chiqarish.

# baho = float(input("olhan bahoingizni kiriting: "))
# if baho >=90 and baho<=100:
#     print("A")
# elif baho >=80 and baho<=89:
#     print("B")
# elif baho >=70 and baho<=79:
#     print("C")
# elif baho >=60 and baho<=69:
#     print("D")
# elif baho <=60:
#     print("F")
# else:
#     print("Bunday son mavjud emas")




# 8 - masala
# Yoshni tekshirish: Foydalanuvchining yoshini so'rang va agar 18 dan katta bo'lsa "Kattalar", aks holda "Bolalar" deb chiqarish

# yosh = int(input("Yoshingizni kiriying: "))
# if yosh >=18 and yosh<=150:
#     print("Balogat yoshiga yetkansiz: ")
# elif yosh >=17 and yosh<=0:
#     print(" lol ")
# else:
#     print(" Balogat yoshiga yetmagansiz:")




# 9 - masala
# Kiyinish qoidalari: Foydalanuvchidan ob-havo haqida so'rab, agar yomg'ir yoki qor bo'lsa, "Ko'ylak kiyma" deb chiqarish

# havo = str(input("Ob havo haqida malumot bering: "))
# if havo == "issiq":
#    print("Mayka,Shorti,Naski: ")
# elif havo == "sovuq":
#    print("Chopon")
# elif havo == "Yomgirli":
#    print("Shim-chopon") 
# else:
#    print("Xatolik")






# 10 - masala
# To'lov turini tanlash: Foydalanuvchidan to'lov turini (naqd, kartochka) so'rab, har biriga alohida xabar berish.


# tolov = str(input("tolovturini tanlang\nKart\nNaqt\n"))
# if tolov =="Kart":
#    print("Parolni krirting")
# elif tolov =="Naqd":
#    print("Summa")
# else:
#    print("Bunday tolov turi mavjud emas: ")






# 11 - masala
# Sertifikat olish: Foydalanuvchi 70% dan yuqori baho olsa, "Sertifikat olishingiz mumkin" deb chiqarish.

# ball = float(input("olgan bahoyingizni kiritimn: "))
# if ball >=70:
#     print("Sertifikat olishimngiz mumkin: ")




# 12 - masala
# Yil faslini aniqlash: Foydalanuvchidan oy raqamini so'rang va yil faslini aniqlash (qish, bahor, yoz, kuz).

# oy = int(input("Oy raqasmini kiriting: "))
# if oy == 12 or oy == 1 or oy == 2:
#     print("Qish fasli")
# elif oy == 3 or oy == 4 or oy == 5:
#    print("Bahor fasli")
# elif oy == 6 or oy == 7 or oy == 8:
#    print("Yoz faski")
# elif oy == 9 or oy == 10 or oy == 11:
#    print("Kuz fasli")
# else: 
#    print("Mavjud bolmagan son raqamini kiritingiz: ")





# 14 - masala
# Qaror qabul qilish: Foydalanuvchiga xohlagan taomni tanlasa, "Tayyorlashga kirishamiz" deb chiqarish

# emish = str(input("xohlagan taomni tanlang: "))
# if emish == "Osh" or emish =="Shorva" or emish == "Mastava":
#     print("Tayyorlashga kirishamiz")
# elif emish == "tuz" or emish== "kalbasa"  or emish == "sasiska":
#   print("Tayyorlashga kirishamiz")
# else: 
#    print("Bunday taom yoq")







# 15 - masala
# Avtomobil yoshi: Foydalanuvchidan avtomobilning yoshi va yurgan masofasini so'rang va agar yoshi 10 dan katta bo'lsa, "Ehtiyot qismlarni tekshiring" deb chiqarish.

# yoshi = int(input("Avtoni yilini kiriting: "))
# masofa = float(input("masofani kiriting: "))
# if yoshi>=10:
#   print("Zapchastlarni tekshjiring")
# elif yoshi<=10:
#   print("Yaroqli")
# else:
#   print("Mashijna xolati Axlat")  









# 16- masala
# Sovg'a tanlash: Foydalanuvchidan yoshi va jinsi (erkak/ayol) so'ralib, unga mos sovg'a tavsiya etish.


# jins = input("Jinsingizni krirting\nErkak: \n Ayol: ")
# yosh = int (input("Yoshingizni kiriting: "))
# if yosh >=18 and yosh<=150:
#     print("Sizga Velosiped taklif qilamiz")
# elif yosh >=18 and yosh <=150:
#    print("Sizga soska reziniviy")
# else: 
#   print("Bunday SHAHS MAVJUD EMAS")   









# 17 - masala
# Reyting tizimi: Agar foydalanuvchining balini 100 dan yuqori bo'lsa, "Reytingni yangilang" deb chiqarish.

# ball = float(input("Ballingizni kiriting "))
# if ball <=100:
#     print("Reyting hali yaroqli")
# else:
#     print("Reytingizni yangilang")    


# 18 - masala
# Vaqtni tekshirish: Foydalanuvchidan vaqtni so'rang va agar tun bo'lsa "Xayrli tun", kunduzi bo'lsa "Xayrli kun" deb chiqarish

# kun = str(input("Hozirgi vaqtni kiriting\n Kun: \n Tun:"))
# if kun <= "Kun:":
#    print("Xayirli kun: ")  
# elif kun >= "Tun":
#   print("xayirli tun")
# else:
#    print("XAto")




# 19 - masala
# Parol kuchini tekshirish: Foydalanuvchidan parolni so'rang va agar u 8 ta belgidan kam bo'lsa, "Parolni kuchaytiring" deb chiqarish.

# Parol = int(input("Parolni kiriting: "))
# if Parol <=8:
#   print("parolni kuchaytiring: ")




# 20 - masala
# Kredit tayyorgarligi: Foydalanuvchining daromadi va qarzini so'rab, agar daromadi qarzidan yuqori bo'lsa "Kredit olish mumkin" deb chiqarish.


# daromad = float(input("Daromadingizni kiriting: "))
# qarz = float(input("Qarz miqdorini kiriting: "))
# if daromad > qarz:
#     print("Kredit olish mumkin")
# else:
#     print("Kredit olish mumkin emas")

