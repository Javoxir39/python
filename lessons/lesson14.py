# 2,6,8,9 

# 6. Sim karta va telefon raqam tekshiruvi
# 9 xonali telefon raqami berilgan. Raqamning birinchi raqamiga qarab, qaysi operator ekanligini
# aniqlang:
# 9 bilan boshlansa: "Beeline"
# 8 bilan boshlansa: "Ucell"
# 7 bilan boshlansa: "UzMobile"
# Boshqasi bo‘lsa: "Noma'lum operator"

tellnoner = input("Telefon raqam: ")
if len(tellnoner) == 9 and tellnoner.isdigit() :
   if tellnoner [0] == "9":
      print("Beeline")
   elif tellnoner  [0] =="8": 
     print("UMS") 
   elif tellnoner  [0] =="7": 
    print("Ucell")   
   else :
    print("Nomalum operator")

else: 
 print("Siz kiritgan malumot turi mavjud emas")
  

#   9. Pul miqdoriga qarab chegirma hisoblash
# Xarid summasi berilgan. Agar xarid 100 mingdan oshsa, "10% chegirma", 50 ming va 100 ming oralig'ida
# bo'lsa "5% chegirma" deb chiqaring, aks holda "chegirma mavjud emas" deb chiqaring.





# 10. Tezlik nazorati
# Mashina tezligi berilgan. Tezlik 60 km/soatdan oshsa, "Tezlikni kamaytiring" deb chiqaring, agar 40-60
# oralig'ida bo'lsa, "Tezlik mos" deb chiqaring, agar 40 dan past bo'lsa, "Tezlashishingiz mumkin" deb 









# Mashq 

sonlar = [1,2,3,4,5,6,7,8,9,10]
print(sonlar(0))
print(sonlar(1))
print(sonlar(2))
print(sonlar(3))
print(sonlar(4))
print(sonlar(5))
print(sonlar(6))
print(sonlar(7))
print(sonlar(8))
print(sonlar(9))


# for sikll
sum = 0
for i in sonlar:
  sum = sum + i
  print(i)