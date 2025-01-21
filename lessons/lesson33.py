# # OOP - 

# class car:

#     color:str = ""
#     engine:str = ""
#     model:str = ""

# # Obyekt yaratish 

# car1 = car()

# # car1 obyektning rangini berish 

# car1.color = "red"
# car1.engine = "electrik"
# car1.model = "sedan"
    
# print(car1.color)
# print(car1.engine)
# print(car1.model)

# ######################################


# color:str = ""
# engine:str = ""
# model: str = ""

# damas = car()

# damas.color = "Damas-Blue"
# damas.engine = "Damas-Gazoil"
# damas.model = "Damas-sedan"


# print(damas.color)
# print(damas.engine)
# print(damas.model)




# ##########################################


# color:str = ""
# engine:str = ""
# model: str = ""

# nexia3 = car()

# nexia3.color = "orange"
# nexia3.engine = "disel"
# nexia3.model = "legenda"


# print(nexia3.color)
# print(nexia3.engine)
# print(nexia3.model)





# class animals:

#  name:str = ""
#  age:int = ""
#  animal:str = ""

# bird = animals()

# bird.name = "But"
# bird.age = "5"
# bird.animal = "Bird"


# print(bird.name)
# print(bird.age)
# print(bird.animal)






# cat = animals()

# cat.name = "Bob"
# cat.age = "10"
# cat.animal = "cat"


# print(cat.name)
# print(cat.age)
# print(cat.animal)



# #####################################################################


# class Car:

#     def __init__(self,color:str,engine:str,model:str):
#         self.color = color
#         self.engine = engine
#         self.model = model

# car2 = Car(color="Red",engine="elctric",model="sedan")
# print(car2.color)
# print(car2.engine)
# print(car2.model)



# car3 = Car(color="Blue",engine="gazoil",model="sedan")
# print(car3.color)
# print(car3.engine)
# print(car3.model)



# car4 = Car(color="Orange",engine="Disel",model="pickup")
# print(car4.color)
# print(car4.engine)
# print(car4.model)



# # class Car:

# #         def __init__(self,color:str,engine:str,model:str):
# #             self.color = color
# #             self.engine = engine
# #             self.model = model

# #         def start (self):
# #               print("Mashina ot oldi")
        
# #         def stop (self):
# #               print("Mashinangiz ochdi")

# # car2 = Car(color="Red",engine="electrik",model="sedan")
# # car2.start()
# # car2.stop()




# # Homework

# # Konstruktorsiz
# # class Student:

# #  name:str = ""
# #  age:int = ""
# #  color:str = ""
# #  sex:str = ""


# # student1 = Student()
# # student1.name = "John"
# # student1.age = 12
# # student1.color = "Fair"
# # student1.sex = "Male"


# # student2 = Student()
# # student2.name = "Sophia"
# # student2.age = 10
# # student2.color = "Fair"
# # student2.sex = "Female"


# # student3 = Student()
# # student3.name = "Lily"
# # student3.age = 11
# # student3.color = "Dark"
# # student3.sex = "Female"


# # print(f"Name: {student1.name}, Age: {student1.age}, Color: {student1.color}, Sex: {student1.sex}")
# # print(f"Name: {student2.name}, Age: {student2.age}, Color: {student2.color}, Sex: {student2.sex}")
# # print(f"Name: {student3.name}, Age: {student3.age}, Color: {student3.color}, Sex: {student3.sex}")




# # Konstruktor bilan



# # class study:
# #     def __init__(self, name, age, color, sex):
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #         self.sex = sex

# #     def display(self):
# #         print(f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Sex: {self.sex}")

# # student4 = study("John", 12, "Fair", "Male")
# # student5 = study("Sophia", 10, "Fair", "Female")
# # student6 = study("Lily", 11, "Dark", "Female")

# # student4.display()
# # student5.display()
# # student6.display()



# class Person:
#     def __init__(self,name:str,age:int,gender:str,occupation:str):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.occupation = occupation

    
#     def walk(self):
#         print(f"{self.walk} is walking")
#     def eat(self):
#         print(f"{self.eat}  is eating")
#     def sleep(self):
#         print(f"{self.sleep}")
#     def work(self):
#         print(f"{self.work}")


# person = Person()
# print(person.name)
# print(person.age)
# print(person.gender)
# print(person.occupation)
# person.sleep()
# person.eat()
# person.walk()






# Tasks OOP (Object Oriented Programming)
# class Military:
#     name:str = ""
#     age:int = ""
#     region:str = ""
#     year:int = ""

# weapon = Military()

# weapon.name = "John"
# weapon.age = "18"
# weapon.region = "Xorazm"
# weapon.year = 2023

# print(weapon.name)
# print(weapon.age)
# print(weapon.region)
# print(weapon.year)

# task2
# class Car:

#     name:str = ""
#     age:int = ""
#     region:str = ""
#     year:int = ""


# cars = Car


# cars.name = "BMW"
# cars.age = "20"
# cars.region = "Germany"
# cars.year = "1992"


# print(cars.name)
# print(cars.age)
# print(cars.region)
# print(cars.year)

# task3
# class Movie:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year

#     def Book(self):
#         print(f"Bu kitobning ismi {self.name}")

#     def MyBook(self):
#         print(f"Bu kitobning yili {self.year}")

# movie = Movie("Harry Potter", "J.K.Rouley", 2000)
# # print(movie.name)
# # print(movie.author)
# # print(movie.year)
# movie.Book()
# movie.MyBook()


# task4

# class Person:
#     def __init__(self, name, age, gender, occupation):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.occupation = occupation

#     def milk(self, amount):
#         print(f"The nurse's name is {self.name}, she is {self.age}, he is {self.occupation}")

# person = Person("Alice", 26, "female", "doctor")
# person.milk()



# # task  amount
# class Person:
#     def __init__(self, name, age, gender, occupation):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.occupation = occupation

#     def milk(self, amount):
#         print(f"The nurse's name is {self.name}, she is {self.age}, he is {self.occupation},  he has got {amount} nuts")

# person = Person("Alice", 26, "female", "doctor")
# person.milk(30)


# Homework OOP 



# Exesice 1 

# class Person:
#     def __init__(self, name, age, gender, occupation):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.occupation = occupation

#     def milk(self, amount):
#         print(f"The nurse's name is {self.name}, she is {self.age}, he is {self.occupation}")

# person = Person("Alice", 26, "female", "doctor")
# person.milk()



# Exesice 2 

# class Animnals:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def popy(self):
#         print(f"The animal name is {self.name}, it's age {self.age}")
    
#     def popins(self, amount, name):
#         print(f"The {self.name}, its {self.age}, The {amount}, its{name}")

#     def birds(self, amount, name):
#         print(f"The {self.name}, it's {self.age},The {amount}, its{name}")
        

# animnals = Animnals("Dog", 9)
# animnals.popy()
# animnals.popins("Cat", 3)
# animnals.birds("Crow",20)


# Exisece 3
 
# class Dog:
#     def __init__(self, breed, age):
#         self.breed = breed
#         self.age = age

#     def bulldok(self,):
#         print(f"The {self.breed}, it's {self.age} years old")

#     def orgdog(self, amaount, year):
#         print(f"The {self.breed}, {self.age} year old and{amaount},{year} years old")

#     def bldog(self, amaount, year):
#         print(f"The {self.breed},{self.age} year old and {amaount},{year} years old")


# dog = Dog("Bulldog", 4)
# dog.bulldok()
# dog.orgdog("Chihuahua", 2)
# dog.bldog("Husky", 6)
        



# Exisece 4 

class Player:
    def __init__(self, name, nationality, position, run, skills, shoot, pass_skill, dribble, header):
        self.name = name
        self.nationality = nationality
        self.position = position
        self.run = run
        self.skills = skills
        self.shoot = shoot
        self.pass_skill = pass_skill
        self.dribble = dribble
        self.header = header

    def player(self):
        return f"Name: {self.name}, Nationality: {self.nationality}, Position: {self.position}"

 


# CR7 obyekti
cr7 = Player(
    name="Cristiano Ronaldo",
    nationality="Portugal",
    position="CF",
    run=99,
    skills=99,
    shoot=99,
    pass_skill=99,
    dribble=98,
    header=99
)

# Messi obyekti
messi = Player(
    name="Lionel Messi",
    nationality="Argentina",
    position="AMF",
    run=9,
    skills=8,
    shoot=4,
    pass_skill=99,
    dribble=99,
    header=0
)

print("CR7 ma'lumotlari:")
print(cr7.player())
print("Run:", cr7.run, "Skills:", cr7.skills, "Shoot:", cr7.shoot)

print("\nMessi ma'lumotlari:")
print(messi.player())
print("Run:", messi.run, "Skills:", messi.skills, "Shoot:", messi.shoot)




# Task 5


# class Student:
#     def __init__(self, name , age, gender, program, studyYaer):
#         self.name = name 
#         self.age = age 
#         self.gender = gender
#         self.program = program
#         self.studyYear = studyYaer

#     def study(self):
#         return f"name: {self.name}, age: {self.age}, {self.gender}"

#     def heldExm(self):
#         print(f"name: {self.gender}, age: {self.program}")

#     def eat(self):
#         return f"name: {self.name}, age: {self.age}, {self.gender}"

#     def walk(self):
#         return f"name: {self.name}, age: {self.age}, {self.gender}"

# rolten = Student("John", 25, "male", "project", 2025)  
# print(rolten.study())
# rolten.heldExm()





# class Teacher:
#     def __init__(self, name, age, gender, designation, salary):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.designation = designation
#         self.salary = salary

#     def teach(self):
#         print(f"Name: {self.name}, age: {self.age}, gender: {self.gender}, designation: {self.designation}, salary: {self.salary}")

#     def takeExam(self):
#         print(f"Name: {self.name}, age: {self.age}, gender: {self.gender}, designation: {self.designation}, salary: {self.salary}")

#     def eat(self):
#         print(f"Name: {self.name}, age: {self.age}, gender: {self.gender}, designation: {self.designation}, salary: {self.salary}")

#     def walk(self):
#         print(f"Name: {self.name}, age: {self.age}, gender: {self.gender}, designation: {self.designation}, salary: {self.salary}")

# tea = Teacher("alice", 23, "male", "project", 2024)
# tea.teach()
# tea.takeExam()
# tea.eat()
# tea.walk()




# class Doctor:
#     def __init__(self, name, age, gender, desig, salary):
#         self.name = name 
    #         self.age = age
    #         self.gender = gender
    #         self.desig = desig
    #         self.salary = salary

    #     def checkUp(self):
    #         return f"Your name {self.name}, he {self.age}, its {self.gender}, {self.desig}, {self.salary}" 

    #     def prescribe(self):
    #         return f"Your name {self.name}, he {self.age}, its {self.gender}, {self.desig}, {self.salary}" 

    #     def eat(self):
    #          return f"Your name {self.name}, he {self.age}, its {self.gender}, {self.desig}, {self.salary}"

    #     def walk(self):
    #          return f"Your name {self.name}, he {self.age}, its {self.gender}, {self.desig}, {self.salary}"

            
    # spaget = Doctor("John", 22 ,"meal", "moon", "go")
    # print(spaget.checkUp())  
    # print(spaget.prescribe())
    # print(spaget.eat())
    # print(spaget.walk())
 












# OOP funksiyasiga set va get orqali funksiya qoshish va yana mayda qoshimchalari bor 


# class Student:
#     def __init__(self, name , age, gender, program, studyYaer):
#         self.name = name 
#         self.age = age 
#         self.gender = gender
#         self.program = program
#         self.studyYear = studyYaer

#     def get(self):
#         return f"name: {self.name}, age: {self.age}, {self.gender}"

#     def set(self):
#         print(f"name: {self.name}, age: {self.age}, {self.gender}")

# rolten = Student("John", 25, "male", "project", 2025)  
# print(rolten.get())
# rolten.set()


