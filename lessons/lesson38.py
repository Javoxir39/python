# Polymorphism = OOP ichida 
# Polymorphism - Bu 

# Son korinishida qoshish Polmyorphism
# a = 20 
# b = 30 
# c = a + b 
# print(c)

# Matin korinishida qoshish 
# matin1 = "Assalom"
# matin2 = "Alaykum"
# matin3 = matin1 + matin2
# print(matin3)



# Funksiyani Inhorntens Eng birimchi olingan vorisni oziga moslash 
# Polifarmizm qilishdan oldin albatta voris olish kerak  


# class Animal:
#     def speak(self):
#         pass

# class Dog (Animal):
#     def speak(self):
#         return "Woof woof"
    
# class Cat (Animal):
#     def speak(self):
#         return "Meow"
# animals:list[Animal] = [Dog(),Cat()]


# for animal in animals:
#     print(animal.speak())




# Task 1  Amaliya ish Misol tariqasida qilingan 


# class Player:
#     def beat(self):
#         pass

#     def protect(self):
#         pass

# # Palmorfiz qilinish jarayoni 
# class Player1 (Player):
#     def  beat(self):
#         print("Sakrab tepadi----")

#     def protect(self):
#         print("Qolda himoya qiladi")


# # Palmorfiz qilinish jarayoni 
# class Player2 (Player):
#     def  beat(self):
#         print("Togridan qoldan zarba----")

#     def protect(self):
#         print("Oyoq bilan himoya qiladi")
    


# while True:
#     choose = input(""" 
#     Oziz uchun oyinchi tanlang
#     1 - Mortol Cambat 
#     2 - Skarpion 
#     """)

#     player:Player == Player()
#     if choose == "1":
#         player = Player1()
#     elif choose == "2":
#         player = Player2
#     else:
#         print("Bunday oyinchi mavjud emas")


#     task = input(""" 
#     1 - Urush 
#     2 - himoya 
#     """)
    
#     if task == "1":
#         player.beat()
#     elif task == "2":
#         player.protect()


# Jaroyom balaralish bitta bajarilishi har hil 





######################################### Task 1 Amaliy mashq Classwork #############################################

# class Printer: 
#     def __init__(self,quality:int):
#         self.__quality = quality

#     def print(self)->str:
#         print("Hello Im black man")
    
#     def SetQualitu(self)->int:
#         print(4050)    

# class LazerPrintert (Printer):
#     def __init__(self, quality):
#         super().__init__(quality)

# # Its my Newclass :)
# class InjetPrinter(Printer):
#     def __init__(self, quality):
#         super().__init__(quality)

#     def print(self)->str:
#         print("Hi Rasul soso")
    
# # New in work 
# class FaxMachine(Printer):
#     def __init__(self, quality):
#         super().__init__(quality)

#     def print(self):
#         print("Life is very beautiful")

# back:list[Printer] = [LazerPrintert(222),InjetPrinter(111),FaxMachine(333)]

# for printer in back:
#     printer.print()
    


####################################################### Task 2 Amaliy mashq classwork ##########################################################
# My work
# class Animal:
#     def __init__(self,color:str):
#         self.__color = color
        
#     def getColor(self)->str:
#         print("Is Gold")

#     def setcolor(self)->str:
#         print("Its very neuatiful")

#     def eat(self)->int:
#         print()

# # New class 
# class Dog (Animal):
#     def __init__(self, color,owner:str):
#         super().__init__(color)
#         self.__owner = owner

#     def  getOwner(self)->str:
#         print("getowner is Rasul")

#     def setOwner(self)->str:
#         print("setOwner is Akmal")

#     def eat(self)->str:
#         print("void eat - Suyag")
    
#     def bark(self)->str:
#         print("void bark - Yoq")

    
# # New class 
# class Lion (Animal):
#     def __init__(self, color,jungleName:str):
#         super().__init__(color)
#         self.__jungleName = jungleName
    
#     def getJungle(self):
#         print("getjungle - Amazonka")

#     def setJungle(self):
#         print("setJungle in Uzbekistan")
    
#     def eat(self):
#         print("void eat - Banana and Apple")

#     def roar(self):
#         print("void roar - soxil shovqini")
    
# lets:list[Animal] = [Dog(),Lion()]
# for print in lets:
#     lets.print()


####################################################### Task 2 Amaliy mashq classwork chatgpt variayant ##########################################################

#  class Animal:
#     def __init__(self, color):
#         self.__color = color

#     def getColor(self):
#         return self.__color

#     def setColor(self, color):
#         self.__color = color

#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def __init__(self, color, owner):
#         super().__init__(color)
#         self.__owner = owner

#     def getOwner(self):
#         return self.__owner

#     def setOwner(self, owner):
#         self.__owner = owner

#     def eat(self):
#         print("Dog is eating")

#     def bark(self):
#         print("Dog is barking")

# class Lion(Animal):
#     def __init__(self, color, jungleName):
#         super().__init__(color)
#         self.__jungleName = jungleName

#     def getJungle(self):
#         return self.__jungleName

#     def setJungle(self, jungleName):
#         self.__jungleName = jungleName

#     def eat(self):
#         print("Lion is eating")

#     def roar(self):
#         print("Lion is roaring")

# # Testing the classes
# if __name__ == "__main__":
#     dog = Dog("Brown", "John")
#     lion = Lion("Golden", "Savannah")

#     print(f"Dog's color: {dog.getColor()}, Owner: {dog.getOwner()}")
#     dog.eat()
#     dog.bark()

#     print(f"Lion's color: {lion.getColor()}, Jungle: {lion.getJungle()}")
#     lion.eat()
#     lion.roar()


####################################################### Task 3 Amaliy mashq classwork ##########################################################


# class Courier:
#     def __init__(self, name:str, home_country:str):
#         self.name = name
#         self.home_country = home_country

#     def calculateShipping(self)->float:
#         print(15,3)

#     def ship(self)->bool:
#         print(True)


# class MonotypeDelivery (Courier):
#     def __init__(self, name, home_country):
#         super().__init__(name, home_country)
    


# class PigeonPost(Courier):
#     def __init__(self, name, home_country):
#         super().__init__(name, home_country)



# count:list[Courier] = [MonotypeDelivery(),PigeonPost()]
# for corer in count:
#     corer.print()
        










