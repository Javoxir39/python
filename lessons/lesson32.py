# Ikkita soni yegindis topadigon funksiya yarating 

# def yegindi(son1:int,son2:int):
#     return son1+son2

# uchta soni  yigindisini topadigon funksiya tuzing 
# def yegindi(son4:int,son5:int,son6:int):
#     return son4+son5+son6




# args bu ozgaruvchi 
# args bu argument 
# qachon ishlatiladi agar ichidagi funksiya nechta argument kelishi nomalum bolsa 
# 
# args da kelgan malumot turi tuple boladi 


# def summa(*args):

#     y = 0

#     for i in args:
     
#          y+=i # y = y + i

#     return y
    
# a = summa(10,20,30,40,50,60,70,80,90,100)
# print(a)


# amaliy mashxulot 
# toq soni nechtaligini aniqlash 

def all(*args):
    y = 0 
    for i in args:
        if i % 2 ==1:
            y+=1
    return y 
a = all(1,2,3,4,5,6,7,8,9)
print(a)



# kwarges bu funksiya 

def talaba_info(**kwargs): 


