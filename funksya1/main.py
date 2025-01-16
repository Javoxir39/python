# def summa(*a):
#     yegindi=0
#     for i in a:
#         yegindi+=i
#     return yegindi
# # l=[1,2,3,4,5,6,7,8,9]

# print(summa(1,2,3,4,5,6,7,8,9))




# def info(name, age):
#     print(f"Name:{name}")
#     print(f"Age{age}")

# info(name="Ali",age=18)


# def ParamDefault(name="Ali"):
#     print(f"Hello{name}")

# ParamDefault()



# def number(**a):
#     print(a["g"])

# number(v=1,b=2,g=3,d=5,s=4,y=6)



# abs= lambda x : x if x>0  else -x

# print(abs(7))


# yegindi = lambda x,y: x+y

# n=int(input("n:"))
# m=int(input("m:"))
# print(yegindi(n,m))



# yegindi = lambda x,y: x+y


# n=int(input("n:"))
# m=int(input("m:"))
# print(yegindi(n,m))



# ayirma= lambda x,y: x-y

# n=int(input("n:"))
# m=int(input("m:"))
# print(ayirma(n,m))



# bolinma = lambda x,y: x/y

# n=int(input("n:"))
# m=int(input("m:"))
# print(bolinma(n,m))



# kopaytma = lambda x,y: x*y

# n=int(input("n:"))
# m=int(input("m:"))
# print(kopaytma(n,m))



# pow = lambda x,y: x**y

# n=int(input("n:"))
# m=int(input("m:"))
# print(pow(n,m))


# butun = lambda x,y: x//y

# n=int(input("n:"))
# m=int(input("m:"))
# print(butun(n,m))






# kattaSon = lambda a, b: a if a > b else b ; print(kattaSon(5,-6))


# checklength= lambda p: len(p)

# chekcParol = lambda p: checklength(p) <= 7

# print(chekcParol("5465df5"))



# isDigitmi= lambda p: "raqam"  if 0<p<=9  else "raqam emas "

# print(isDigitmi(10))
p=input()
a= int(input("a:"))
def top(a,p):
    for i in range(len(p)):  
        if a==int(p[i]) :
            return True
    return False
print(top(a,p))