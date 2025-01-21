# Mavzu: OOP takrorlash 

class Student:
    def __init__(self,id:int,name:str,surname:str,age:int,group:int,phone:str,money:int):
        self.id:int = id 
        self.name:str = name 
        self.surname:str = surname 
        self.age:int = age 
        self.__group:int = group
        self.phone:str = phone
        self.__money = money


    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,new_money:int):
        if new_money > 0:
            self.__money > new_money


    @property
    def group(self):
        return self.__group
    
    @group.setattr
    def group(self,new_group:int):
        if new_group > 0:
            self.__group > new_group



javlon = Student(1,input("ismi = "),"otabek",20,209,"+9989977065656")

otabek = Student(id = 2,name = "otabek",surname="shuxratov",age=20,group=209,phone="+9989977054545")

print(javlon.group)
javlon.group = 210
print(javlon.group)