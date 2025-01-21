# # Mavzu: Sort qilish 
# sonlar = [20,30,24,78]
# sonlar.sort()
# print(sonlar)


# # keyngi safar tuple da bolsa 

# sonlar1 = (20,30,24,78) 
# a = sorted(sonlar1)
# sonlar2 = {20,30,24,78}
# b = sorted(sonlar2)
# print(b)



# sonlar3 = {2:"ikki",3:"uch",4:"tort",5:"Besh"}

# print(sonlar3.get(6,"Bu keyda malumot yoq "))

# f = sorted(sonlar3.values())
# print(f)

# # uzunligi bpycha sortlash 
# g = sorted(sonlar3.values(),key = len)
# print(g)


# Yangi funlsiya 

# import math 
# import random

# # a = math.sqrt(25)
# # print(a)
# # p = math.pi
# # e = math.e
# # print(P)
# # print(e)
# # random.radit(a,b) - > a va b sonlar orasidan ixtiyoriy
# # bittasini olib beradi 
# a = random.randint(10,20)
# print(a)
# somlar1 = (23,45,10,34,98)
# # berilgan royhaatdan ixtiyoriy bitta elementni tanlab bering 
# b = random.choice(somlar1)
# print(b)
# talabalar = ["Samir","Jamship","Akosh","Avaz","Akmal"]
# while True:
#     if input("Dastur toxtashish uchun stop ni kiriting ") =="stop":
#         break 
#     talaba = random.choice(talabalar)
#     print(f"tanlangan talaba (talabalar)")
#     talabalar.remove(talabalar)

# import random 
# talabalar = ["Muzrob","Mominjon","Baxtiyor","Dovut","Laziz"]


# while True:
#     if input("Dasturni toxtatish uchun stopni kiriting")=="stop" or len(talabalar):
#         break

#     talaba = random.choice(talabalar)
#     if talaba =="feruz":
#         continue
#     print(f"{talaba}")
#     talabalar.remove




# 1 

    # a = int(input("son kiriting = "))
    # b = abs(a)
    # print(b)



# 2 

# a = float(input("son kiriting = "))
# b = round(a)
# print(a)

# 3 

# a = float(input("som kirit = "))
# b = pow(a)
# print(b)

# 4 

# import random
# tas_dan = random.randint(1,100)
# print(f"tasodifiy tanlgn son {tas_dan}")


# 5 
# royxat = (5,10,15,20)
# a = random.choice(royxat)
# print(a)



# 6 
import random
son = random.randint(1,10)
isFind = False
# son = 28 
for i in range(5,10):
    user = int(input(" 1 dan 50 dan tasodifiy tan son topipishga urinip koring = "))
    if user == son:
        isFind = True
        print("siz tanlangan soni topdingiz")
        break
    elif user > son:
        print("siz katta son tanladingiz")
    elif user < son:
        print("siz kichik son taanladingiz")
if not isFind:
    print("siz yahshi son kiritingiz afsus omad yetishmadi {son}")  