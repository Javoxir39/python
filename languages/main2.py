class CarNumber:
    def __init__(self, number_id, car_number, price, status):
        self.number_id = number_id
        self.carnumber = car_number
        self.price = price
        self.status = status



class Users:
    def __init__(self, user_id , name, address, bought_numbers):
        self.user_id = user_id
        self.name = name
        self.address= address
        self.bought_numbers = bought_numbers



class Sell:
    def __init__(self, sell_id, car_number,  user_id, date):
        self.sell_id = sell_id
        self.car_number = car_number
        self.user_id = user_id
        self.date = date


cardlar = {}
boughtcards = {}
users = {}
def carnumbers_list():
    global count
    count =len(cardlar)
    for k,v in cardlar.items():
        if v.status == True:
            print(f"ID: {k} AvtoRaqam: {v.carnumber} Narxi: {v.price} USD ")
        else: # v.status = false
            count -=1
    if count == 0:
        print("Xozircha avtoraqam yoq")



def add_carnumber():
    number = input("Raqamni kiriting XX X XXX XX: ")
    set_price = input("Raqam narxini kiriting $(USD): ")
    if len(number)==8 and  number[0:2].isdigit() and number[2].isalpha and number[3:6].isdigit() and number[6:-1].isalpha() and set_price.isdigit():
        cardlar[len(cardlar) + 1576] = CarNumber(car_number=number, price=set_price,  number_id=len(cardlar)+1576, status=True)
        print("AvtoRaqam muafiqiyatli qoshildi")
    else:
        print("Notogri malumot kiritildi:")    

def edit():
    carnumbers_list()
    if count>0:
        id  = input("Ozgartirmoqchi bolgan AvtoRaqam idsini kiriting: ")
        for k, v in cardlar.items():
            if k == int(id):
                
                while True:
                    number = input("Yangi Avtoraqamni kiriting: ")
                    if len(number)==8 and  number[0:2].isdigit() and number[2].isalpha and number[3:6].isdigit() and number[6:-1].isalpha():
                        v.carnumber = number
                        print("Avtoraqam muafiqiyatli ozgartirildi")
                        break
                    else:
                        print("Raqam notugri kiritildi")
                while True:
                    set_new_price = input("Raqamning yangi narxini kiriting")
                    if set_new_price.isdigit():
                        v.price = set_new_price
                        print("AvtoRaqam narxi muafiqiyatli ozgartirildi")
                        break
                    else:
                        print("Narx notugri kiritildi")
            else:
                print("Bunday IDga ega AvtoRaqamyoq")


def delete():
    carnumbers_list()
    if count>0:
        id = input("ochirmoqchi bolgan Avtoraqam idsini kiriting")
        for k,v in cardlar.items():
            if k == int(id):
                v.status = False
                print("AvtoRaqam ochirildi")
            else:
                print("Bunday IDga ega AvtoRaqam yoq")



def show_history():
    for k, v in boughtcards.items():
        print(f"ID {k}, AvtoRaqam: {v.carnumber}, Narx {v.price}, ")
    if len(boughtcards)==0:
        print("Xozircha AvtoRaqam sotilmagan")


def show_users():
    for k ,v in users.items():
        print(f"ID: {k} Ism: {v.name} Manzil: {v.address} Sotib olingan raqamlar: {v.bought_numbers}")
    if len(users)==0:
        print("Xozircha xech kim AvtoRaqam sotib olmadi")



def buy_carnumber():
    print("AvtoRaqam sotib olish uchun royhatdan otishingiz kerak")
    username = input("Ismingizni kiriting")
    address = input("Manzilingizni kiriting")
    carnumbers_list()
    if len(cardlar)>0:
        id = input("Sotib bolmoqchi bolgan AvtoRaqam id sini kiriting")
        for k ,v in cardlar.items():
            if k == int(id):
                v.status = False
                print("AvtoRaqam muafiqiyatli sotib olindi")
                boughtcards[len(boughtcards) +1] = v
                boughtnumbersofuser = []
                boughtnumbersofuser.append(v.carnumber)
                users[len(users) + 1] = Users(user_id=len(users) + 1, name=username, address=address, bought_numbers=boughtnumbersofuser)
            else:
                print("Bunday IDga ega AvtoRaqam yoq")



def admin_panel():
    password  = "1234"
    login = "1234"
    password_check = input("Parolni kiriting")
    login_check = input("Loginni kiriting")
    if password_check == password and login_check == login:
        while True:
        
            print("""
    1. AvtoRaqamlar royhati
    2. AvtoRaqam qoshish
    3. AvtoRaqamni tahrirlash
    4. AvtoRaqamni ochirish
    5. Sotib olingan raqamlar tarixi
    6. Foydalanuvchilar
    7. Orqaga
    """)
            choice = input("Bolimni tanlang")
            if choice=="1":
                carnumbers_list()
            elif choice=="2":
                add_carnumber()
            elif choice=="3":
                edit()
            elif choice=="4":
                delete()
            elif choice=="5":
                show_history()
            elif choice=="6":
                show_users()
            elif choice=="7":
                break
            else:
                print("Notogri malumot kiritildi")

            
def user_panel():
    while True:
        print("""
1. AvtoRaqamlar Royhati
2. AvtoRaqam sotib olish
3. Orqaga
""")
        result = input("Bolimni tanlang")
        if result == "1":
            carnumbers_list()
        elif result == "2":
            buy_carnumber()
        elif result == "3":
            break
        else:
            print("Notogri malumot kiritildi")
    





print("Assalomu alaykum dasturga xush kelibsiz")

while True:
    print("""
1. Admin
2. Foydalanuvchi
3. Chiqish
""")
    choice = input("Bolimni tanlang")
    if choice =="1":
        admin_panel()
    elif choice == "2":
        user_panel()
    elif choice == "3":
        break
    else:
        print("Notogri malumot kiritildi")

