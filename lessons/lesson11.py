# Mavzu : Shart operatorlari
# (If… Else…)
# Va
# Mantiqiy operatorlar
 

# Misol:
# A = false, B = true, C = true, D = false bo'lsa,
# quyidagi ifoda natijasini aniqlang.
# ((A and !B) or (C and D)) and not(A or B)


# A = 5  = 5 
# B = 2 %2 ==1
# C = 14 // 4 == 3,
# D = not True
# natija = (A or B) and (C or D) or not (A or B)
# print(natija)

# Son muspat toqligini aniqlash shart 

# age = int (input("Yoshingizni kiriting"))

# agar foudalanuvchi 18 dan katta bolsa dasturdan foydalanaolishini aytamiz 
# aks holda esa dasturdan foydalama

# if age>= 18:
#   print("Dasturga hushkelibsiz")


# else:
#    print("Hozirda dasturda foydalana olmaysiz")





   # Misolar  ▪ Berilgan son musbat juft son bo’lsa True agarda manfiy juft son bo’lsa
# False natija chiqaradigan dastur tuzishni ko’rib chiqamiz.
# ▪ Bu jarayonda nimalarga e’tibor qilishimiz zarur:
# ▪ 1.Son musbat bo’lishi kerak
# ▪ 2.Son juft son bo’lishi kerak

# son = 12
# if son > 0 and son % 2 == 0:
#    print( True)
# else: 
#   print(False)

# Natija : True 



# ▪ Berilgan son 0ga teng yoki 0dan kata bo’lsa “son manfiy emas” degan
# natijani aks xolda “son manfiy” degan natijani chop etsin.
# ▪ Bu jarayonda nimalarga e’tibor qilishimiz zarur:
# ▪ 1.Son 0ga teng bo’lishi yoki 0dan kata bo’lsa yetarli
# ▪ 2.Son juft son bo’lishi kerak 
# son = -5 

# if son >= 0:
#    print("son manfiy emas")
# else: 
#   print("son manfiy")

# HOMEWORK 

# 1 ▪ 1.Butun son berilgan agar son musbat bo’lsa qiymat 1ga oshirilsin aks
# xolda o’zgartirilmasin. Hosil bo’lgan sonni ekranga chiqaruvchi dastur
# tuzing.

# raqam = int(input("Butun raqam kiriting: "))

# if raqam > 0:
#   raqam +=1

# print("Javobi:", raqam)
# Javob : kiritilgan raqamgfa 1 



#  2.Uchta son berilgan shularning orasida eng kattasini aniqlovchi
# dastur tuzing


# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting: "))
# son3 = float(input("3-sonni kiriting: "))

# eng_katta = son1

# if son2 > eng_katta:
#     eng_katta = son2
# if son3 > eng_katta:
#     eng_katta = son3

# print("Eng katta son:", eng_katta)

# Ustoz bergan misol 

# son1 = float(input("son1=")) 
# son2 = float(input("son2=")) 
# son3 = float(input("son3="))

# # agar son eng katta bolsa 
# if son1 >son2 and son1>son3:
# print(f"kiritilgan sondan eng kattasi"(son1))
# # agar son2 eng kattasi bolsa 
# if son2 > son1 and son2>son3:
#     print(f"kiritilgan eng katta son"(son2))
# # agar son3 eng katta bolsa 
# if son3> son1 and son3> son2:
# print(f"kiritilgan eng katta on"(son3))


# 4.Berilgan sonni juft yoki toq son ekanligini topuvchi dastur tuzing.

# son = int(input("Butun sonni kiriting: "))

# if son % 2 == 0:
#     print("Bu son juft.")
# else:
#     print("Bu son toq.")


