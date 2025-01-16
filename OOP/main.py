class Talaba:
    ism = "Javoxir"
    yosh= 18

javoxir= Talaba()
print(javoxir.ism)
print(javoxir.yosh)

muhammdayusuf= Talaba()
muhammdayusuf.ism="Muuhammadyusuf"
muhammdayusuf.yosh= 19
print(muhammdayusuf.ism)
print(muhammdayusuf.yosh)

class Mashina :
    nomi=""
    nomeri=""
    tezligi=0
    narxi= 0
    rangi=""

    def mashinaPrint(self):
        print(self.nomi,self.nomeri,self.tezligi,self.narxi,self.rangi)




onix= Mashina()
onix.nomi=input("Nomi : ")
onix.nomeri=input("Nomeri : ")
onix.narxi=input("Narxi : ")
onix.rangi=input("Rangi : ")


onix.mashinaPrint()