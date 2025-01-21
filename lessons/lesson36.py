# Mavzu: OOP Getwork

# class Animal:
#     def __init__(self, age:int, gender:str):
#         self.age = age
#         self.gender = gender

#     def isMamal(self):
#         return f"Your name {self.age}"
    
#     def mate(self):
#         return f"You {self.gender}"

# animal = Animal(20,"mean")
# print(animal.isMamal())
# print(animal.mate())


# # New class 1

# class Duck (Animal):
#     def __init__(self, age, gender, beakColor:str):
#         super().__init__(age, gender)
#         self.beakColor = beakColor
    
#     def swim(self):
#         return f"You color is {self.beakColor}"
    
#     def quack(self):
#         return f"Your like this"

# duck = Duck(age=21,gender="animal",beakColor="Yellow")
# print(duck.swim())
# print(duck.quack())



# # New Class 2 

# class Fish (Animal):
#     def __init__(self, age, gender, sizeinFt:int, canEat:bool):
#         super().__init__(age, gender)
#         self.__sizeinFt = sizeinFt
#         self.__canEat = canEat

    # @property 
    # def sizeinFt(self)->str:
    #     return self.__sizeinFt
    
    # @sizeinFt.setter
    # def sizeinFt(self, new_sizeinFt:str):
    #     if new_sizeinFt.isalpha():
    #         self.__sizeinFt = new_sizeinFt
    #     else:
    #         ("Malumot qoshib bolmaydi")
    
    # @property 
    # def canEat(self)->bool:
    #     return self.__canEat
    
    # @sizeinFt.setter
    # def canEat(self, new_canEat:str):
    #     if new_canEat.isalpha():
    #         self.__canEat = new_canEat
    #     else:
    #         print("Xatolik yuz berdi qayta tekshitring")
        
#     def swim(self):
#         return f"This is {self.__sizeinFt}"

# fish = Fish(age=21, gender="Animal", sizeinFt="120metr", canEat=True)
# print(fish.sizeinFt)
# print(fish.canEat)




# class Zebra (Animal):
#     def __init__(self, age, gender, iswild:bool):
#         super().__init__(age, gender)
#         self.iswild = iswild
    

#     def run(self):
#         return f"Its {self.iswild}"
    
# zebro = Zebra(age=11, gender="Animal", iswild=True)
# print(zebro.run())




############################### Task 2 #######################



# class Courier:
#     def __init__(self, name:str, home_country:str):
#         self.name = name 
#         self.home_country = home_country

#     def calculeteShipping(self)->float:
#         return 9.2
    
#     def ship(self)->bool:
#         return True
    
# courier = Courier("Jorg", "Mirobod mahallasi")
# print(courier.calculeteShipping())
# print(courier.ship())


# New class 

# class MonotypeDelivery (Courier):
#     def __init__(self, name, home_country,):
#         super().__init__(name, home_country)


    
# mount = MonotypeDelivery(name="Akmal", home_country="Toshkent Mirzo Ulugbek")
# print(mount.ship)



### New class 


# class PigeonPost (Courier):
#     def __init__(self, name, home_country):
#         super().__init__(name, home_country)




# pige = PigeonPost(name="Aziz",home_country="Buxoro")
# print(pige.ship())




################################### Task 3 #####################################

# class Shape:
#     def __init__(self, area:float):
#         self.area = area

#     def Area(self)->float:
#         return 33.4

# shape = Shape(33.22)
# print(shape.Area())


######################################## New class ################################

# class Rectangle (Shape):
#     def __init__(self, area, lenght:float, width:float):
#         super().__init__(area)
#         self.lenght = lenght
#         self.width = width

#     def Rocket(self)->float:
#         return 9.2

#     def getArea(self)->float:
#         return 11.3


# rectangle = Rectangle(area=22,lenght=11,width=90)
# print(rectangle.Rocket())
# print(rectangle.getArea())



######################################## New class ################################

# class Circle (Shape):
#     def __init__(self, area, radius:float):
#         super().__init__(area)
#         self.radius = radius

#     def Lol(self)->float:
#         return 2.2

# circ = Circle(area=3.1,radius=5.1)
# print(circ.Lol)









################################### Task 4 #####################################

# class Employee:
#     def __init__(self, name:str, started:int):
#         self.name = name
#         self.started = started

#     def Employee(self):
#         return f"Funksiya ishlash jarayonida"

#     def Setname(self)->str:
#         return f"Employee name is {self.name}"

#     def Setstarted(self)->int:
#         return f"Employee start at {self.started}"

# emp = Employee("Lily", 17)
# print(emp.Employee())
# print(emp.Setname())
# print(emp.Setstarted())



######################################## New class ################################


# class FullTimeEmployee (Employee):
#     def __init__(self, name, started, pensiontier:int):
#         super().__init__(name, started)
#         self.pensiontier = pensiontier

#     def  FullTimeEmployee(self):
#         return f"Funksiya Ishlayapti"

#     def setPensionTier(self)->int:
#         return f"Bu hodim robot {self.pensiontier}"

# time = FullTimeEmployee(name="Conor", started="Tez orada", pensiontier="Chitiy sport jeg jeg")
# print(time.FullTimeEmployee())
# print(time.setPensionTier())



######################################## New class ################################

# class PartTimeEmployee (Employee):
#     def __init__(self, name, started, hourseworked:int):
#         super().__init__(name, started)
#         self.hourseworked = hourseworked

#     def PartTimeEmployee(self):
#         return f"Funksiya ishladi :)"

#     def setHoursWorked(self)->int:
#         return f"Bu ishchiyam odammi {self.hourseworked}"

# part = PartTimeEmployee(name="Rasul",started="Buguni ozida", hourseworked="Tinimsiz jazo qolaniladi")
# print(part.PartTimeEmployee())
# print(part.setHoursWorked())





###################################  Task 5   #####################################

class Superclass:
    def __init__(self, NewAttribute1:str):
        self.NewAttribute1 = NewAttribute1

    def NewOperation1(self):
        return f"Maxsus tizim togala uchun {self.NewAttribute1}"
super = Superclass("Maxsus")
print(super.NewOperation1())

######################################## New class ################################

class Subclass (Superclass):
    def __init__(self, NewAttribute1):
        super().__init__(NewAttribute1)