# 
# for ozgaruvchi 
# 1 korinish 
# stering elementarlarini 
# for i in "20":
#     print(i)

# 2 listning har biort elementlarini olish mumklin 
# listning har bi
# for i in (1,2,3,4,5):
#     print(i)

# 3 korinishi a sendan elenmentlardan olish 

# fori i in range (o,10,1)
# for i in range(10):
#     print(i)        


# 
# for i in range(10,101):
#     print(i)

#1 masala
# 100 dan 1000 bogan toq sonlarni kiriting 
# for i in range (101,1000,2):
#      print(i)


# 2 misol 
# for i in range(1,1001,1):
#      if i % 2 ==0:
#       print(i)


# usul 
# for a in range(5,1001,5):
#    print(a)
#2 masala 
#  1 dan 100 gacha bolgan toq sonlarni kiriting 
# for i in range(1,101,2):
#     print(i)
#  # 3 masala 




 # 1 dan 100 gacha bolgan sonlar yegindisi yegin 
# yegindi = 0 
# for i in range(1,101,1):
#  yegindi = yegindi+1 
#  print(yegindi)

 # 2 1 da 50 gacha bo’lgan toq va juft sonlarni yig’indisini
# hisoblash
 
#  toq = 0 
#  juft = 0
# for i in range(1,51):
#     if 1 & 2 ==0:
#            juft= juft+1
# else:
#     toq = toq+1 

# print(juft)
# print(toq)         



# Misolar 

# 1 dan 100 gacha nechta juft son bor 
# range (Start, stop,stop)
# Olma = 0 
# for i in range(1,101,1):
#     if 1 % 2 ==0:
#      Olma = Olma+1 
# print(f"1 dan 100 gacha sonlar orasida {Olma} juft son")







# Masalalar 

# Mashq 1 
# 1 dan 100 gacha bo’ldan sonlarni yig’indisini toping

# for i in range(1,101,1):
#     print(i)

# mashq 2 
# 1 da 50 gacha bo’lgan toq va juft sonlarni yig’indisini
# hisoblash.

#  toq = 0 
#  juft = 0
# for i in range(1,51):
#     if 1 & 2 ==0:
#            juft= juft+1
# else:
#     toq = toq+1 

# print(juft)
# print(toq)         




# mashq 3 
# -80 dan 80 gacha bo’lgan sonlar ichida 7 ga
# bo’linadiganlarni nechta ekanligini toping.

# Lol = 0 
# for a in range(-81,80+1):
#     if a % 7 ==0:
#         Lol+=1
# print(f"-80 dan 80 gacha bo'lgan sonlar ichida {Lol} ta son bor")





#  mashq 4  
# List berilgan mevalar = ['olma', 'banan', 'apelsin‘, ‘olma’]
# Listning ichida nechta ‘olma’ so’z borligni aniqlang.

# a =+1 
# mevalar = ("Olma","Banan","apelsin","olma")
# for i in mevalar:
#     if i + "Olma":
#         a = a + 1
# print("olma sponi",a)



# 5 masala 
# range (Start stop step)
# range(20) # start = 0. step = 1 , stop = 20 

# sonlar = (2,3,1,90,50)
# for i in sonlar:
#     print(sonlar(i))
# #######################################

# talabalar = ("abu","Doni","Otash")
# # malumaot turlari int float srting tuple bool list  

# for i in talabalar:
#     print(i)


# # .
# #  6. masaala
# #  List x = [1,2,3,4,5,6,6,7,8,9] berilgan list ichida 2 ga 
# # bo’linadiganlarni nechta ekanligini aniqlang
# lister=0
# List_x = [1,2,3,4,5,6,6,7,8,9] 
# for i in range(1,10):
#     if i % 2 == 0:
#         lister=lister+2
#         print(f"2ga bolinadigan sonlar {lister} lar bolinadi")  
# #  7. masaala Ekrandan matn kiritiladi masalan: “Welcome to System”  
# # shu matn ichida nechta katta harf bor ekanligini aniqlang.
# matin =input ("welkome to syustem")
# b=0
# print(matin[0])
# for i in matin:
#     if i.isupper():
#         b= b+1
# print(f"siz kirtgan matnda {b} ta arif bor ")






 # Misol 7 
# 7. Ekrandan matn kiritiladi masalan: “Welcome to System”
# shu matn ichida nechta katta harf bor ekanligini aniqlang

# matin = input("matin = ")
# b = 0 
# print(matin(0))
# for i in matin:
#     if i.isupper():
#      b = b + 1      
# print("siz kiritgan matinda (b) ta katta harf bor")




# # 8 masalaa
# # 1 dan 100 gacha raqamlarni chop eting, lekin:
# #  Agar raqam 3 ga bo'linadigan bo'lsa, "Fizz" ni chiqarin.
# #  Agar raqam 5 ga bo'linadigan bo'lsa, "Buzz" ni chiqarin.
# #  Agar raqam 3 va 5 ga ham bo'linadigan bo'lsa, "FizzBuzz" ni 
# # chiqarin
# for i in range(1,101):
#     if i % 3 ==0:
#        print("fizz")
#     elif i % 5 == 0:
#        print("buzz")
#     elif i % 3 ==0 and i % 5 ==0:
#        print("fizzbuzz")
# else:
#    print(i)


# 5. A dan B gacha sonlar berilgan berilgan son ichida nechta
# toq va juft sonlar borligni aniqlang


# A =  int(input("a = "))
# B =  int(input("b = "))
# if A>B:
#    A,B = B,A
# toq_c = 0
# juft_c = 0
# for i in range(A,B+1):
#     if 1 % 2 == 0:
#         juft_c = juft_c+1
#     else: 
#         toq_c = toq_c+1 
# print(f"{A} sonda {B} songacha {juft_c} ta juft son bor")
# print(f"{A} sonda {B} songacha {toq_c} ta juft son bor")



# 9. Berilgan ro'yxatdagi har bir o'lchovni dyuymdan santimetrga
# o'zgartiring (1 dyuym = 2.54 sm). dyumlar = [1, 2, 3, 4, 5]


# dyumlar = (1,2,3,4,5) # 1 d = 2.54 sm 
# smlar = []
# for i in dyumlar:
#    smlar.append(1*2,54)
# print(smlar)


# 10. sonlar = [5, 10, 15, 20, 25, 30]. Berilgan ro'yxatdagi faqat juft va
# 10 dan katta sonlarni olish.







# 11. sonlar = [5, 10, 15, 20, 25, 30] berilgan ro’yxatning har bir
# elementini 3 ga bo’lgandagi qoldiqni yangi ro’yxatga yuklang va
# hosil bo’lga ro’yxatning elementlarini chiqaring
# sonlar = [5, 10, 15, 20, 25, 30]
# qoldig = []
# for i in sonlar:
#     qoldig.append(i%3)
# print(qoldig)

# 12. Ro’yxat berilga x = ["olma", "banana", "olcha", "limon", "olxo'ri"]
# Berilgan ro’yxat ichida ‘o’ harfidan boshlangan barcha elemetlarni
# chiqaring

# x = ["olma", "banana", "olcha", "limon", "olxo'ri"]
# for i in x:
#     if i [0] == "o":
#         print(i)
