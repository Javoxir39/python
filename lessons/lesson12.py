# Mavzu :  if,else,elif

# haaftakuni = input("Kun = ")
# if haaftakuni == "1":
#     print("Monday")
# elif haaftakuni == "2":
#      print("Seshanba")
# elif haaftakuni == "3":
#      print("cHORSHABA")
# elif haaftakuni == "4":
#      print("payshanba")
# elif haaftakuni == "5":
#      print("Juma") 
# elif haaftakuni == "6":
#      print("shanba")
# elif haaftakuni == "7":
#      print("yakshanba")     
# else:
#     print("Bunday haftani kuni mavjud emas ")




# Oysanalari = input("Oy = ")
# if Oysanalari == "1":
#     print("Monday")
# elif Oysanalari == "2":
#      print("Seshanba")
# elif haaftakuni == "3":
#      print("cHORSHABA")
# elif haaftakuni == "4":
#      print("payshanba")
# elif haaftakuni == "5":
#      print("Juma") 
# elif haaftakuni == "6":
#      print("shanba")
# elif haaftakuni == "7":
#      print("yakshanba")     
# else:
#     print("Bunday haftani kuni mavjud emas ")


# Ozimni misolim 

# a = float(input("Hohlagan son kiriting: "))
# b = float(input("Hohlagan son kiriting: "))

# 1 = a + b 
# 2 = a - b 
# 3 = c * 1-2 
# print("Natija", c)z



# Homework Vazifa:


# 1 misol
# Semestr davomida talaba to’plagan reyting ballga mos
# ravishda uning o’zlashtirishi haqida xabar chiqaring:
# 00-55 -> 2-qoniqarsiz
# 56-70 -> 3-qoniqarli
# 71-85 -> 4-yaxshi
# 86-100 -> 5-a’lo


# ball1=float(input("Toplangan balingizni kiriting: "))
# print(""" 
#     1: 00-55 -> 2-qoniqarsiz
#     2: 56-70 -> 3-qoniqarli
#     3: 71-85 -> 4-yaxshi
#     4: 86-100 -> 5-a’lo """)
# ball3 = input(f"toplangan bnallingiz: ")
# if ball1>0 and ball1 <56:
#     print("qoniqarsiz")
# elif ball1 =="2":
#     print("qoniqarli")
# elif ball1=="3":
#     print("Yaxshi")
# elif ball1=="4":
#     print("Alo")
# else:
#     print("Mavjud bolmagan ballni kiritingiz: ")

# Ustoz bergan malumot 

# reyting_ball = float(input("Ballingizni kiriting: "))
# natija = ""
# if reyting_ball >= 0 and reyting_ball <= 55:
#     natija = "2-qoniqarsiz"
# elif reyting_ball > 55 and reyting_ball <= 70:
#     natija = "3-qoniqarli"
# elif reyting_ball > 70 and reyting_ball <= 86:
#     natija = "4-yaxshi"
# elif reyting_ball > 86 and reyting_ball <= 100:
#     natija = "5-a'lo"
# else:
#     natija = "Xato! Bunday ball mavjud emas"
# print(natija)


# Elektromobilning 100 km masofani bosib o’tish uchun
# akkumlatoridagi to’liq quvvatning 40 foizini sarflaydi. Ayni
# paytda uning quvvati (energy) K foiz qolgan. Haydovchi D
# (distance) km masofaga borishi uchun quvvat yetarli yoki
# yetarli emasligini aniqlang. Agar bor quvvat yetarli bo’lmasa,
# yana necha foiz quvvat kerakligi (required power) ni aniqlang.
# Bunda K va D foydalanuvchi tomonidan kiritiladi. 

# K = float(input("Qancha energy qolganini kiriting: "))
# D = float(input("Nchi Km/h bosip otingiz: "))

# Natija = K*D
# print(Natija)


# Ustoz korsatgan variyant 

# K = float(input("Qancha energy qolganini kiriting: "))
# D = float(input("Nchi Km/h bosip otingiz: "))

# yurish_masofasi= K * 2.5
# if D < yurish_masofasi:
#   print("Quvvat yetarli")
# else:
#    kerakli_quvvat = (D-yurish_masofasi)
#    print(f"""siz bormoqchi bolgan masofaga yetaolmaysiz{kerakli_quvvat}% yana kerak""")


# Uztozning misolari 

# reyting_ball = float(input("Talabaning reyting ballini kiriting: "))
# natija = ""
# if reyting_ball >= 0 and reyting_ball <= 55:
#     natija = "2 - Qoniqarsiz"
# elif reyting_ball >= 56 and reyting_ball <= 70:
#     natija = "3 - Qoniqarli"
# elif reyting_ball >= 71 and reyting_ball <= 85:
#     natija = "4 - Yaxshi"
# elif reyting_ball >= 86 and reyting_ball <= 100:
#     natija = "5 - A’lo"
# else:
#     natija = "Xato: Bunday ball mavjud emas"

# print(natija)


# Vazifa 

# Oysanalari = input("Oy = ")
# if Oysanalari == "1":
#     print("qish fasli")
# elif Oysanalari == "2":
#      print("qish fasli")
# elif Oysanalari == "3":
#      print("bahor fasli")
# elif Oysanalari == "4":
#      print("bahor fasli")
# elif Oysanalari == "5":
#      print("bahor fasli") 
# elif Oysanalari == "6":
#      print("yoz fasli")
# elif Oysanalari == "7":
#      print("yoz fasli")     
# elif Oysanalari == "8":
#      print("yoz fasli")      
# elif Oysanalari == "9":
#      print("kuz fasli")
# elif Oysanalari == "10":
#      print("kuz fasli")  
# elif Oysanalari == "11":
#      print("noybar")
# elif Oysanalari == "12":
#      print("qish faslir")                     
# else:
#     print("Bunday oy kuni mavjud emas ")


# Oy = input("Oy = ")

# if Oy ==11 or Oy == 2 or Oy==12:
#   print("qish")
# elif Oy==3 or Oy == 4 or Oy==5: 
#   print("Bahor")
# elif Oy ==6 or Oy== 7 or Oy ==8:
#   print("yoz")
# elif Oy ==9 or Oy ==10 or Oy ==11:
#   print("Kuz")
# else:
# print("Bunday oy mavjud emas")


# Usul 3
# oy = int(input("Oy -> "))
# if oy == 1:
#     print("Qish")
# elif oy == 2:
#     print("Qish")
# elif oy == 3:
#     print("Bahor")
# elif oy == 4:
#     print("Bahor")
# elif oy == 5:
#     print("Bahor")
# elif oy == 6:
#     print("Yoz")
# elif oy == 7:
#     print("Yoz")
# elif oy == 8:
#     print("Yoz")
# elif oy == 9:
#     print("Kuz")
# elif oy == 10:
#     print("Kuz")
# elif oy == 11:
#     print("Kuz")
# elif oy == 12:
#     print("Qish")
# else:
#     print("Siz kiritgan oy mavjud emas")




# Vazifa 2 


# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting: "))
# son3 = float(input("3-sonni kiriting: "))

# eng_katta = son1

# if son2 > eng_katta:
#     eng_katta = son2
# if son3 > eng_katta:
#     eng_katta = son3

# print("Eng katta son:", eng_katta)


# Topshiriq 2
# Foydalanuvchidan 3 ta sonni qabul qilib oling va shu sonlarni o'sish tartibida joylashtiring

# son1 = float(input("son1 -> "))
# son2 = float(input("son2 -> "))
# son3 = float(input("son3 -> "))
# if son1 >= son2 and son1 >= son3:
#     print("son1 eng katta")
# elif son2 >= son1 and son2 >= son3:
#     print("son2 eng katta")
# elif son3 >= son1 and son3 >= son2:
#     print("son3 eng katta")




# Topshiriq 
# foydalanuvchidan 3 ta sonni qabul qilib oling va shu sinlarni 
# osish tartibida koylashtiringh  


# son1=float(input("son1="))
# on2=float(input("son2="))
# son3=float(input("son3="))
# agar son1 eng katta bolsin
# if son1>son2 and son1>son3:
#       print("son1 katta")
# son2 yoki son3 eng kichigi bolishi mumkin
# if son2>son3:
#       print("son3 eng kichik")
#       print("son2 ortanchasi")
# else:
#       print("son2 eng kichik")
#       print("son3 ortanchasi")
# son2 eng kattasi bolsa
# elif son2>son1 and son2>son3:
#       print("son2 katta")
      
#   son3 eng katta bolsin
# elif son3>son1 and son3>son2
#      print("SOn3 katta")
# if son2>son1:
#     print("son1 eng kichik")
#     print("son2 ortanchasi")
# else:
#      print("son2 eng kichik")
#      print("son1 ortanchasi")


