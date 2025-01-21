
class User:
    def __init__(self,name,phone_number):
        self.name = name 
        self.phone_number = phone_number



class Admin:
    def __init__(self,parol,login):
        self.parol = parol
        self.login = login



class Raqam:
    def __init__(self,nomeri,narxi):
        self.nomeri = nomeri
        self.narxi = narxi
        self.sotilagan = False


    def raqamni_sotildi(self):
        self.sotilaganmi = True 

    
    def show_info(self):
        print(f""" 
    raqami = {self.nomeri}
    narxi = {self.narxi}
        """)

    
    def raqam_qoshish():
        input("Mashinaning raqamini kiriting = ")
        narxi = int(input("Narxi = "))
        raqam = Raqam(nomeri=mashina_raqami,narxi=narxi)
        raqamlar.append(raqamlar)

    def show_number():
        for i in raqamlar:
            if i.sotilganmi == False:
                i.show_info()

    raqamlar:list[Raqam] = []



while True:
   choose = input("""
1 - Admin 
2 - User 
 """)