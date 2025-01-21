# # Mavzu: Funksiyalar 
# # qiymat qaytaradigon 

# def daraja(son:int,daraja,int)->int:
#     return son ** daraja

# # positional qilish 
# def daraja1(son:int,daraja,int/)->int:
#     return son ** daraja
 

# # positional 
# natija = daraja(5,2)

# # named qilish 
# natija = daraja(daraja=2,son=5)




# Yangi mavzu 

# lambda - nomsiz funksiya 
# faqat bir qattor dan tashkil topadi 
# hardoim qiymat qaytaradi 
# qiymatmni qaytarmadigon qilip bolmaydi 

# darajani_hisoblash = lambda son,daraja:son**daraja
# darajani_hisoblash(5,2)


# 
# 5 ta son kelsa shunchaki bir biriga qoshish kerak bolsa 

# hisoblash1 = lambda son1,son2,son3,son4,son5:son1+son2+son3+son4+son5
# print(hisoblash1(1,2,3,4,5))

# Mustsqil ish 
# 3 ta sonni kopaymasini hisoblash lambda funksiya tuzish 

# kopaytirish = lambda son1,son2,son3:son1*son2*son3
# print(kopaytirish(1,2,3))

# Funksiyaning maqsadi 
# bu misolda 2 funksiya bor 







# # maqsad - > talaba info_dan eng uzun ismga ega talabani aniqlash 
# talaba_info = {"Javlon":209,"Jasur":208,"Feruz":209}
# # ("Javlon".209)


# def filitirlash(x:tuple):
#     return len(x(0))


# print(max(talaba_info.items(),key=lambda x:len(x(0))))
# print(max(talaba_info.items(),key=filitirlash))








# funksiyani bashqarish 
# boshqa Logika 
# maqsad - > talaba info_dan eng uzun ismga ega talabani aniqlash 
talaba_info = {"Javlon":209,"Jasur":208,"Feruz":209}
# ("Javlon",209)


# def filtirlash(x:tuple):
#     return len(x[0])


# print(max(talaba_info.items(),key=filtirlash))

# print(max(talaba_info.items(),key=lambda x:len(x[0])))




talaba_info = {"Abrorbek","Jasur","Javlon","Otabek"}
# maqsad - talabalarni ismini uzinligi boycha sort lamoqchiman 
# Sorted - bu funksiya bizga raqam va sonlarni tartiblab beradii 
a = sorted(talaba_info,key=lambda y:len(y))
print(a)


# Amaliy ish 
# shu set (talaba info) ichidagi eng uzun elementni dastur tuzing 

talaba_info = {"Abrorbek","Jasur","Javlon","Otabek"}
a = max(talaba_info,key=lambda y:len(y))
print(a)



# Yangi funksiya 
#
sonlar = [0,40,-60,6]
# maqsad listdan musbat sonlarni ajtatib berij

sonlar2 = list(filter(lambda x:x>=0,sonlar))
print(sonlar2)


# map - degan funksiya 

sonlar3 = list(map(lambda x:x+10,sonlar))
print(sonlar3)
