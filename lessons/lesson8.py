# name = input(" name = ")

#  print(f" sizning  ismingiz {name}")

# string hech bir funksiyasi  uning asl qiymatini  o'zgartirilmaydi 

# matindagi barcha hariflarni katta hariflarlarga aylantiradi 
# name_katta = name.upper()
# print(name)
# print(name_katta)

#  Bu funksiya matindagi barcha belgilarni kichik harifga aylantiradi 
# print(name.lower())

#  bu funkdiya matinig boshio va oxiridagi bosha joylarni olib tashlaydi 
# print(name.strip())

#  bu funksiya matin boshidagi bosh joyni olib tashlaydi 
# print(name.lstrip())

#  bu funksiya matini oxiridan bosh joyni olib tashlaydi 
# print(name.rstrip())

#  bu funksiya berilgan matinda biror belgi nechi marta qatnashganini aniqlashda yordam beradi 
# print(name.count("j"))

#  bu funksiya matinda har bir sozda birinchi ketgan 
# print(name.title())

# bu funksiya 
# print(name.capitalize())

# bu funskiya birnecha ozgaruvchini elon qilish 
# a , b , c = 10, " Hello", True
# print(type(a))

# uka = int(input ("uka yosh ="))  

# aka = int(input("aka yosh = "))
# print(aka - uka )

# stringdan dan float otish 

# vazin = "85.8"
# b = float (vazin)
# print (b+10)


# topshiriq tort 
# S = ENI + BO'YI 

# eni = float(input(" eni = "))
# boyi = float(input(" boyi = "))
# print= (eni + boyi)


# savol stringdan int ga otish uchun 
# a = "28"
# b = int (a)


# intdan stringa otish uchun 
# age = 20
# new_age = str(age) # "28"

# 12.4 floatdan intga otish 
# son = 12.4 
# new_son = int(son)
# print(new_son)

# int dan float ga otish 
# son1 = 20 
# son2 = float(son1)
# print(son2)


# name = "Jalol"
# new_name = name.upper()
# print= (name)


# topshiriq name oling qiymati barchasi katta harifga olinsin 
# name = "Jalol"
# name = name.lower() # Upper()
# print(name) # Jalol  


 
# ikkita sonni bir – biriga qo'shish
# x, y = 20, 30
# print(x + y)

# ikkita sonda birini ikkinchisidan ayirish
# print(x - y)

# ikkita sonda birini ikkinchisiga ko'paytirish
# print(x * y)

# ikkita sonda birini ikkinchisiga bo'lish
# print(x / y)  # natija nima typeda bo'ladi, int yoki float

# ikkita sonda birini ikkinchisiga butun bo'lish
# print(x // y)

# ikkita sonda birini ikkinchisiga qoldiqli bo'lish
# print(x % y)

# biror sonni darajaga ko'tarish
# print(x ** y)



# a, b = 2, 10

# # a va b ning tengliga tekshirish operatori
# a_tengmi = a == b
# print(a_tengmi)

# # a ni b ga teng emasliga tekshirish
# a_teng_emasmi = a != b
# print(a_teng_emasmi)

# # a ni b dan kattaligiga tekshirish
# a_kattami = a > b
# print(a_kattami)

# # a ni b dan kichikligiga tekshirish
# a_kichikmi = a < b
# print(a_kichikmi)

# # a ni b dan katta yoki tengligiga tekshirish
# a_katta_yoki_teng = a >= b
# print(a_katta_yoki_teng)

# # a ning b dan kichik yoki tengligiga tekshirish
# a_kichik_yoke_teng = a <= b
# print(a_kichik_yoke_teng)



# USERDAN SON Kiritishinmi sorang va unga javob 

# a = int(input(" number1: "))
# b = int(input(" number2: "))

# yegindi = a+b 
# ayerma = a-b

# # print(yegindi)
# # print(ayerma)

# print(f"{a} + {b} = {yegindi}")
# print(f"{a} - {b} = {ayerma}") 


# a = float(input(" Raqam kiriting: "))
# b = float(input(" Raqam kiririing "))

# TOPSHIRIQ 1 
# a = int(input(" number1: "))  # Float 
# b = int(input(" number2: "))  # Float 

# Son = a - b 


# print(Son)



# TOPSHIRIQ 2 

# a = int(input(" number1: "))
# b = int(input(" number2: "))

# raqam = a < b 
# burchak = a > b 

# print(raqam)
# print(burchak)


# Topshiriq 3 

# a = int(input(" number1: "))
# b = int(input(" number2: "))

# raqam = a < b 
# tenglik = a = b 

# print(raqam)
# print(tenglik)


# Topshiriq 4 

# a = float(input(" number1: "))
# b = float(input(" number2: "))

# raqam = a + b 
# tenglik = a // b 

# print(f"{a} + {b} = {raqam}")
# print(f"{a} // {b} = {tenglik}")


# Topshiriq 5 


# a = int(input(" number1: "))
# b = int(input(" number2: "))

# raqam = a - b 
# belgi = a + b 

# print(f"{a} - {b} = {raqam}")
# print(f"{a} + {b} = {belgi}")


# Topshiriq 6 

# a = int(input(" number1: "))
# b = int(input(" number2: "))

# raqam = a + b 
# belgi = a // b 

# print(f"{a} + {b} = {raqam}")
# print(f"{a} // {b} = {belgi}")


# Topshiri1q 7 

# print(f"{m}^{r}={m**r}")


# Topshiriq 8 

# R=float(input("R="))
# p=3.14
# print(2*p*R)

# Topshiriq 9 

# Foydalanuvchi  xonaning o'lchamni kiriting
# uzunlik = float(input("Xonaning uzunligini metrlarda kiriting: "))
# eni = float(input("Xonaning enini metrlarda kiriting: "))
# qalinlik = float(input("Polning qalinligini metrlarda kiriting: "))

# beton_hajmi = uzunlik * eni * qalinlik

# print(f"Sizga kerak bo'ladigan beton miqdori: {beton_hajmi} kub metr")


# Topshiriq 10 

# gildirak  = float(input("gildirak radiusini kiriting: "))
# masofa = float(input("avtomobilni bosib otgan masofasini kiriting: "))
# pi= 3.14

# aylanish = gildirak * 2 * pi
# N = masofa/aylanish

# print(f"gildirak aylanishi {N }marta: ")



# Topshiriq 11 

# ishchilar = int(input" ishchilar soni: ")
# ishlabchiqarish = int(input"ishalabchiqarilgan mahsulot soni ")



# Yangi Mavzu 

# my_list = [1,2,3,4,5]
# names = ["Javohir,Jalol,Anvar,Akmal"]
# numbers1 = [2.3, 4,66,7.89,10.88]
# numbers2 = ["bir","ikki", 3, 4, 5]



# print(my_list)
# print(names)
# print(numbers1)
# print(numbers2)



# my_list = [1,2,3,4,5]
# print(my_list[0]) # 1 
# print(my_list[4]) # 5




# my_list = [1,2,3,4,5]
# my_list[2] = 10
# print(my_list) # [1,2,10,4,5]



# my_list = (1,2,3,4,5)
# my_list.appened(6)
# print(my_list) # (1,2,3,4,5,6)


my_list = [1,2,3,4,5,]
my_list.insert(1,100)
print(my_list)



