# mavzu : break cointinue 

# for i in range(1,11):
#     if i % 2 !=0:
#         continue
#     print(i)



# class work 


# Kursda qilingan mashqlar 

# 1 dan 10 gacha bo'lgan sonlarni tekshirib, birinchi uchragan toq sonni
# topganimizda tsiklni to'xtatamiz.

# for i in range(1,11):
#     if i % 2 ==1:
#      print(i)       
#     break


# 2 
# 1 dan 10 gacha bo'lgan sonlarni tekshirib, faqat toq sonlarni chiqaramiz
# (juft sonlarni o'tkazib yuboramiz).


# for i in range(1,10):
#    if i % 2 !=0:
#     continue
# print(i)


# 3 
# Foydalanuvchi ‘stop’ so`zini kiritguncha qadar tsikl davom etadigan
# dastur tuzing

# while True:
#   soz = input("dasturni toxtatmoqchi bolsangiz stop kiriting")
#   if soz=="stop":
#     print("tsikl toxtatildi")
#     break
  
# 4 
# Berilgan matnda birinchi uchragan 'a' harfini topganda tsiklni to'xtatamiz.

# matn = input("harf kiriting a 1 marta uchraydi ")
# for harf in matn:
#   if harf == "a":
#     print('birinchi a harf kiriting ')
#     break
  

# 5  
#   Sonlar yig'indisini topish (continue bilan). Foydalanuvchi kiritgan manfiy
# sonlarni o'tkazib, ijobiy sonlar yig'indisini topamiz

y = 0 
while True:
  a = int(input("son = "))
  if a <0:
    continue
  elif a == 0:
    break
  else:
    y = y + a 
print("yegindi = ",y)
