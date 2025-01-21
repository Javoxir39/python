# Mavzu: 

# task 1 

# class Person:

# class Person:
#     def __init__(self, ismi, yoshi, familiyasi, telefon_raqam):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.familiyasi = familiyasi
#         self.telefon_raqam = telefon_raqam

#     def ismi(self):
#         return f"Your {self.ismi}"
    
#     def yoshi(self):
#         return f"{self.yoshi} years old"
    
#     def familiyasi(self):
#         return f"Surename: {self.familiyasi}"
    
#     def telefon_raqam(self):
#         return f"Phone number: {self.telefon_raqam}"
    
# Shaxs = Person("Jovoh", 21, "Alayorov", +998991268636)
# print(Shaxs.ismi)
# print(Shaxs.yoshi)
# print(Shaxs.familiyasi)
# print(Shaxs.telefon_raqam)


# task 2

#  Person Student 

# class Student:
#     def __init__(self, ismi, yoshi, familiyasi, telraqam, oqish_joy, kursi, speak, eat, study):
#         self.ismi = ismi 
#         self.yosh = yoshi
#         self.familiyasi = familiyasi
#         self.telraqam = telraqam
#         self.oqish_joy = oqish_joy 
#         self.kursi = kursi 
#         self.speak = speak
#         self.eat = eat
#         self.stydy = study
#         self.__pul = 0

#     @property 
#     def pul(self):
#         return self.__pul
    
#     @pul.setter
#     def pul(self,new_pul):
#         if new_pul>=0:
#             self.__pul += new_pul

#         else:
#             print("qarz olinmaydi")

        

#     def ismi(self, ):
#         return f"Your name {self.ismi}, your {self.yoshi} year old, {self.familiyasi}, {self.telraqam}, {self.oqish_joy}, and {self.kursi}, {self.speak}, {self.eat}, {self.study}"



# oquvchi = Student("Laziz", 21, "Azizov", +998991267685, "Tatu", 1, "Ozbekcha", "Moliyachi", "Student" )
# print(oquvchi.ismi())
# oquvchi.pul()



# task 3 



# class Student (Person):
#     def __init__(self, ismi, yoshi, familiyasi, telraqam, oqish_joy, kursi,):
#         super().__init__(ismi=ismi,yoshi=yoshi, familiyasi=familiyasi, telefon_raqam=telraqam)
#         self.oqish_joy = oqish_joy 
#         self.kursi = kursi 


#     def ismi(self):
#         print("ismi")

    
# talaba1 = Student(ismi="Laziz",familiyasi="Azizov",yoshi=21, telraqam= "+998991234455", oqish_joy="Tatu",kursi="Eng")
# print(talaba1.yoshi)




# New 

class Animals:
    def __init__(self, color:str):
        self.__color = color

    @property
    def color(self)->str:
        return self.__color


    @color.setter
    def color (self, new_color:str):
        if new_color.isalpha():
            self.__color = new_color
        else:
            print("raqam qatnashmaydi")

    def eat(srlf):
        print("Animal eat")


# New clas ++ onmly class 


class Dog (Animals):
    def __init__(self, color, owner:str):
        super().__init__(color)
        self.__owner:str = owner

    @property 
    def owner(self)->str:
        return self.__owner

    @owner.setter
    def owner(self, new_owner:str):
        if new_owner.isalpha():
            self.__owner = new_owner
        else:
            print("Isim matindan iborat")

    def bark(self):
        print("Dod is bark")


dog1 = Dog(color="red", owner="Jasur")
print(dog1.color)
dog1.color = "Black"
print(dog1.color)
dog1.eat()



class Lion(Animals):
    def __init__(self, color, jungleName:str):
        super().__init__(color)
        self.__jungleName:str = jungleName

    @property
    def jungleName(self)->str:
        return self.__jungleName

    @jungleName.setter
    def jungleName(self, new_jungleName:str):
        if new_jungleName.isalpha():
            self.__jungleName = new_jungleName
        else:
            print("Bunday shart masjud emas")

    def roar(self):
        print("roar is black")

lion1 = Lion(color="Yellow", jungleName="Jorg")
print(lion1.jungleName)
lion1.color = "Green"
print(lion1.color)        

