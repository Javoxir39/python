# Mavzu:  Global ozgaruvchi 
# Return qiymat qaytaradi 


# local ozgaruvchi 

# aylana yuzini hisoblaydigon funksiya tuzing 
# global ozgaruvchi - barcha funksiya ichida turib oqish mumkin 
# pi - global ozgaruvchi 
# pi = 3.14
# def aylana(r:float):
#     p = 3.14
#     s = p*r**2
#     l= 2*p*r
#     return s 

# son = aylana(r=10)
# print(son)

# aylanai uzunligini hisoblaydigon funksiya tuzing

# def uzunligi(r:float)->float: # -> qachon yoziladi 
#     p = 3.14
#     l = 2*p*r
#     return l
# lol = uzunligi(20)
# print(lol)





# global opzgaruvchi 

umumiy_pul = 200_000
history = []
def wifi():
    global umumiy_pul
    umumiy_pul = umumiy_pul - 100_000
    print(f"{umumiy_pul} ming pul yechdi")
    history.append("wifiga 100ming tolandi")
def kamunal_tolov():
    global umumiy_pul
    umumiy_pul = umumiy_pul - 80_000
    print(f"{umumiy_pul} ming pul yechdi")
    history.append("wifiga 80ming tolandi")
def begzodga_yordam():
    global umumiy_pul
    umumiy_pul = umumiy_pul + 1_000_000
    print(f"{umumiy_pul} ming pul yechdi")
    history.append("1 mln yordam keldi")

while True:
    if input("Dasturni toxtatish uchun 0 ni kiriting") == "0":
        break
    vazifa  = input("""
    1-wifi pul tolash uchun
    2-kamunal tolovlar
    3-Lazizga yordam
    4-umumiy balansni korish
    5 - history
    """)

    if vazifa =="1":
        wifi()
    elif vazifa == "2":
        kamunal_tolov()
    elif vazifa == "3":
        begzodga_yordam()
    elif vazifa == "4":
        print(f"sizning umumiy pulingiz {umumiy_pul}")
    elif vazifa =="5":
        print(history)
    else:
        print("Bunday tolov yoq")




 