class Person:
    def __init__(self, name, age, region, id):
        self.name = name
        self.age = age
        self.region = region
        self.id = id

    def eat(self):
        print(f"a {self.name} is eating icecream and she is {self.age} years old . she is from {self.region} and she has got an {self.id}")

    def information(self, amount, amoun):
        print(f"the {amount} is {amoun} years old and He is from {self.region} and he has got {self.id}")


person = Person('Alice', 23, 'toshkent', 123456)
person.eat()
person.information('JORJ', 45)





# class Person:
#     name: str = ""
#     age: int = ""
#     region: str = ""
#     id:int = ""

# person = Person()
# person.name = "Alice"
# person.age = 23
# person.region = "Tashkent"
# person.id = 123456

# print(person.name)
# print(person.age)
# print(person.region)
# print(person.id)
# print(f"{person.name} is {person.age}")

