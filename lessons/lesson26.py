# def find_max(a,b):
#     if a>b:
#         print(f"{a}son katta{b}dan")
#     elif a==b:
#         print("Bu sonlar teng")
#     else:
#         print(f"{b}son katta {a}dan")

# Mavzu:  Funksiya
# 2 sonni kattasini aniqlash

# a = int(input("a ="))
# b = int(input("b ="))
# find_max(a,b)

# if a>b:
#     print(f"{a}son katta{b}dan")
# else:
#     print(f"{b}son katta{a}dan")


# d = int(input("d = "))
# c = int(input("c = "))
# find_max(d,c)
# if d>c:
#         print(f"{d}son katta{c}dan")
# elif d==c:
#      print("bu sonlar teng")
# else:
#      print(f"{c}son katta{d}dan")



# Mavzu: Def
# qiymat qaytarmaydigon funksiya





# def three_max(a,b,g):
#     natija = max(a,b,c)
#     print(natija)

# def three_max2(son1,son2,son3):
#     katta_son = son1
#     if katta_son < son2:
#         katta_son=son2

#     if katta_son < son3:
#         katta_son = son3

# three_max(2,90,100)
# three_max(30,40,50)





# Funksiya 2 ga bolindi 
# qiymart qaytarmaydigan funksiya 
# 2 - qiymat qaytaradigon funksiya 
# qiymat qaytarish uchun reeturn sozi ishlatiladi 



def find_max(son1,son2):
    if son1>son2:
        return son1
    else:
        return son2
a = find_max(2*50,50-98)
print(a)




