# column=int(input("column"))
# row=int(input("row"))
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         if j==1 or j==column:
#             print(j, end=' ')
#         elif i==1:
#             print(j, end=" ")
#         elif i==row:
#             print(j,end=" ")
#         else:
#             print("*", end=' ')
#     print()

# column=int(input("column"))
# row=int(input("row"))
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         if j==1:
#             print(i,end=" ")
#         elif i==1:
#             print(j,end=' ')
#         else:
#             print("*",end=" ")
#     print()


# # Ro'yxat berilgan
# numbers = [1, 2, 3, 6, 5, 4]

# # Foydalanuvchidan son kiritish
# N = int(input("Ro'yxatdan son kiriting: "))

# # Ro'yxatda kiritilgan sonning indeksini topish
# if N in numbers:
#     idx = numbers.index(N)
#     # Shu son gacha bo'lgan sonlarning yig'indisini hisoblash
#     yigindi = sum(numbers[:idx + 1])
#     print(f"Ro'yxatda {N} gacha bo'lgan sonlarning yig'indisi: {yigindi}")
# else:
#     print(f"{N} ro'yxatda mavjud emas.")


# # Rekursiv funksiya
# def yigindi_rekursiya(numbers, index):
#     # Baza holati: agar index 0 ga teng bo'lsa, faqat birinchi sonni qaytaramiz
#     if index == 0:
#         return numbers[0]
#     # Rekursiv chaqiruv: agar index 0 dan katta bo'lsa, yig'indini hisoblaymiz
#     else:
#         return numbers[index] + yigindi_rekursiya(numbers, index - 1)

# # Ro'yxat berilgan
# numbers = [1, 2, 3, 6, 5, 4]

# # Foydalanuvchidan son kiritish
# N = int(input("Ro'yxatdan son kiriting: "))

# # Ro'yxatda kiritilgan sonning indeksini topish
# if N in numbers:
#     idx = numbers.index(N)
#     # Rekursiya yordamida yig'indini hisoblash
#     yigindi = yigindi_rekursiya(numbers, idx)
#     print(f"Ro'yxatda {N} gacha bo'lgan sonlarning yig'indisi: {yigindi}")
# else:
#     print(f"{N} ro'yxatda mavjud emas.")




# Rekursiv funksiya
# def yigindi_rekursiya(numbers, index):
#     if index == 0:
#         return 0  
#     else:
#         return numbers[index - 1] + yigindi_rekursiya(numbers, index - 1)

# numbers = [1, 2, 3, 6, 5, 4]
# N = int(input("Ro'yxatdan son kiriting: "))

# if N in numbers:
#     idx = numbers.index(N)
#     yigindi = yigindi_rekursiya(numbers, idx)
#     print(f"Ro'yxatda {N} dan kichik bo'lgan sonlarning yig'indisi: {yigindi}")
# else:
#     print(f"{N} ro'yxatda mavjud emas.")




# a=[1,2,3,4,5,6,7,8,9]
# umumiy=0
# for i in a:
#     umumiy +=i



# print(umumiy)


# royxat= [7, 10, 2, 5, 4]
# katta=royxat[0]
# kichik=royxat[0]

# for i in royxat:
#     if i >katta:
#         katta=i
#     elif i< kichik:
#         kichik= i
# print(katta,kichik)


# royxat= [1, 2, 3, 4, 5, 6]
# juft=[]
# toq=[]

# for i in royxat:
#     if i %2==0:
#         juft.append(i)
#     if i %2!=0:
#         toq.append(i)
# print(juft,toq)


# royxat= [1, 2,9,8,9,8,9,4,5, 3, 4]

# kota=royxat[0]
# list.append(kota)
# for i in royxat:
#     if i >kota:
#         kota=i
# print(list)



# a=[1,2,3,4,5,6,7,8,9]

# kotta=0
# for i in a :
#     kotta+=i
# print(kotta)


# a=[15, 25, 35, 45, 55]
# orta=0
# for i in a:
#     orta+=i/len(a)
# print(int(orta))


# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]
# oxshash=numbers[0]
# for i in numbers: 

# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]

# # Takrorlangan elementlarni saqlash uchun ro'yxat
# duplicates = []

# # Elementlarni ko'rgan jamiyat (set)
# seen = set()

# for number in numbers:
#     if number in seen:
#         if number not in duplicates:
#             duplicates.append(number)
#     else:
#         seen.add(number)

#         print("Takrorlangan elementlar:", duplicates)


# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]


# takrorlangan=[]
# korilgan=[]

# for i in numbers:
#     if i in korilgan and i not in takrorlangan:
#         takrorlangan.append(i)
#     else :
#         korilgan.append(i)
# print(takrorlangan)




# numbers = [5, 10, 15, 20, 25]
# teskari=[]
# for i in range(len(numbers)-1,-1,-1):
#     teskari.append(numbers[i])
# print(teskari)


# numbers = [22, 5, 89, 12, 6, 1, 34, 23]
# kichik=numbers[0]

# for i in numbers:
#     if i <kichik:
#         kichik=i

# print(kichik)



# numbers = [22, 5, 89, 12, 6, 1, 34, 23]

# for i in numbers:
#     numbers.sort(i)[:3]


# numbers = [22, 5, 89, 12, 6, 1, 34, 23]


# max=numbers[0]
# min=numbers[0]
# for i in numbers:
#     if i>max:
#         max=i
#     if i<min :
#         min=i
# print(min)
# print(max)




# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]
# juft =[]
# toq=[]
# for i in numbers:
#     if numbers[i] % 2==0:
#         juft.append(numbers[i])
#     else:
#         toq.append(numbers[i])
# print(len(juft))
# print(len(toq))


# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]
# # yegindi=numbers[0]

# # for i in numbers:
# #     yegindi+=numbers[i]
# print(numbers)



# numbers = [1, 2, 3, 4, 3, 5, 6, 2, 7]

# orta=numbers[0]
# for i in numbers:
#     orta+=i/len(numbers)
# print(orta)



# numbers = [1, 2, 3, 1, 5, 9, 4, 3, 5, 6, 2, 7]

# takrorlangan=[]

# list=[]

# for i in numbers:
#     if i in list and i not in takrorlangan:
#         takrorlangan.append(i)
#     else:
#         list.append(i)

# print(takrorlangan)
# print(list)

# a="asdfgh sdfg98756 adsf5151sdfg savdfbg1525 sdsf5dgf41b1"

# ajratilgan=""


# for i in a:
#     if i >= "0" and i <= "9":
#         ajratilgan+=i

# yegindi=0
# for i in ajratilgan:
#     yegindi+=int(i)

# print(yegindi) 
# a=  int(input("son kiriting"))
# for i in range(a):
#     if i>0:
#         if i//3==0 and i//5==0:
#             print("feez bass")
#         elif i //3==0:
#             print("feez")
#         elif i//5==0:
#             print("bass")
#     else:   
#         print("error")