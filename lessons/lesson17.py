# while shart 
#    while tanasi 

# while 2==2:
#     print("Group 209")

# 1 dan 100 gacha sonlarni chiqarish
# for bilan 
# for i in range(1,101):
#     print(i)

# while else statement 

# i =1 
# while i < 6:
#     print(i)
#     i = i + 1 
# else:
#     print("Loy")


# while loop list 

# mevalar = ["olma","banan","olcha","Limon","Jovoh"]
# i = 0 
# while i < len(mevalar):
#     print(mevalar[i])
#     i = i + 1 


# While loop if 

# number  = [1,20,-9,6,0,41]
# i = 0 
# while i < len(number):
#     if number[i] % 2 ==0: 
#       print(number[i])
#     i = i + 1 


#  Misol 
# Foydalanuvchidan raqam so'rang va u 0 dan katta bo'lsa, uni
# yig'indiga qo'shib boring. 0 kiritilganda, yig'indini chiqarin.



# 1 topshiriq 
# 100 dan 1000 gacha toq sonlarni ekranga chgiqarish 
# i = 100 
# while i <1000:
#     if i %2== 1:
#         print(i)
#     i = i + 1     

# topshiriq 2  
# 10 dan 1000 gacha bolgan  juft  sonlarni ekranga chiqarish 

# i = 10 
# while i<1001:
#     if i %2==0:
#         print(i)
#     i = i + 1 

# topshiriq 3 
# 100 dan 1000 gacha 5 ga bolinadigon sonlarni ekranga chiqarish  

# i = 100 
# while i<1001:
#     if i %5==0:
#         print(i)
#     i = i + 1    

# topshiriq 4 
# -80 dan 100 gacha 10 ga bolinadigon sonlarni yigilishini toping 


# i = -80 
# yeginmdi = 0 
# while i <101:
#     if i %10 == 0:
#         print(i)
#         yeginmdi +=1 
#     i = i + 1   
# print(yeginmdi)


# topshiriq 5 
# - 180 dan 1000 gacha 33 ga bolinadigon sonlar nechta 

# i = -180 
# yeginmdi = 0 
# while i <1001:
#     if i %33 ==0:
#         yeginmdi +=1 
#     i = i + 1 
# print(yeginmdi)    


# 6 topshiriq 
# -80 dan 100 gacha 5 ga va 10 bolinadigon sonlarni yigindisini topi

# i = -80 
# yegindi = 0 
# while i <101:
#     if i %5==0 and i %10==0:
#         yegindi +=1
#     i = i + 1 
# print(yegindi)        
 


# Topshiriq 1
# user stop yozuvini yozgunicha ekranga 
# Dasturni to'xtatish uchun stop ni yozing degan matin chiqsin
# print("Das toxta uch toxta dep yozinihg")
# while input().lower()=="stop":
#     print("Dasturni toxtashish uchun stopni ypzing")

# info =""
# while info != "stop":
#     info = input("Dasturni toxtashish uchun stopni ypzing").lower()


# Topshiriq 2
# Foydalanuvchi biror  son kiritsin 
# agar u toq son kiritsa
# siz toqson kiritdingiz
# agar juft son kiritsa 
# siz juft son kiritdingiz 
# degan matin chiqsin 
# agar 0 kiritsa dastur to'xtasin

# a = 1 
# while a !=0:
#     a = int(input("son kiriting = "))
#     if a % 2 == 1:
#         print("siz toqson kiritingiz")
#     else:
#         print("siz juft son kiritingiz")




# Topshiriq 3
# Foydalanuvchidan raqam so'rang va u 0 dan katta bo'lsa, 
# uni yig'indiga qo'shib boring. 0 kiritilganda, yig'indini chiqarin.

# c = 100 
# y = 0 
# while c !=0:
#     c = int(input("son kiriting = "))
#     if c>0:
#         y = y + c 
# print(y)        
# else 
# print("notogri malumot kiritingiz")
        

# Homework 

# 1. Foydalanuvchidan raqam so'rang va u 0 dan katta bo'lsa, uni
# yig'indiga qo'shib boring. 0 kiritilganda, yig'indini chiqarin.

# yigindi = 0
# raqam = int(input("Birinchi raqamni kiriting (0 chiqish uchun): "))
# if raqam > 0:
#     yigindi += raqam
#     print("Joriy yig'indi:", yigindi)
# else:
#     print("Yig'indi:", yigindi)


#  2. A dan B gacha bo’lgan sonlarni yig’indisni ekranga chiqaring.


# a = int(input("A son kiriting = "))
# b = int (input("B son kiritting = "))
# yegindi = 0
# if a > b:
#     a,b=b,a
# while a < b + 1:
#     yegindi +=a
#     a+=1 
#     print(yegindi)

    

