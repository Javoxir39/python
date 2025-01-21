# Mavzu: OOP 

# talaba 
# yoshi 
# ismi 
# telefon raqami 
# familiyasi 

ages = [20,22]
names = ["Otabek","Shuhrat"]
suenames = ["Eronov","Tursunboyev"]
phone_numbers = ["+998971111212","+998992333322"]\

print(f"""Talaba malumotlari 
      
ismi = {names[0]}
yoshi = {ages[0]}
familiyasi {suenames[0]}
telefon raqami {phone_numbers[0]}
""")

class Talaba:
    def __init__(self,ismi:str , yoshi:int, familiyasi:str,  telfon_raqami:str):
        self.ismi = ismi
        self.yoshi = yoshi
        self.familiyasi = familiyasi
        self.telefon_raqami = telfon_raqami
        self._pul = 0 
        self.__hemis_parol = ""

    def get_pul(self):
        return self._pul
    
    def set_pul(self,new_pul):
        if new_pul>0:
            self._pul = new_pul
        else:
            print("Biz qarzga ishlamaymiz")


# getter 
    @property 
    def hemis_parol(self):
        return self.__hemis_parol

# Kamida 1 ta kichik harf bitta  katta harf va bitta raqam va uzunligi 4 dan kam bolmasin 

    @hemis_parol.setter
    def hemis_parol(self,new_parol:str):
        katta_harf = 0 
        kichik = 0 
        raqam = 0 
        for i in new_parol:
            if i.isupper():
                katta_harf+=1
            elif i.islower():
                kichik_harf+=1
            elif i.isdigit():
                raqam+=1 
        if katta_harf>=1 and kichik_harf>=1 and len(new_parol)>=4:
            self.__hemis_parol == new_parol
        else:
            print("""
Kuchsiz paril kiritilda,parol ozgartirilmadi,
kamida bitta kichik harf bitta katta harf va bitta raqam va uzunligi 4 dan kam bolmasin
        """)




talaba1 = Talaba(ismi = "Jamshid", familiyasi = "Odilov", telfon_raqami = "+99894232344", yoshi = 30)

talaba1.set_pul(20)
print(talaba1.get_pul())

talaba1.__hemis_parol="ABS123@a"
print(talaba1.hemis_parol)
talaba2 = Talaba(ismi = "Jamshid", familiyasi = "Odilov", telfon_raqami = "+99894232344", yoshi = 30)

