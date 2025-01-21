# # Mavzu : Ekuk va Ekub kub

# # Ekub 
# while True:
#      if input("Dasturni toxtatish uchun 0 kiriting ") == "0":
#           break
#      a = int(input("a = "))
#      b = int(input("b = "))

#      # a kichik b katta 

#      if a > b:
#           a,b = b,a
#           i = 1 
#           ekub = 1 
#           while i < a+1:
#                if a % 1 == 0 and b % 1 == 0:
#                              ekub = 1 
# i = i + 1 
# print(f"{a} va {b} sonning ekubi = {ekub}")

# # Ekuk A = 5 B = 15 
# Ekuk = 0
# c = b
# while True:
#     if c % a == 0 and c % b == 0:
#          Ekuk = c 
#          break
#     c = c + 1 
# print(f"{a} va {b} sonning ekuki = {Ekuk}")


# while True:
#     if input("Dasturni toxtatish uchun 0 kiriting ") == "0":
#        break
# son = int(input("son = "))
# i = 2 
# counter = 0
# while i < son:
#     if son % i == 0:
#         counter = counter + 1 
#         break
# if counter == 0:
#     print("Toq son")
# else:
#     print("Toq emas")


# homework 

# topshiriq 1 
# user kiritgan ikkita sonni ekubni aniqlashni for yardamida qilish

while True:
    if input("Dasturni toxtatish uchun 0 kiriting ") == "0":
       break

    number = int(input("number = "))
    for j in range(2,number+1):
         son = j
         i = 2 
         counter = 0
         while i < son:
            if son % i == 0:
                counter = counter + 1 
                break
            i = i + 1 
         if counter == 0:
            print(f"{son}-Tup son")
         # else:
         #    print(f"{son}-Tup emas")
# topshirq 2
# userdan son kiritishini so'rang va shu songacha bo'lgan barcha tup sonlarni chiqarib bering